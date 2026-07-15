#!/usr/bin/env python3
"""
Live Citation Test — queries AI models directly and measures brand visibility.

This is the core differentiator of the aeo-audit skill: every other AEO tool
infers AI visibility from site signals. This one measures it.

For each brand, generates 5 strategic prompts and runs them against every
configured AI provider (Claude via Anthropic, GPT via OpenAI, Perplexity,
and/or OpenRouter which unlocks Gemini, Llama, DeepSeek, Mistral, and others).
Parses responses for brand mentions, ranking position, sentiment, and
competitor citations.

Usage:
    python live_citation_test.py \\
        --brand "Acme Inc" \\
        --url "https://acme.com" \\
        --category "project management software" \\
        --competitors "Asana,Notion,ClickUp" \\
        --output audit-data/live-citation.json

Environment:
    ANTHROPIC_API_KEY     (optional — enables Claude queries)
    OPENAI_API_KEY        (optional — enables ChatGPT queries)
    PERPLEXITY_API_KEY    (optional — enables Perplexity queries)
    OPENROUTER_API_KEY    (optional — enables any OpenRouter-supported model;
                           default is Google Gemini 2.0 Flash; override via
                           --openrouter-model, e.g. meta-llama/llama-3.3-70b-instruct)

At least one key must be set. Missing providers are skipped gracefully.

Never hardcode API keys in this file. Read them from environment variables only.
"""

import argparse
import asyncio
import json
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from typing import Optional

try:
    import aiohttp
except ImportError:
    print("ERROR: aiohttp required. Install: pip install aiohttp --break-system-packages",
          file=sys.stderr)
    sys.exit(1)


# ------------------------------------------------------------------
# Prompt generation
# ------------------------------------------------------------------

def build_prompts(brand: str, category: str, competitors: list[str]) -> list[dict]:
    """Generate the 5 strategic prompts for a brand."""
    top_competitor = competitors[0] if competitors else "industry leaders"
    competitor_list = ", ".join(competitors[:3]) if competitors else "top competitors"

    return [
        {
            "id": "name_query",
            "label": "Name query (entity recognition)",
            "prompt": f"What is {brand}? What do they do, and who are their typical customers?",
        },
        {
            "id": "category_query",
            "label": "Category query (top-of-mind recall)",
            "prompt": f"What are the best {category} in 2026? Give a ranked list with brief reasoning for each.",
        },
        {
            "id": "problem_query",
            "label": "Problem query (use-case matching)",
            "prompt": f"I'm looking for a {category} solution. What do you recommend and why?",
        },
        {
            "id": "comparison_query",
            "label": "Comparison query (head-to-head framing)",
            "prompt": f"Compare {brand} to {competitor_list}. What are the main differences?",
        },
        {
            "id": "alternative_query",
            "label": "Alternative query (alternative discoverability)",
            "prompt": f"What are good alternatives to {top_competitor} for {category}?",
        },
    ]


# ------------------------------------------------------------------
# Provider clients (async)
# ------------------------------------------------------------------

async def query_anthropic(session: aiohttp.ClientSession, prompt: str, api_key: str) -> str:
    """Query Claude via the Anthropic Messages API."""
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    payload = {
        "model": "claude-opus-4-7",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": prompt}],
    }
    async with session.post(url, headers=headers, json=payload, timeout=60) as r:
        data = await r.json()
        if r.status != 200:
            raise RuntimeError(f"Anthropic {r.status}: {data}")
        return "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")


async def query_openai(session: aiohttp.ClientSession, prompt: str, api_key: str) -> str:
    """Query GPT via the OpenAI Chat Completions API."""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "gpt-4o",  # Stable, broadly-available model. Swap as needed.
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1024,
    }
    async with session.post(url, headers=headers, json=payload, timeout=60) as r:
        data = await r.json()
        if r.status != 200:
            raise RuntimeError(f"OpenAI {r.status}: {data}")
        return data["choices"][0]["message"]["content"]


async def query_perplexity(session: aiohttp.ClientSession, prompt: str, api_key: str) -> dict:
    """Query Perplexity — returns text AND the citation URLs (unique to Perplexity)."""
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "sonar-pro",
        "messages": [{"role": "user", "content": prompt}],
        "return_citations": True,
    }
    async with session.post(url, headers=headers, json=payload, timeout=60) as r:
        data = await r.json()
        if r.status != 200:
            raise RuntimeError(f"Perplexity {r.status}: {data}")
        return {
            "text": data["choices"][0]["message"]["content"],
            "citations": data.get("citations", []),
        }


