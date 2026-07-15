# Citability Rubric (AI Extractability Scoring)

> Adapted from geo-seo-claude `geo-citability` skill. Research foundation: Princeton / Georgia Tech / IIT Delhi GEO studies (2024), Bortolato (2025), Ahrefs (Dec 2025).

## Core insight

AI language models preferentially cite passages that are:
- **134-167 words long** (optimal extraction length)
- **Self-contained** (understandable without surrounding context)
- **Fact-rich** (specific statistics, dates, named entities)
- **Answer-first** (the answer appears in the first 1-2 sentences)

Citability is fundamentally different from SEO copywriting. SEO copy optimizes for keyword density and engagement. Citability optimizes for *extractability* — how easily an AI can pull a passage verbatim as a direct answer.

## Scoring formula

```
Block_Citability = (Answer_Block_Quality   * 0.30)
                 + (Self_Containment       * 0.25)
                 + (Structural_Readability * 0.20)
                 + (Statistical_Density    * 0.15)
                 + (Uniqueness             * 0.10)
```

Page-level score = average of all block scores. Citability Coverage = % of blocks scoring above 70.

---

## 1. Answer Block Quality (30%)

Does content open with clear, quotable direct answers?

| Score | Criteria |
|---|---|
| 90-100 | Every major section opens with a 1-2 sentence direct answer using "X is…" or "X refers to…" patterns. First 40-60 words stand alone. |
| 70-89 | Most sections have clear answer openings. Some definition patterns. Answers identifiable but may need minor context. |
| 50-69 | Some answer-like openings. Many sections bury the answer in the middle/end. Few explicit definition patterns. |
| 30-49 | Answers buried in long paragraphs. Content is narrative-driven rather than answer-driven. |
| 0-29 | No identifiable answer blocks. Entirely narrative, conversational, or fragmented. |

**Signals to detect programmatically:**
- Definition patterns: `"X is [a/an/the]..."`, `"X refers to..."`, `"X means..."`, `"X can be defined as..."`
- Answer-first structure: answer in first sentence, detail follows
- Quantified answers: "The average cost of X is $Y" (not "Many factors affect the cost")
- Comparison answers: "X differs from Y in three ways: [list]"

**High-citability example:**
> Content delivery networks (CDNs) are distributed server systems that cache and serve web content from locations geographically close to end users. A CDN reduces latency by 50-70% on average. The three largest CDN providers are Cloudflare, Amazon CloudFront, and Akamai Technologies.

*58 words. Self-contained. 3 specific facts. Definition pattern. Score: ~95.*

**Low-citability example:**
> If you've ever wondered why some websites load faster than others, the answer might surprise you. There's this amazing technology that has been around for a while now. Let me explain how it works and why you should care about it.

*52 words. No topic named. 0 facts. No definition. Score: ~15.*

---

## 2. Self-Containment (25%)

Can a passage be extracted and understood without surrounding content?

| Score | Criteria |
|---|---|
| 90-100 | 80%+ of blocks are fully self-contained. Each passage names its subject explicitly. No pronoun references to earlier content. |
| 70-89 | 60-79% self-contained. Most passages name subjects. Occasional pronoun references needing context. |
| 50-69 | 40-59% self-contained. Mixed explicit/pronoun use. Some passages require prior reading. |
| 30-49 | 20-39% self-contained. Heavy pronoun reliance. Most passages need surrounding text. |
| 0-29 | Under 20%. Continuous narrative where extraction loses meaning. |

**Per-block checklist:**
1. Does the passage name the subject explicitly (not "it," "this," "they")?
2. Can the main point be understood from ONLY this passage?
3. Does it contain ≥1 specific fact/stat/named entity?
4. Is the word count 50-200?
5. Does it avoid opening with "But," "However," "And" (implies prior context)?

---

## 3. Structural Readability (20%)

Formatting that helps AI parse and segment content.

| Score | Criteria |
|---|---|
| 90-100 | Clean H1>H2>H3 hierarchy. Question-based headings. Short paragraphs (2-4 sentences). Tables for comparisons. Ordered lists for processes. |
| 70-89 | Good hierarchy with minor skips. Some question-headings. Mostly short paragraphs. Some tables/lists. |
| 50-69 | Inconsistent hierarchy. Few question-headings. Mix of paragraph lengths. Limited tables/lists. |
| 30-49 | Minimal headings. No question-headings. Long paragraphs dominate. |
| 0-29 | No hierarchy or broken. Wall-of-text. No tables/lists. |

