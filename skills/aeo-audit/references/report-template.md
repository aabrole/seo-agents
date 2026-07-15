# AEO Audit Report Template

Use this as the structure for `AEO-AUDIT-REPORT.md`. Replace all `[placeholder]` values with actual audit findings.

---

```markdown
# AEO Audit: [Brand Name]

**Prepared by:** [Your name / company]
**Date:** [Date]
**URL audited:** [URL]
**Category:** [Detected/provided category]
**Business type:** [SaaS / Local / E-commerce / Publisher / Agency / Hybrid]
**Pages analyzed:** [N]
**Audit mode:** [quick / standard / deep]

---

## Executive Summary

**Overall AEO Score: [X]/100 ([Rating])**

[2-3 sentence plain-English summary. Lead with the most striking finding from the Live Citation Test. Example: "Across 15 strategic queries run against ChatGPT, Claude, and Perplexity, [Brand] was mentioned in only 3 responses. Competitor [Name] was cited 11 times. The underlying cause: [top issue]."]

### Score breakdown

| Dimension | Score | Weight | Contribution |
|---|---:|---:|---:|
| Live Citation Test | [X]/100 | 15% | [X] |
| AI Citability | [X]/100 | 20% | [X] |
| Brand Authority | [X]/100 | 20% | [X] |
| Content CORE-EEAT | [X]/100 | 20% | [X] |
| Technical AEO | [X]/100 | 15% | [X] |
| Schema & Structured Data | [X]/100 | 10% | [X] |
| **Overall AEO Score** | | | **[X]/100** |

---

## 1. Live Citation Test — What AI Systems Actually Say About You

This is the headline finding. We ran 5 strategic prompts against 3 AI systems (15 total queries) to measure real-world AI visibility.

### Summary table

| Prompt type | ChatGPT cited? | Claude cited? | Perplexity cited? | Competitors cited |
|---|:---:|:---:|:---:|---|
| "What is [brand]?" | ✓ / ✗ | ✓ / ✗ | ✓ / ✗ | — |
| "Best [category]?" | Position [N] | Position [N] | Position [N] | [list] |
| "Solution for [problem]?" | ✓ / ✗ | ✓ / ✗ | ✓ / ✗ | [list] |
| "Compare [brand] vs competitors" | Framing: [brand-led / competitor-led / neutral] | … | … | [list] |
| "Alternatives to [top_competitor]?" | ✓ / ✗ | ✓ / ✗ | ✓ / ✗ | [list] |

**Hit rate: [X]/15** ([X]% of queries mentioned the brand)
**Position when mentioned: [average position in ranked lists]**
**Sentiment: [positive / neutral / negative breakdown]**

### Representative quotations (raw AI responses)

**Prompt:** "Best [category] in 2026?"
**Platform:** Perplexity
**Response excerpt:**
> [verbatim excerpt — 2-4 sentences max]

**What this reveals:** [interpretation — e.g., "The brand is not in Perplexity's top-of-mind category list; it favors [competitor list] which have stronger third-party coverage"]

[Repeat for 3-5 representative responses]

### What's driving these results

[Link the Live Citation findings to the site-audit dimensions. Examples:
- "Weak brand recognition in the name-query (0 hits) correlates with the low Brand Authority score (32/100) — specifically the absence of Wikipedia presence and limited YouTube mentions."
- "Competitor [X] wins category queries 4/5 times because they have 3x the FAQ schema coverage and their blog posts follow answer-first structure."
]

---

## 2. Critical Issues (fix this week)

[List 3-8 issues that materially block AEO performance. For each:]

### Issue: [Name]
**Severity:** Critical
**Dimension:** [Technical / Citability / Brand / etc.]
**What's happening:** [Plain-English description]
**Evidence:** [Specific URL / finding]
**Recommended fix:** [Concrete action]
**Expected impact:** [+N points to [dimension] score]

---

## 3. Dimension Deep-Dives

### 3.1 AI Citability ([X]/100)

**What we measured:** How extractable your content is for AI citation across [N] pages.

**Sub-scores:**
- Answer Block Quality: [X]/100
- Self-Containment: [X]/100
- Structural Readability: [X]/100
- Statistical Density: [X]/100
- Uniqueness: [X]/100

**Top 3 strongest pages:**
1. [URL] — [X]/100 — [what's working]
2. …

**Top 3 rewrite priorities:**
1. [URL] — [X]/100

   **Current opening:**
   > [first 2 sentences]

   **Recommended rewrite:**
   > [answer-first, definition-pattern, fact-rich replacement]

2. …

### 3.2 Brand Authority ([X]/100)

**Platform presence:**

| Platform | Score | Notes |
|---|---:|---|
| YouTube | [X]/100 | [channel status, third-party mentions] |
| Reddit | [X]/100 | [subreddit presence, sentiment] |
| Wikipedia | [X]/100 | [page status, Wikidata entry] |
| LinkedIn | [X]/100 | [page activity, thought leadership] |
| Other | [X]/100 | [industry pubs, podcasts, etc.] |

**Key finding:** [The single most important brand-authority insight — typically the platform where absence is most costly]

### 3.3 Content CORE-EEAT ([X]/100)

[Pass/partial/fail summary of the 20 lightweight items or 80 full items]

**Strongest dimensions:** [top 2]
**Weakest dimensions:** [bottom 2]
**Highest-leverage items to fix:** [3-5 specific item IDs with recommendations]

### 3.4 Technical AEO ([X]/100)

**Crawler access:**
- GPTBot: [Allowed / Blocked]
- ClaudeBot: [Allowed / Blocked]
- PerplexityBot: [Allowed / Blocked]
- Google-Extended: [Allowed / Blocked]

**llms.txt:** [Present / Missing / Incomplete]
**Rendering:** [SSR / SSG / Hybrid / CSR-only]
**Core Web Vitals:** [Pass / Mixed / Fail]
**Meta hygiene:** [X]/100

### 3.5 Schema & Structured Data ([X]/100)

**Schemas found:** [list types with counts]
**Required missing:** [Organization / Person / FAQPage / etc.]
**Validation errors:** [count]

**Priority additions:**
1. [schema type on what pages, with estimated effort]
2. …

---

## 4. Quick Wins (implement this week)

[5-10 items with <2 hour effort each, sorted by impact-to-effort ratio]

1. **[Specific action]** — effort: [X hours] — expected lift: +[N] points on [dimension]
2. …

---

## 5. 30-Day Action Plan

### Week 1 — Foundation
- [ ] [Action item]
- [ ] [Action item]

### Week 2 — [Theme]
- [ ] [Action item]

### Week 3 — [Theme]
- [ ] [Action item]

### Week 4 — Verify & Measure
- [ ] Re-run AEO audit
- [ ] Compare Live Citation Test results week-over-week
- [ ] Document score deltas by dimension

---

## 6. 90-Day Trajectory

[If implementing the 30-day plan fully, realistic expectations for where score moves:]
- Live Citation Score: [current] → [projected 90-day] ([+/- N] points)
- Overall AEO Score: [current] → [projected 90-day] ([+/- N] points)

Ground these in the Brand Authority dimension — third-party signals (YouTube, Reddit, Wikipedia) move slowly. Citability and Schema can move fast (days to weeks). Brand Authority realistically moves over 90-180 days.

---

## Appendix A — Pages Analyzed

| URL | Title | Citability Score | Issues Found |
|---|---|---:|---:|
| [url] | [title] | [X] | [N] |

## Appendix B — Raw Live Citation Test Data

[Point to `AEO-AUDIT-DATA.json` for full raw responses]

## Appendix C — Methodology & Attribution

**Scoring frameworks:**
- Citability rubric adapted from [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)
- Brand authority rubric based on Ahrefs Dec 2025 study of 75,000 brands
- CORE-EEAT framework from [core-eeat-content-benchmark v3.0](https://github.com/aaron-he-zhu/core-eeat-content-benchmark)
- Technical AEO rubric adapted from geo-seo-claude and seo-geo-claude-skills

**Audit tool:** aeo-audit skill by [your name] — [link to your site]

---

*This audit represents a point-in-time measurement. AEO is probabilistic. Re-run monthly to track trajectory.*
```