async def query_openrouter(
    session: aiohttp.ClientSession,
    prompt: str,
    api_key: str,
    model: str = "google/gemini-2.0-flash-001",
) -> str:
    """
    Query any OpenRouter-hosted model. Unlocks Gemini, Llama, DeepSeek, Mistral,
    and dozens more through one API. Model is configurable via --openrouter-model.

    Popular choices (as of 2026):
      google/gemini-2.0-flash-001   — fast, cheap, great for AEO testing
      google/gemini-2.5-pro         — flagship Google
      meta-llama/llama-3.3-70b-instruct
      mistralai/mistral-large
      deepseek/deepseek-chat
      qwen/qwen-2.5-72b-instruct
    """
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        # OpenRouter recommends these for attribution; harmless if absent.
        "HTTP-Referer": "https://github.com/aeo-audit-skill",
        "X-Title": "aeo-audit-skill",
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1024,
    }
    async with session.post(url, headers=headers, json=payload, timeout=60) as r:
        data = await r.json()
        if r.status != 200:
            raise RuntimeError(f"OpenRouter {r.status}: {data}")
        return data["choices"][0]["message"]["content"]


# ------------------------------------------------------------------
# Response parsing
# ------------------------------------------------------------------

def normalize(s: str) -> str:
    """Lowercase, collapse whitespace for matching."""
    return re.sub(r"\s+", " ", s.lower().strip())


def brand_variants(brand: str) -> list[str]:
    """Generate plausible brand variants for matching."""
    b = brand.strip()
    variants = {b, b.lower(), b.upper()}
    # Strip common suffixes
    for suffix in [" Inc", " LLC", " Ltd", " Co", ", Inc.", ", LLC", ".com"]:
        if b.endswith(suffix):
            variants.add(b[: -len(suffix)].strip())
    # Add lowercase/no-spaces variant
    variants.add(b.lower().replace(" ", ""))
    return [v for v in variants if v]


def find_mention(response_text: str, brand: str) -> bool:
    """Check if brand (or variants) appears in the response."""
    text_norm = normalize(response_text)
    for v in brand_variants(brand):
        if normalize(v) in text_norm:
            return True
    return False


def find_position(response_text: str, brand: str) -> Optional[int]:
    """
    If the response contains a ranked list, find the brand's position.
    Returns None if not in a ranked list or not found.

    Heuristic: look for numbered lists (1., 2., …) or enumeration patterns
    and find which numbered item contains the brand.
    """
    # Split on numbered list patterns
    # Matches: "1.", "1)", "1:", "**1.", etc.
    pattern = r"(?:^|\n)\s*(?:\*\*)?\s*(\d+)[.):]\s*(.+?)(?=(?:\n\s*(?:\*\*)?\s*\d+[.):]\s)|\Z)"
    matches = re.findall(pattern, response_text, flags=re.DOTALL)
    if not matches:
        return None

    brand_forms = [normalize(v) for v in brand_variants(brand)]
    for num_str, content in matches:
        content_norm = normalize(content)
        if any(bf in content_norm for bf in brand_forms):
            try:
                return int(num_str)
            except ValueError:
                continue
    return None


def find_competitor_mentions(response_text: str, competitors: list[str]) -> list[str]:
    """Which competitors were mentioned in the response?"""
    text_norm = normalize(response_text)
    mentioned = []
    for c in competitors:
        for v in brand_variants(c):
            if normalize(v) in text_norm:
                mentioned.append(c)
                break
    return mentioned


def position_to_score(position: Optional[int]) -> int:
    """Convert ranking position to a score (0-100)."""
    if position is None:
        return 0
    if position == 1:
        return 100
    if position == 2:
        return 80
    if position == 3:
        return 65
    if position == 4:
        return 50
    if position == 5:
        return 35
    return 20  # mentioned but beyond top 5


# ------------------------------------------------------------------
# Sentiment (via Claude second-pass)
# ------------------------------------------------------------------

