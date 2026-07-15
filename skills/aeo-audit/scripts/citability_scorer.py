#!/usr/bin/env python3
"""
Citability Scorer — analyzes page content for AI citation readiness.

Adapted from geo-seo-claude (zubair-trabzada) with modifications for
aeo-audit workflow. Same 5-category rubric, lightly tuned.

Scoring based on research (Princeton / Georgia Tech / IIT Delhi 2024,
Bortolato 2025): AI-cited passages are 134-167 words, self-contained,
fact-rich, with answer-first structure.

Usage:
    python citability_scorer.py <url>
    # outputs JSON with per-block and page-level scores

    python citability_scorer.py --urls url1,url2,url3 --output out.json
    # batch mode for audit workflow
"""

import argparse
import json
import re
import sys
from typing import Optional

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: install: pip install requests beautifulsoup4 lxml --break-system-packages",
          file=sys.stderr)
    sys.exit(1)


def score_passage(text: str, heading: Optional[str] = None) -> dict:
    """Score one passage across 5 citability categories. Max = 100."""
    words = text.split()
    word_count = len(words)

    scores = {
        "answer_block_quality": 0,     # 0-30 (30% weight)
        "self_containment": 0,         # 0-25 (25%)
        "structural_readability": 0,   # 0-20 (20%)
        "statistical_density": 0,      # 0-15 (15%)
        "uniqueness_signals": 0,       # 0-10 (10%)
    }

    # ---------- 1. Answer Block Quality (30%) ----------
    abq_score = 0

    # Definition patterns anywhere in passage
    for pattern in [
        r"\b\w+\s+is\s+(?:a|an|the)\s",
        r"\b\w+\s+refers?\s+to\s",
        r"\b\w+\s+means?\s",
        r"\b\w+\s+(?:can be |are )?defined\s+as\s",
    ]:
        if re.search(pattern, text, re.IGNORECASE):
            abq_score += 15
            break

    # Answer appears early (first 60 words)
    first_60 = " ".join(words[:60])
    answer_markers = [
        r"\b(?:is|are|was|were|means?|refers?)\b",
        r"\d+%",
        r"\$[\d,]+",
        r"\d+\s+(?:million|billion|thousand)",
    ]
    if any(re.search(p, first_60, re.IGNORECASE) for p in answer_markers):
        abq_score += 15

    # Question-based heading bonus
    if heading and heading.rstrip().endswith("?"):
        abq_score += 10

    # Clear sentence structure (5-25 words)
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    if sentences:
        clear = sum(1 for s in sentences if 5 <= len(s.split()) <= 25)
        abq_score += int(10 * clear / len(sentences))

    # Explicit evidence language
    if re.search(
        r"(?:according to|research shows|studies? (?:show|indicate|suggest|found)|data (?:shows|indicates|suggests))",
        text, re.IGNORECASE,
    ):
        abq_score += 10

    scores["answer_block_quality"] = min(abq_score, 30)

    # ---------- 2. Self-Containment (25%) ----------
    sc_score = 0

    # Optimal word count (134-167 is the research sweet spot)
    if 134 <= word_count <= 167:
        sc_score += 10
    elif 100 <= word_count <= 200:
        sc_score += 7
    elif 80 <= word_count <= 250:
        sc_score += 4
    elif 30 <= word_count <= 400:
        sc_score += 2

    # Low pronoun density
    pronouns = len(re.findall(
        r"\b(?:it|they|them|their|this|that|these|those|he|she|his|her)\b",
        text, re.IGNORECASE,
    ))
    if word_count > 0:
        ratio = pronouns / word_count
        if ratio < 0.02:
            sc_score += 8
        elif ratio < 0.04:
            sc_score += 5
        elif ratio < 0.06:
            sc_score += 3

    # Named entities (proper nouns anchor the passage)
    proper_nouns = len(re.findall(r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b", text))
    if proper_nouns >= 3:
        sc_score += 7
    elif proper_nouns >= 1:
        sc_score += 4

    scores["self_containment"] = min(sc_score, 25)

    # ---------- 3. Structural Readability (20%) ----------
    sr_score = 0

    if sentences:
        avg_len = word_count / len(sentences)
        if 10 <= avg_len <= 20:
            sr_score += 8
        elif 8 <= avg_len <= 25:
            sr_score += 5
        else:
            sr_score += 2

    # Transition/list language
    if re.search(r"\b(?:first|second|third|finally|additionally|moreover|furthermore)\b",
                 text, re.IGNORECASE):
        sr_score += 4
    if re.search(r"(?:\d+[\.\)]\s|\b(?:step|tip|point)\s+\d+)", text, re.IGNORECASE):
        sr_score += 4
    if "\n" in text:
        sr_score += 4

    scores["structural_readability"] = min(sr_score, 20)

    # ---------- 4. Statistical Density (15%) ----------
    sd_score = 0
    sd_score += min(len(re.findall(r"\d+(?:\.\d+)?%", text)) * 3, 6)
    sd_score += min(len(re.findall(
        r"\$[\d,]+(?:\.\d+)?(?:\s*(?:million|billion|M|B|K))?", text)) * 3, 5)
    sd_score += min(len(re.findall(
        r"\b\d+(?:,\d{3})*(?:\.\d+)?\s+(?:users|customers|pages|sites|companies|businesses|people|percent|times)",
        text, re.IGNORECASE)) * 2, 4)
    if re.search(r"\b20(?:2[3-6]|1\d)\b", text):
        sd_score += 2
    for pattern in [
        r"(?:according to|per|from|by)\s+[A-Z]",
        r"(?:Gartner|Forrester|McKinsey|Harvard|Stanford|MIT|Google|Microsoft|OpenAI|Anthropic|Ahrefs|Princeton)",
        r"\([A-Z][a-z]+(?:\s+\d{4})?\)",
    ]:
        if re.search(pattern, text):
            sd_score += 2

    scores["statistical_density"] = min(sd_score, 15)

    # ---------- 5. Uniqueness Signals (10%) ----------
    us_score = 0
    if re.search(
        r"(?:our (?:research|study|data|analysis|survey|findings)|we (?:found|discovered|analyzed|surveyed|measured))",
        text, re.IGNORECASE,
    ):
        us_score += 5
    if re.search(
        r"(?:case study|for example|for instance|in practice|real-world|hands-on)",
        text, re.IGNORECASE,
    ):
        us_score += 3
    if re.search(r"(?:using|with|via|through)\s+[A-Z][a-z]+", text):
        us_score += 2

    scores["uniqueness_signals"] = min(us_score, 10)

    # ---------- Total & grade ----------
    total = sum(scores.values())
    if total >= 80:
        grade, label = "A", "Highly Citable"
    elif total >= 65:
        grade, label = "B", "Good Citability"
    elif total >= 50:
        grade, label = "C", "Moderate Citability"
    elif total >= 35:
        grade, label = "D", "Low Citability"
    else:
        grade, label = "F", "Poor Citability"

    return {
        "heading": heading,
        "word_count": word_count,
        "total_score": total,
        "grade": grade,
        "label": label,
        "breakdown": scores,
        "preview": " ".join(words[:30]) + ("..." if word_count > 30 else ""),
    }


def analyze_page(url: str) -> dict:
    """Fetch page, split into content blocks, score each."""
    try:
        r = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0 (aeo-audit)"},
            timeout=30,
        )
        r.raise_for_status()
    except Exception as e:
        return {"url": url, "error": f"Fetch failed: {e}"}

    soup = BeautifulSoup(r.text, "lxml")
    # Strip non-content
    for el in soup.find_all(["script", "style", "nav", "footer", "header", "aside", "form"]):
        el.decompose()

    blocks, current_heading, current_paras = [], "Introduction", []
    for el in soup.find_all(["h1", "h2", "h3", "h4", "p", "ul", "ol", "table"]):
        if el.name.startswith("h"):
            if current_paras:
                combined = " ".join(current_paras)
                if len(combined.split()) >= 20:
                    blocks.append({"heading": current_heading, "content": combined})
            current_heading = el.get_text(strip=True)
            current_paras = []
        else:
            t = el.get_text(strip=True)
            if t and len(t.split()) >= 5:
                current_paras.append(t)
    if current_paras:
        combined = " ".join(current_paras)
        if len(combined.split()) >= 20:
            blocks.append({"heading": current_heading, "content": combined})

    scored = [score_passage(b["content"], b["heading"]) for b in blocks]

    if not scored:
        # Likely client-side-rendered SPA. Detect evidence and return a finding,
        # not a silent error — this is itself AEO-critical intelligence.
        html_lower = r.text.lower()
        spa_markers = ["<div id=\"root\">", "<div id=\"__next\">", "<div id=\"app\">",
                       "<div id=\"svelte\">", "window.__nuxt__", "<noscript>"]
        spa_detected = any(m in html_lower for m in spa_markers)
        total_body_words = len(re.sub(r"<[^>]+>", " ", r.text).split())
        return {
            "url": url,
            "error": "No content blocks extractable from initial HTML",
            "likely_csr_spa": spa_detected,
            "total_body_words_in_html": total_body_words,
            "aeo_implication": (
                "AI crawlers that do not execute JavaScript (most, including GPTBot and "
                "ClaudeBot by default) will see no content on this page. This is a CRITICAL "
                "technical AEO issue — recommend SSR/SSG migration."
            ) if spa_detected else (
                "Page has content but not in the heading/paragraph structure the scorer recognizes. "
                "Verify manually; page may use unusual markup."
            ),
        }

    avg = sum(b["total_score"] for b in scored) / len(scored)
    top = sorted(scored, key=lambda x: x["total_score"], reverse=True)[:5]
    bottom = sorted(scored, key=lambda x: x["total_score"])[:5]
    grade_dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for b in scored:
        grade_dist[b["grade"]] += 1
    coverage = 100 * sum(1 for b in scored if b["total_score"] >= 70) / len(scored)

    return {
        "url": url,
        "total_blocks_analyzed": len(scored),
        "average_citability_score": round(avg, 1),
        "citability_coverage_pct": round(coverage, 1),
        "optimal_length_passages": sum(1 for b in scored if 134 <= b["word_count"] <= 167),
        "grade_distribution": grade_dist,
        "top_5_citable": top,
        "bottom_5_citable": bottom,
        "all_blocks": scored,
    }


def main():
    parser = argparse.ArgumentParser(description="AI Citability Scorer")
    parser.add_argument("url", nargs="?", help="Single URL (simple mode)")
    parser.add_argument("--urls", help="Comma-separated URLs (batch mode)")
    parser.add_argument("--output", help="Output JSON path (default: stdout)")
    args = parser.parse_args()

    if args.urls:
        urls = [u.strip() for u in args.urls.split(",") if u.strip()]
        results = [analyze_page(u) for u in urls]
        successful = [r for r in results if "error" not in r]
        aggregate = {
            "n_pages": len(results),
            "n_successful": len(successful),
            "site_avg_citability": round(
                sum(r["average_citability_score"] for r in successful) / max(len(successful), 1), 1
            ),
            "site_coverage_pct": round(
                sum(r["citability_coverage_pct"] for r in successful) / max(len(successful), 1), 1
            ),
            "pages": results,
        }
        out = json.dumps(aggregate, indent=2, default=str)
    elif args.url:
        out = json.dumps(analyze_page(args.url), indent=2, default=str)
    else:
        parser.error("Provide either a URL or --urls")

    if args.output:
        with open(args.output, "w") as f:
            f.write(out)
        print(f"Saved: {args.output}", file=sys.stderr)
    else:
        print(out)


if __name__ == "__main__":
    main()
