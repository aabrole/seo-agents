---
name: aeo-audit
description: "Full Answer Engine Optimization (AEO) audit that measures — not just infers — how AI systems like ChatGPT, Claude, Perplexity, and Gemini discover, cite, and recommend a brand. Combines a live-citation test (actually queries AI models and parses responses) with a site-level audit (citability scoring, brand authority, technical crawler access, schema, CORE-EEAT). Produces a composite AEO Score (0-100) with a prioritized 30-day action plan and a client-ready report. Use this skill when the user mentions: 'AEO audit', 'GEO audit', 'AI search visibility', 'get cited by ChatGPT/Claude/Perplexity', 'am I showing up in AI answers', 'answer engine optimization', 'AI-first SEO', or when they want to pitch, scope, or deliver an AEO consulting engagement. Also trigger when a client-style prompt asks to check a brand's presence in AI answers or benchmark it against competitors."
---

# AEO Audit Skill

## What this skill does

Runs a full Answer Engine Optimization audit on a brand or website. Unlike traditional GEO/AEO skills that only *infer* AI visibility from site signals (schema, llms.txt, citability), this skill *measures* it directly by querying AI models and parsing whether the brand appears. The two halves are combined into one composite score with a deliverable report.

**This is the core differentiator:** every existing AEO audit tool reads the site and guesses. This one asks the AI and counts.

## When to use it

- Pitching a new AEO client and needing a fast, credible diagnostic
- Delivering a paid audit as a standalone engagement
- Generating content/lead-magnet material (run against public brands, blog the results)
- Self-audit of your own brand to track AEO progress over time

## High-level workflow

```
INPUT: brand name, homepage URL, category, 2-3 competitor names
  │
  ├─► Phase 1: Live Citation Test (NEW — the differentiator)
  │     Query ChatGPT, Claude, Perplexity with 5 strategic prompts each.
  │     Parse responses for brand mentions, ranking, sentiment, competitors cited.
  │
  ├─► Phase 2: Site-Level Audit (5 parallel subagents)
  │     1. AI Citability scoring    (content extractability)
  │     2. Brand Authority scan      (YouTube, Reddit, Wikipedia, LinkedIn)
  │     3. Technical AEO             (robots.txt, llms.txt, SSR, crawlers)
  │     4. Content CORE-EEAT         (80-item checklist — see references/)
  │     5. Schema & Structured Data  (JSON-LD validation)
  │
  ├─► Phase 3: Score Aggregation
  │     Weighted composite AEO Score (0-100) across all six dimensions.
  │
  └─► OUTPUT: AEO-AUDIT-REPORT.md (client-ready)
              + AEO-AUDIT-DATA.json (raw scores)
              + AEO-AUDIT-REPORT.html (presentation-ready, optional)
```

---

## Phase 1 — Live Citation Test

This is the phase no other AEO skill does. Before any site analysis, find out whether AI models actually cite the brand today.

### Input collection

Ask the user for:
1. **Brand name** (exact spelling)
2. **Homepage URL**
3. **Category** (e.g., "project management software", "Seattle dentist", "sneaker reseller")
4. **2-3 named competitors**
5. **API access** — Anthropic, OpenAI, and Perplexity API keys in env vars (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `PERPLEXITY_API_KEY`). If any are missing, gracefully skip that provider and note it in the report.

### The five strategic prompts

For each brand, generate these prompt variants. These are designed to surface different failure modes:

| # | Prompt type | Template | What it tests |
|---|---|---|---|
| 1 | Name query | "What is {brand}? What do they do?" | Entity recognition — does the AI know the brand exists? |
| 2 | Category query | "What are the best {category} in 2026?" | Top-of-mind recall for the category |
| 3 | Problem query | "I need help with {category-adjacent-problem}. Recommend a solution." | Use-case matching |
| 4 | Competitor comparison | "Compare {brand} to {competitor_1} and {competitor_2}." | Head-to-head framing |
| 5 | Alternative query | "What are good alternatives to {top_competitor}?" | Does the brand show up as an alternative? |

Run each prompt against each available provider (Claude via Anthropic API, GPT via OpenAI API, and Perplexity via their API since it searches the web live). Use `scripts/live_citation_test.py` — it handles parallelization, rate limits, and fallbacks.

### Parsing responses

For each AI response, extract:
- **Mentioned?** — does the brand name appear (case-insensitive, handle variants)?
- **Position** — if mentioned in a list/ranking, what position (1st, 2nd, … nth)?
- **Sentiment** — favorable / neutral / negative (use Claude for this classification — second-pass LLM call)
- **Competitors cited** — which competitors were named instead of or alongside?
- **Citation sources** — for Perplexity specifically, which URLs did it cite?

### Live Citation Score (0-100)