async def classify_sentiment(
    session: aiohttp.ClientSession,
    response_text: str,
    brand: str,
    anthropic_key: Optional[str],
) -> str:
    """
    Classify how the brand is portrayed in the response.
    Returns: 'favorable' | 'neutral' | 'negative' | 'not_mentioned' | 'unknown'
    """
    if not find_mention(response_text, brand):
        return "not_mentioned"
    if not anthropic_key:
        return "unknown"

    classifier_prompt = f"""Classify how the brand "{brand}" is portrayed in the following text. Respond with EXACTLY one word: favorable, neutral, or negative.

Text:
---
{response_text[:2000]}
---

One word answer:"""
    try:
        result = await query_anthropic(session, classifier_prompt, anthropic_key)
        answer = result.strip().lower().split()[0] if result.strip() else "unknown"
        if answer in ("favorable", "positive"):
            return "favorable"
        if answer in ("negative", "unfavorable"):
            return "negative"
        if answer == "neutral":
            return "neutral"
        return "unknown"
    except Exception:
        return "unknown"


# ------------------------------------------------------------------
# Main orchestration
# ------------------------------------------------------------------

@dataclass
class QueryResult:
    prompt_id: str
    prompt_label: str
    prompt_text: str
    provider: str
    response_text: str = ""
    mentioned: bool = False
    position: Optional[int] = None
    position_score: int = 0
    sentiment: str = "unknown"
    competitors_mentioned: list[str] = field(default_factory=list)
    citations: list[str] = field(default_factory=list)
    error: Optional[str] = None


async def run_single(
    session: aiohttp.ClientSession,
    prompt_info: dict,
    provider: str,
    api_key: str,
    brand: str,
    competitors: list[str],
    anthropic_key_for_sentiment: Optional[str],
    extras: Optional[dict] = None,
) -> QueryResult:
    """Run one provider × one prompt. `extras` passes per-provider options
    (e.g. {'model': 'google/gemini-2.0-flash-001'} for OpenRouter)."""
    extras = extras or {}
    qr = QueryResult(
        prompt_id=prompt_info["id"],
        prompt_label=prompt_info["label"],
        prompt_text=prompt_info["prompt"],
        provider=provider,
    )
    try:
        if provider == "anthropic":
            qr.response_text = await query_anthropic(session, prompt_info["prompt"], api_key)
        elif provider == "openai":
            qr.response_text = await query_openai(session, prompt_info["prompt"], api_key)
        elif provider == "perplexity":
            result = await query_perplexity(session, prompt_info["prompt"], api_key)
            qr.response_text = result["text"]
            qr.citations = result["citations"]
        elif provider == "openrouter":
            model = extras.get("model", "google/gemini-2.0-flash-001")
            qr.response_text = await query_openrouter(
                session, prompt_info["prompt"], api_key, model=model
            )
            # Record which model was used for this provider (since OpenRouter multiplexes)
            qr.provider = f"openrouter:{model}"
        else:
            qr.error = f"Unknown provider: {provider}"
            return qr
    except Exception as e:
        qr.error = str(e)
        return qr

    qr.mentioned = find_mention(qr.response_text, brand)
    qr.position = find_position(qr.response_text, brand)
    qr.position_score = position_to_score(qr.position)
    qr.competitors_mentioned = find_competitor_mentions(qr.response_text, competitors)
    qr.sentiment = await classify_sentiment(
        session, qr.response_text, brand, anthropic_key_for_sentiment
    )
    return qr


def calculate_live_citation_score(results: list[QueryResult]) -> dict:
    """Aggregate per-prompt-type scores into the composite Live Citation Score."""
    by_type: dict[str, list[QueryResult]] = {}
    for r in results:
        if r.error:
            continue
        by_type.setdefault(r.prompt_id, []).append(r)

    def avg_hit_rate(group: list[QueryResult]) -> float:
        if not group:
            return 0
        return 100 * sum(1 for r in group if r.mentioned) / len(group)

    def avg_position_score(group: list[QueryResult]) -> float:
        if not group:
            return 0
        return sum(r.position_score for r in group) / len(group)

    # Comparison framing: did brand appear favorably vs. buried/absent?
    def comparison_framing(group: list[QueryResult]) -> float:
        if not group:
            return 0
        score = 0
        for r in group:
            if not r.mentioned:
                score += 0
            elif r.sentiment == "favorable":
                score += 100
            elif r.sentiment == "neutral":
                score += 60
            elif r.sentiment == "negative":
                score += 20
            else:
                score += 50
        return score / len(group)

    name_score = avg_hit_rate(by_type.get("name_query", []))
    category_score = avg_position_score(by_type.get("category_query", []))
    problem_score = avg_hit_rate(by_type.get("problem_query", []))
    comparison_score = comparison_framing(by_type.get("comparison_query", []))
    alternative_score = avg_hit_rate(by_type.get("alternative_query", []))

    composite = (
        name_score * 0.20
        + category_score * 0.30
        + problem_score * 0.20
        + comparison_score * 0.15
        + alternative_score * 0.15
    )

    return {
        "composite_score": round(composite, 1),
        "sub_scores": {
            "name_query_hit_rate": round(name_score, 1),
            "category_query_position_score": round(category_score, 1),
            "problem_query_hit_rate": round(problem_score, 1),
            "comparison_framing_score": round(comparison_score, 1),
            "alternative_query_hit_rate": round(alternative_score, 1),
        },
        "n_queries_total": len(results),
        "n_queries_successful": sum(1 for r in results if not r.error),
        "n_mentions": sum(1 for r in results if r.mentioned and not r.error),
    }


