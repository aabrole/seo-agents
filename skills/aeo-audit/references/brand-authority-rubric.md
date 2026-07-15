# Brand Authority Rubric (Third-Party AI Citation Signals)

> Adapted from geo-seo-claude `geo-brand-mentions` skill. Research: Ahrefs December 2025 analysis of 75,000 brands, Profound (2025), Terakeet (2025).

## Core insight

Brand mentions correlate **~3x more strongly** with AI visibility than traditional backlinks. **Unlinked brand mentions** — references to a brand name without a hyperlink — are a stronger predictor of AI citation than Domain Rating or backlink count.

**The platform where the mention appears matters enormously.** Not all mentions are equal. A mention on YouTube or Reddit can carry more weight for AI citation than a dofollow backlink from a DR 70 blog.

This inverts traditional SEO logic and is the single most counter-intuitive finding in the AEO research.

## Scoring formula

```
Brand_Authority_Score = (YouTube  * 0.30)
                      + (Reddit   * 0.25)
                      + (Wikipedia * 0.20)
                      + (LinkedIn  * 0.15)
                      + (Other    * 0.10)
```

---

## 1. YouTube (30%) — STRONGEST signal (correlation ~0.737)

**Why YouTube matters most:**
- Second-largest search engine globally (2.5B+ monthly users)
- AI training datasets heavily incorporate YouTube transcripts, descriptions, metadata
- Google Gemini and AI Overviews directly reference YouTube content
- Perplexity and ChatGPT index and cite YouTube videos
- Transcripts are high-value because they contain natural-language mentions in conversational context

**What to check:**
- Brand YouTube channel: exists? Active? Subscriber count? Upload frequency?
- Third-party video mentions: how many? In reviews, tutorials, or comparisons?
- Video descriptions: brand name in descriptions of industry-relevant content?
- Video transcripts: brand mentioned in spoken content of relevant videos?
- YouTube search presence: does "[brand name]" return results on YouTube?
- Comment mentions: brand discussed in comments on relevant industry videos?

**Scoring:**

| Score | Criteria |
|---|---|
| 90-100 | Active channel with 10K+ subs, regular uploads, mentioned in 20+ third-party videos, strong YouTube search presence |
| 70-89 | Active channel with 1K+ subs, 10-19 third-party mentions, some YouTube search presence |
| 50-69 | Channel exists with content, 5-9 third-party video mentions |
| 30-49 | Inactive channel, 1-4 third-party mentions |
| 10-29 | No channel or empty, 1-2 mentions only |
| 0-9 | No YouTube presence |

---

## 2. Reddit (25%) — High correlation

**Why Reddit matters:**
- Heavily indexed in AI training data (Google's $60M/year Reddit licensing deal, 2024)
- AI systems weight Reddit for product recommendations, comparisons, user sentiment
- "Reddit" is appended to an estimated 10-15% of Google searches seeking authentic opinions
- Perplexity frequently cites Reddit threads
- ChatGPT and Claude reference Reddit for product/service questions

**What to check:**
- Subreddit presence: mentioned in which relevant subreddits?
- Mention volume: how many threads? Trend (increasing/decreasing)?
- Sentiment: positive/negative/neutral? Common praise/complaints?
- Official presence: does the brand have a Reddit account? AMAs?
- Recommendation threads: does the brand appear in "What do you recommend for X?" threads?
- Brand subreddit: owned? How active?

**Scoring:**

| Score | Criteria |
|---|---|
| 90-100 | Frequently recommended in relevant subreddits, predominantly positive, active official presence, own subreddit 5K+ members |
| 70-89 | Regularly mentioned, mostly positive, appears in multiple recommendation threads |
| 50-69 | Mentioned in several threads, mixed sentiment, community recognizes the name |
| 30-49 | Occasional mentions in 1-2 subreddits, no official presence |
| 10-29 | Rare mentions, largely unknown on Reddit |
| 0-9 | No Reddit presence |

---

## 3. Wikipedia (20%) — High correlation

**Why Wikipedia matters:**
- One of the highest-authority sources in AI training data; all major AI models trained on Wikipedia
- AI systems use Wikipedia for entity recognition — determining whether a brand is a "real" entity
- Wikidata (Wikipedia's structured sibling) provides machine-readable facts for knowledge graphs
- Having a Wikipedia page is a strong notability signal

**What to check:**
- Brand Wikipedia page: exists? Quality (stub, start, B-class, higher)?
- Founder/CEO Wikipedia page?
- Brand website cited as reference in other Wikipedia articles?
- Wikidata entry (Q-number) with complete properties?
- Brand mentioned in other Wikipedia articles (industry, competitor, category pages)?

**Scoring:**

| Score | Criteria |
|---|---|
| 90-100 | Detailed article (B-class+), Wikidata entry complete, brand cited as reference in multiple articles, founder has Wikipedia page |
| 70-89 | Article exists (start-class+), Wikidata entry, mentioned in 2+ other articles |
| 50-69 | Stub/start article, basic Wikidata, limited mentions |
| 30-49 | No article but mentioned in other articles or cited as reference |
| 10-29 | Mentioned in 1-2 articles as passing reference |
| 0-9 | No Wikipedia/Wikidata presence |

---

## 4. LinkedIn (15%) — Moderate correlation

**Why LinkedIn matters:**
- Increasingly indexed by AI systems for professional/B2B context
- Company pages and employee thought leadership build entity signals
- AI references LinkedIn for company info, team credentials, professional authority

**What to check:**
- Company page: exists? Follower count? Post frequency?
- Leadership thought leadership: are execs posting?
- Third-party mentions: non-employees discussing the brand?
- LinkedIn long-form articles about or mentioning the brand?
- Employee profiles: detailed, complete, linking to company?
- Typical post engagement (likes, comments, shares)?

**Scoring:**

| Score | Criteria |
|---|---|
| 90-100 | Active page 10K+ followers, regular leadership thought leadership, frequent third-party mentions |
| 70-89 | Active page 5K+ followers, some employee thought leadership, occasional third-party mentions |
| 50-69 | Page with 1K+ followers, irregular posting, limited third-party mentions |
| 30-49 | Sparse/inactive page, few followers |
| 10-29 | Basic page with minimal info |
| 0-9 | No LinkedIn presence |

---

## 5. Other Platforms (10%) — Supplementary

Lower individual correlation but meaningful in aggregate:

- **Stack Overflow / GitHub** (for dev tools): mentioned in answers, stars on repos
- **Quora**: brand name appearing in relevant answers
- **Medium / Substack**: thought leadership or third-party coverage
- **Podcast appearances**: founder/exec interviewed; transcripts indexed
- **Product Hunt**: launch results, ongoing discussion
- **Industry publications**: TechCrunch, The Verge, category-specific trade pubs
- **G2 / Capterra / Trustpilot** (for SaaS/services): review volume and sentiment

Score 10% weight proportionally based on relevance to business type.

---

## Critical adjacent signals

These affect the Brand Authority score indirectly but should be flagged:

- **Brand name ambiguity**: does the brand share a name with another entity? High ambiguity = AI systems cannot resolve the entity reliably. Recommend long-form brand disambiguation content.
- **Entity consistency**: is the brand name spelled consistently across all third-party mentions? Inconsistency fragments the entity graph.
- **Founder entity**: is the founder a recognized entity? A founder with strong personal brand pulls the company brand up.
- **Category co-occurrence**: does the brand name reliably appear alongside the category name in corpus-level searches? This is what AI systems learn as "brand X is a [category]".