```
Live_Citation_Score = (name_query_hit_rate * 0.20)          # baseline: do they know you exist?
                    + (category_query_position_score * 0.30) # highest weight: can you be discovered?
                    + (problem_query_hit_rate * 0.20)
                    + (comparison_framing_score * 0.15)      # do you show up in your own comparison?
                    + (alternative_query_hit_rate * 0.15)
```

Position scoring: 1st mentioned = 100, 2nd = 80, 3rd = 65, 4th = 50, 5th = 35, beyond = 20, not mentioned = 0.

This score is the first thing in the executive summary. It's the most visceral data point for clients — "ChatGPT ranked your competitor first in 4 of 5 queries. It didn't mention you at all."

---

## Phase 2 — Site-Level Audit

Five parallel subagent analyses. Each produces a 0-100 category score. Detailed rubrics live in reference files so this SKILL.md stays under the 500-line guidance.

### Subagent 1: AI Citability (weight 20%)

Scores how extractable the site's content is for AI citation. Full rubric in **`references/citability-rubric.md`** — load this file before running citability analysis.

Quick summary: 5 sub-dimensions weighted as Answer Block Quality 30%, Self-Containment 25%, Structural Readability 20%, Statistical Density 15%, Uniqueness 10%. Use `scripts/citability_scorer.py` as a first-pass scanner over crawled pages, then read the rubric for rewrite suggestions on the lowest-scoring blocks.

### Subagent 2: Brand Authority (weight 20%)

Measures third-party presence on the platforms AI models weight most heavily. Full rubric in **`references/brand-authority-rubric.md`**.

Quick summary: **YouTube mentions correlate ~0.737 with AI citation** (strongest single signal, per Ahrefs Dec 2025 study of 75,000 brands). Reddit, Wikipedia, LinkedIn follow. Check: brand YouTube channel, third-party video mentions, Reddit recommendation threads, Wikipedia page + Wikidata entry, LinkedIn company presence. Critical counter-intuitive finding: unlinked mentions on these platforms outperform high-DR backlinks for AI visibility.

### Subagent 3: Technical AEO (weight 15%)

Measures infrastructure-level access for AI crawlers. Full rubric in **`references/technical-aeo-rubric.md`**.

Core checks (quick reference):
- `robots.txt` allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot, ChatGPT-User, PerplexityBot, Applebot-Extended
- `llms.txt` file exists at domain root, is well-formed, lists key pages
- SSR/SSG rendering (SPA-only sites are invisible to most AI crawlers)
- Core Web Vitals within Google thresholds
- No domain-level noindex
- Schema.org markup present at Organization level

### Subagent 4: Content CORE-EEAT (weight 20%)

80-item checklist across 8 dimensions: **C**ontextual Clarity, **O**rganization, **R**eferenceability, **E**xclusivity (CORE = content body) × **E**xperience, Exp**e**rtise, **A**uthority, **T**rust (EEAT = source credibility). Full 80-item checklist in **`references/core-eeat-checklist.md`**.

Lightweight mode (default): sample 3-5 high-value pages, evaluate ~20 core items. Full mode: all 80 items across all crawled pages.

### Subagent 5: Schema & Structured Data (weight 10%)

Validates JSON-LD markup and identifies gaps. Full rubric in **`references/schema-rubric.md`**.

Priority schemas for AEO: `Organization`, `Person` (for founder/authors), `FAQPage`, `HowTo`, `Article`, `Product`, `Service`, `LocalBusiness`. Use `scripts/schema_validator.py` to extract and validate existing markup.

---

## Phase 3 — Scoring & Report Generation

### Composite AEO Score

```
AEO_Score = (Live_Citation   * 0.15)   # Phase 1 result
          + (Citability      * 0.20)
          + (Brand_Authority * 0.20)
          + (CORE_EEAT       * 0.20)
          + (Technical_AEO   * 0.15)
          + (Schema          * 0.10)
```

**Why Live Citation is weighted 15% despite being the most important signal conceptually:** the other dimensions are *causes* and Live Citation is the *effect*. Weighting effect too heavily makes the score volatile (a single bad query skews the whole audit). Weighting causes appropriately makes the report actionable.

### Score interpretation

| Score | Rating | Interpretation |
|---|---|---|
| 90-100 | Excellent | Dominant AEO presence. AI systems reliably cite. |
| 75-89 | Good | Strong foundation. Specific optimization opportunities remain. |
| 60-74 | Fair | Mixed signals. Meaningful gaps to close. |
| 40-59 | Poor | Weak AEO presence. Likely invisible in most AI queries. |
| 0-39 | Critical | No meaningful AEO footprint. Ground-up work needed. |

### Issue severity taxonomy

- **Critical (fix this week)** — AI crawlers blocked, no content indexable, zero brand recognition in name-query test
- **High (fix this month)** — Missing llms.txt, no Organization schema, zero third-party AI-trusted mentions, not cited in category-query test
- **Medium (fix this quarter)** — Partial crawler access, thin author bios, low citability scores, no Wikipedia presence
- **Low (ongoing)** — Minor schema errors, alt text gaps, heading hierarchy inconsistencies

