# aeo-audit-skill

> **The Claude skill that measures — not guesses — how AI systems see your brand.**
> Runs real queries against ChatGPT, Claude, and Perplexity. Reports what they actually say about you.

<!-- badges: replace with real ones once repo is live -->
![License: MIT](https://img.shields.io/badge/license-MIT-blue)
![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-7c5cff)
![Status: Beta](https://img.shields.io/badge/status-beta-f5a623)

---

## Why this exists

Every AEO audit tool on the market today *infers* how AI systems treat your brand from site signals — schema markup, llms.txt, robots.txt, content structure. That's fine for technical housekeeping, but it doesn't tell you the one thing that matters:

**When someone asks ChatGPT, "What's the best [your category]?" — do you get mentioned or not?**

This skill answers that question directly. It runs 5 strategic prompts against 3 AI providers (15 real queries), parses every response for brand mentions, ranking position, sentiment, and competitor citations. Then combines that with a full site audit (citability, brand authority, technical AEO, CORE-EEAT, schema) into a single composite AEO Score.

You get a client-ready report in markdown, a raw JSON data dump for programmatic use, and a presentation-ready HTML version.

---

## What you get

### The Live Citation Test (the differentiator)

Five strategic prompts, each designed to surface a different failure mode:

| # | Prompt type | What it measures |
|---|---|---|
| 1 | Name query: *"What is [brand]?"* | Entity recognition — does the AI know you exist? |
| 2 | Category query: *"Best [category] in 2026?"* | Top-of-mind recall |
| 3 | Problem query: *"I need help with [X]. Recommend a solution."* | Use-case matching |
| 4 | Comparison: *"Compare [brand] to [competitor_1] and [competitor_2]"* | Head-to-head framing |
| 5 | Alternative: *"What are good alternatives to [top_competitor]?"* | Alternative discoverability |

Each runs against Claude (Anthropic API), GPT-4o (OpenAI API), and Perplexity (web-live). Responses are parsed for mentions, ranking, sentiment (via a second-pass Claude classification), and competitor citations.

### Full site audit (5 parallel analyses)

| Dimension | What it measures |
|---|---|
| **AI Citability** | How extractable your content is — 5-category rubric (Answer Block Quality, Self-Containment, Structure, Stats, Uniqueness) |
| **Brand Authority** | Third-party presence on YouTube, Reddit, Wikipedia, LinkedIn — the platforms AI weights most |
| **Technical AEO** | Crawler access (GPTBot, ClaudeBot, PerplexityBot), llms.txt, SSR/SSG rendering, Core Web Vitals |
| **Content CORE-EEAT** | 80-item checklist across 8 dimensions — Contextual Clarity, Organization, Referenceability, Exclusivity × Experience, Expertise, Authority, Trust |
| **Schema & Structured Data** | JSON-LD validation, priority schemas for AEO (Organization with `sameAs`, FAQPage, HowTo, Person) |

### Composite AEO Score (0-100) with prioritized 30-day action plan

```
AEO_Score = (Live_Citation * 0.15) + (Citability * 0.20) + (Brand_Authority * 0.20)
          + (CORE_EEAT * 0.20) + (Technical_AEO * 0.15) + (Schema * 0.10)
```

Missing a dimension (e.g. no API keys)? Weights renormalize automatically.

---

## Installation

### Prerequisites

- [Claude Code](https://claude.com/product/claude-code) installed
- Python 3.10+ (for the bundled scripts)
- One or more of: `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `PERPLEXITY_API_KEY`, `OPENROUTER_API_KEY` (Phase 1 degrades gracefully if missing)

> **On API keys:** You only need one to run the Live Citation Test. More providers = more coverage — but even one provider's responses give you a directional read on AI visibility. If you don't have the budget for multiple, `OPENROUTER_API_KEY` alone is the best bang-for-buck: it unlocks Gemini, Llama, DeepSeek, Mistral, Qwen, and dozens of others through a single pay-per-use endpoint at [openrouter.ai](https://openrouter.ai).

### Install the skill

```bash
# Clone into your Claude skills directory
git clone https://github.com/aabrole/aeo-audit-skill.git ~/.claude/skills/aeo-audit

# Install Python dependencies
cd ~/.claude/skills/aeo-audit
pip install -r requirements.txt

# Set your API keys (at least one — never commit these)
export ANTHROPIC_API_KEY=sk-ant-...              # from console.anthropic.com
export OPENAI_API_KEY=sk-proj-...                # from platform.openai.com
export PERPLEXITY_API_KEY=pplx-...               # from perplexity.ai/settings/api
export OPENROUTER_API_KEY=sk-or-v1-...           # from openrouter.ai/keys
```

**Via OpenRouter you can query any of these models** (pick the one that matters most for your audit — default is Gemini 2.0 Flash because it's cheap, fast, and the Google entity graph is huge):

```bash
# Default (Gemini 2.0 Flash)
python scripts/live_citation_test.py --brand ... --openrouter-model google/gemini-2.0-flash-001

# Other options
#   google/gemini-2.5-pro           — flagship Google
#   meta-llama/llama-3.3-70b-instruct
#   mistralai/mistral-large
#   deepseek/deepseek-chat
#   qwen/qwen-2.5-72b-instruct
# See openrouter.ai/models for the full catalog.
```

### First run

Open Claude Code and just ask:

```
Run a standard AEO audit on [your domain].
Category: [your category].
Competitors: [comma-separated list].
```

Claude will invoke the skill, run all phases, and drop three files in your working directory:
- `AEO-AUDIT-REPORT.md` — the client-deliverable markdown
- `AEO-AUDIT-DATA.json` — raw scores and every AI response verbatim
- `AEO-AUDIT-REPORT.html` — presentation-ready version (for sharing or screen-recording)

---

## Operating modes

Pick based on how polished the output needs to be:

| Mode | Runtime | Pages | CORE-EEAT | Best for |
|---|---|---|---|---|
| `quick` | ~5 min | 10 | 20 items | Cold pitch, no API keys |
| `standard` | ~20 min | 30 | 20 items | Paid audit |
| `deep` | ~45 min | 50 | 80 items | Enterprise deliverable |

Specify in your prompt:
```
Run a deep AEO audit on linear.app...
```

---

## Example output

See [`examples/`](./examples) for a real audit run (redacted client data). Highlights:

- **Executive summary** with composite score, severity-ranked issues, and projected 90-day trajectory
- **Live Citation Test section** with verbatim AI responses showing exactly how the brand is (or isn't) mentioned
- **30-day action plan** with weekly themes and specific action items
- **Methodology appendix** with scoring weights and attribution

---

## What's in the repo

```
aeo-audit-skill/
├── SKILL.md                       Main skill (Claude loads this into context)
├── README.md                      You are here
├── CREDITS.md                     Attribution to upstream sources
├── LICENSE                        MIT
├── requirements.txt               Python deps
├── references/                    Rubrics loaded on demand
│   ├── citability-rubric.md
│   ├── brand-authority-rubric.md
│   ├── technical-aeo-rubric.md
│   ├── core-eeat-checklist.md
│   ├── schema-rubric.md
│   ├── report-template.md
│   └── business-type-adjustments.md
├── scripts/                       Executable helpers
│   ├── live_citation_test.py      ← the differentiator
│   ├── citability_scorer.py
│   ├── schema_validator.py
│   ├── generate_report.py
│   └── generate_html_report.py
└── evals/evals.json               Test cases
```

---

## Manual script invocation

You can also run the individual scripts directly (useful for CI pipelines or custom workflows):

```bash
# Phase 1 — Live Citation Test
python scripts/live_citation_test.py \
    --brand "Linear" --url "https://linear.app" \
    --category "project management software" \
    --competitors "Jira,Asana,Notion" \
    --output live-citation.json

# Phase 2 — Citability (batch)
python scripts/citability_scorer.py \
    --urls "https://linear.app,https://linear.app/features" \
    --output cit.json

# Phase 2 — Schema validation
python scripts/schema_validator.py \
    --urls "https://linear.app,https://linear.app/features" \
    --output schema.json

# Phase 3 — Assemble report
python scripts/generate_report.py \
    --brand "Linear" --url "https://linear.app" \
    --category "project management software" \
    --live-citation live-citation.json --citability cit.json --schema schema.json

# Phase 3 — Presentation HTML (optional)
python scripts/generate_html_report.py --data AEO-AUDIT-DATA.json
```

---

## Roadmap

Things I'm working on (and would love PRs for):

- [ ] Playwright fallback in citability scorer for client-rendered SPAs
- [ ] Gemini API support in the Live Citation Test
- [ ] Reddit/YouTube API integration for real brand-authority measurement
- [ ] Historical tracking (re-run monthly, diff scores over time)
- [ ] Webhook to post score deltas to Slack/Discord
- [ ] "Private mode" — run the audit without sending prospect data to any AI provider

---

## Contributing

PRs welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md) for how to propose changes, especially to the scoring rubrics.

## Attribution

This skill is a synthesis of excellent open-source work. See [CREDITS.md](./CREDITS.md) for full attribution to:
- [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) by Zubair Trabzada (MIT)
- [core-eeat-content-benchmark](https://github.com/aaron-he-zhu/core-eeat-content-benchmark) by Aaron He-Zhu (Apache-2.0)
- [marketingskills](https://github.com/coreyhaines31/marketingskills) by Corey Haines (MIT)

## License

MIT. Use it, fork it, sell services built on top of it. Just preserve upstream attribution when redistributing the rubrics.

---

**Built by [Aman Abrole](https://amanabrole.com)** — AI builder with AEO specialization.