**Best practices:**
- H1 (page) > H2 (sections) > H3 (subsections). Never skip levels.
- Question-based headings: "What is [topic]?" / "How does [topic] work?" match AI query patterns
- 2-4 sentence paragraphs
- Tables for any 3+ item comparison — AI extracts table data with high accuracy
- Ordered lists for sequential processes, unordered for non-sequential
- Bold first use of important terms for entity recognition

---

## 4. Statistical Density (15%)

Specific, verifiable data points AI systems prioritize when selecting sources.

| Score | Criteria |
|---|---|
| 90-100 | 5+ specific statistics per 500 words. Named sources. Exact numbers. Percentages, dollar amounts, timeframes. |
| 70-89 | 3-4 stats per 500 words. Most claims sourced. Mostly specific numbers. |
| 50-69 | 1-2 stats per 500 words. Some sourcing. Mixed specific/vague. |
| 30-49 | <1 stat per 500 words. Few sourced claims. |
| 0-29 | No statistics. No sourced claims. All quantifiers vague. |

**Counts as a statistic:**
- Specific percentages: "73% of marketers report..."
- Dollar amounts: "Average cost is $4,500 per month"
- Timeframes: "Implementation takes 6-8 weeks"
- Named studies: "Per the 2025 HubSpot State of Marketing Report..."
- Specific counts: "Integrates with 340+ tools"
- Comparison data: "40% faster than industry average"

**Does NOT count:**
- "Many companies use..." (vague)
- "A significant percentage..." (vague)
- "Studies show that..." (no named source)
- "Experts agree..." (no named experts)

---

## 5. Uniqueness & Original Data (10%)

Information AI cannot find elsewhere, making the source necessary.

| Score | Criteria |
|---|---|
| 90-100 | First-party research, proprietary data, original surveys, unique datasets. Methodological transparency. |
| 70-89 | Some original insights or unique analysis of existing data. Distinct perspective with original examples. |
| 50-69 | Mostly synthesis with some unique commentary/examples. |
| 30-49 | Largely derivative. Restates common knowledge. |
| 0-29 | Entirely derivative. Often verbatim on higher-authority sources. |

**Signals of uniqueness:**
- "Our analysis of [X] data found..."
- "We surveyed [N] [professionals] and found..."
- "Based on our experience with [N] clients..."
- Custom charts, graphs, visualizations
- Case studies with specific named outcomes
- Original frameworks or taxonomies

---

## Rewrite workflow (for blocks scoring below 60)

For each low-scoring block:

1. **Identify primary weakness** — buried answer / no facts / poor structure / derivative / pronoun-heavy
2. **Propose rewritten opening** — answer-first or definition pattern, name the subject explicitly
3. **Suggest specific facts to add** — look for numbers, percentages, named sources, timeframes
4. **Recommend structural fixes** — split long paragraph, add table, convert to list, add question-heading

## Reference data (cite in reports)

- Optimal passage length for AI citation: **134-167 words** (Bortolato 2025, AI Overview passage analysis)
- Definition patterns increase citation rate by **2.1x** (Georgia Tech 2024)
- Adding statistics to passages increases citation by **40%** (Princeton GEO study 2024)
- Adding quotations from authorities increases citation by up to **115%** in certain categories (IIT Delhi 2024)
- Fluency optimization increases visibility by **30%** on average across query types
- Content with source citations is cited **20-25% more often** by Perplexity and ChatGPT Search

## Platform-specific citation preferences

| Platform | Preference |
|---|---|
| ChatGPT (Search) | Explicit definitions, named sources, recent dates. Typically cites 2-4 sources per response. |
| Perplexity | Heavily favors fact-dense passages with statistics. Cites 4-8 sources per response. Values recency. |
| Claude | Well-structured, comprehensive passages. Values nuance and accuracy over brevity. |
| Gemini / AI Overviews | Concise answer blocks (40-60 words). Favors content already in top 10 organic. |
| Copilot (Bing) | Similar to Gemini. High-authority domains with clear factual claims. |