### Report output

Generate **three files** (all in working directory):

1. **`AEO-AUDIT-REPORT.md`** — client-ready markdown, ~2000 words, template in `references/report-template.md`
2. **`AEO-AUDIT-DATA.json`** — raw scores, raw AI responses, all sub-scores, for programmatic use
3. **`AEO-AUDIT-REPORT.html`** — optional presentation-ready HTML using the beautiful-slides aesthetic — only generate if user requests OR if running in demo/screen-record mode

The report template follows this structure: Executive Summary (with composite score + radar chart) → Live Citation Test Results (the hero section — actual AI responses quoted) → Site Audit Findings by dimension → Critical Issues → Quick Wins (this week) → 30-Day Action Plan → Appendix (pages analyzed, raw data).

---

## Operating modes

The skill supports three modes. Default is `standard`.

| Mode | Use when | What changes |
|---|---|---|
| `quick` | Cold pitch, 15-min turnaround, no API keys | Skip Phase 1 live citation; Phase 2 limited to 10 pages; CORE-EEAT lightweight (20 items); ~5 min runtime |
| `standard` | Paid audit, billable engagement | All phases, up to 30 pages, full CORE-EEAT lightweight (20 items), ~20 min runtime |
| `deep` | Enterprise client, premium deliverable | All phases, up to 50 pages, full 80-item CORE-EEAT, HTML report included, ~45 min runtime |

User specifies mode via prompt (e.g., "run a quick AEO audit on acme.com"). If unspecified, ask once.

---

## Quality gates (always enforce)

- **Page crawl cap:** 50 pages maximum per audit. Prioritize homepage, nav pages, pricing, about, top blog posts.
- **Rate limiting:** 1 second minimum between page fetches. For AI API calls, respect per-provider rate limits.
- **Robots.txt:** Always check and respect. If the target site blocks AI crawlers, still run the audit (the block itself is a finding) but do not override robots.txt rules when fetching.
- **Error resilience:** Failed fetches/API calls get logged in the appendix but never stop the audit.
- **Timeout:** 30 seconds max per page fetch, 60 seconds max per AI API call.
- **Data retention:** Raw AI responses saved to JSON so the user can verify every claim in the report.
- **Attribution:** Report footer must credit the source rubrics — see `CREDITS.md`. The citability and brand-authority rubrics are lifted (with adaptation) from geo-seo-claude; the 80-item checklist is adapted from core-eeat-content-benchmark.

---

## Reference files (load on demand)

| File | When to load |
|---|---|
| `references/citability-rubric.md` | Running citability subagent (Phase 2.1) |
| `references/brand-authority-rubric.md` | Running brand authority subagent (Phase 2.2) |
| `references/technical-aeo-rubric.md` | Running technical subagent (Phase 2.3) |
| `references/core-eeat-checklist.md` | Running content subagent (Phase 2.4) |
| `references/schema-rubric.md` | Running schema subagent (Phase 2.5) |
| `references/report-template.md` | Generating final report (Phase 3) |
| `references/business-type-adjustments.md` | When detected business type changes weighting (SaaS, local, e-commerce, publisher, agency) |

## Bundled scripts

| Script | Purpose |
|---|---|
| `scripts/live_citation_test.py` | Phase 1 — runs parallel queries across Claude/GPT/Perplexity, parses responses |
| `scripts/citability_scorer.py` | Phase 2.1 — scores page content for AI citability (adapted from geo-seo-claude) |
| `scripts/schema_validator.py` | Phase 2.5 — extracts and validates JSON-LD from HTML |
| `scripts/generate_report.py` | Phase 3 — assembles final markdown report from raw JSON |
| `scripts/generate_html_report.py` | Phase 3 optional — beautiful-slides style HTML report |

---

## Example invocations

**Quick pitch mode, no API keys:**
> "Run a quick AEO audit on stripe.com, category 'payment processing', competitors Adyen and Square."

**Standard audit for a paid client:**
> "Do a full AEO audit on acme-dental.com. They're a dental practice in Portland. Main competitors are pearl-dental.com and brightwhite-ortho.com. I have my API keys set."

**Self-audit with deep mode:**
> "Deep AEO audit on amanabrole.com — I want to see every CORE-EEAT item. Category is 'AI consultant'. My competitors are neilpatel.com and aleydasolis.com."

---

## What this skill is NOT

- Not a replacement for traditional SEO audits (different objective — cite-ability vs. rank-ability). For keyword research, technical SEO, and on-page optimization, use a traditional SEO audit skill.
- Not a content generator. It identifies gaps and suggests rewrites but does not produce finished copy.
- Not a monitoring tool. It's a point-in-time audit. For ongoing monitoring, schedule it to re-run monthly and compare outputs.
- Not a guarantee of citation. AEO is probabilistic. The score measures whether the conditions for citation are met — not whether any specific query will cite the brand.