async def main_async(args):
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
    openai_key = os.environ.get("OPENAI_API_KEY")
    perplexity_key = os.environ.get("PERPLEXITY_API_KEY")
    openrouter_key = os.environ.get("OPENROUTER_API_KEY")

    # Each tuple: (provider_name, api_key, extras_dict)
    providers = []
    if anthropic_key:
        providers.append(("anthropic", anthropic_key, {}))
    if openai_key:
        providers.append(("openai", openai_key, {}))
    if perplexity_key:
        providers.append(("perplexity", perplexity_key, {}))
    if openrouter_key:
        providers.append(("openrouter", openrouter_key, {"model": args.openrouter_model}))

    if not providers:
        print("ERROR: No API keys configured. Set at least one of "
              "ANTHROPIC_API_KEY, OPENAI_API_KEY, PERPLEXITY_API_KEY, "
              "OPENROUTER_API_KEY.",
              file=sys.stderr)
        sys.exit(1)

    provider_labels = [
        f"{p[0]}:{p[2]['model']}" if p[0] == "openrouter" else p[0]
        for p in providers
    ]

    print(f"Running live citation test for '{args.brand}'", file=sys.stderr)
    print(f"  Category: {args.category}", file=sys.stderr)
    print(f"  Competitors: {args.competitors}", file=sys.stderr)
    print(f"  Providers: {provider_labels}", file=sys.stderr)

    competitors = [c.strip() for c in args.competitors.split(",") if c.strip()]
    prompts = build_prompts(args.brand, args.category, competitors)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for prompt_info in prompts:
            for provider_name, api_key, extras in providers:
                tasks.append(run_single(
                    session, prompt_info, provider_name, api_key,
                    args.brand, competitors, anthropic_key, extras,
                ))
        results = await asyncio.gather(*tasks)

    # Assemble output
    output = {
        "brand": args.brand,
        "url": args.url,
        "category": args.category,
        "competitors": competitors,
        "providers_used": provider_labels,
        "n_queries": len(results),
        "scoring": calculate_live_citation_score(results),
        "raw_results": [asdict(r) for r in results],
    }

    if args.output:
        os.makedirs(os.path.dirname(os.path.abspath(args.output)) or ".", exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2)
        print(f"Saved: {args.output}", file=sys.stderr)
    else:
        print(json.dumps(output, indent=2))

    # Always print the composite score to stderr for visibility
    print(f"\nLive Citation Score: {output['scoring']['composite_score']}/100",
          file=sys.stderr)
    print(f"  Mentions: {output['scoring']['n_mentions']}/{output['scoring']['n_queries_total']}",
          file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="Live Citation Test for AEO audit")
    parser.add_argument("--brand", required=True, help="Brand name (exact spelling)")
    parser.add_argument("--url", required=True, help="Homepage URL")
    parser.add_argument("--category", required=True,
                        help="Category, e.g. 'project management software'")
    parser.add_argument("--competitors", required=True,
                        help="Comma-separated competitor names")
    parser.add_argument("--output", help="Output JSON path (default: stdout)")
    parser.add_argument(
        "--openrouter-model",
        default="google/gemini-2.0-flash-001",
        help=("Model slug for OpenRouter provider (if OPENROUTER_API_KEY is set). "
              "Examples: google/gemini-2.0-flash-001, google/gemini-2.5-pro, "
              "meta-llama/llama-3.3-70b-instruct, mistralai/mistral-large, "
              "deepseek/deepseek-chat, qwen/qwen-2.5-72b-instruct. "
              "See openrouter.ai/models for the full catalog."),
    )
    args = parser.parse_args()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
