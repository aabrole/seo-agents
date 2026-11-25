---
name: review-amplification
description: Use when a brand has genuine customer reviews and wants to turn them into content that shows up for consideration-stage branded searches such as "[brand] review", "is [brand] legit", or "is [brand] worth it". Produces per-platform post drafts, an on-site review page plan, and a before/after monitoring log. Also use when the user mentions "reputation search", "[brand] reviews", "is it a scam", "testimonial posts", "review schema", or "what AI says about our brand".
user-invocable: true
argument-hint: "<brand> [review source or pasted reviews] [platforms]"
license: MIT
metadata:
  author: aabrole
  version: "1.0.0"
  category: seo
---

# Review Amplification

Turns real customer reviews, with permission, into posts and pages that answer the questions people ask while deciding whether to trust a brand. One review is reused across platforms with different opening lines, so it can match several queries.

Why this works: after someone hears about a brand, they often search a branded query with a trust word: "[brand] review", "[brand] reviews", "is [brand] legit", "is [brand] a scam", "is [brand] worth it", "[brand] rating". These are consideration-stage searches. Social posts, review sites, and the brand's own pages often fill those results, and AI answers draw on the same sources. If the only content is thin or negative, buyers see that. Genuine positive reviews, published where search engines and AI tools look, help buyers see the real picture.

## Input

- **Brand** (required): name, site, product, any known alternate spellings
- **Reviews** (required): real reviews with source, date, reviewer name or handle, and written permission to reuse. Pasted text, a review platform export, or a feedback folder
- **Platforms** (optional): company page presence on LinkedIn, Facebook, X, Instagram, YouTube community, Threads, etc.
- **Negative or mixed reviews** (optional): so the plan does not hide them

## Role

You are a reputation content editor. You select and quote real reviews exactly, write platform-appropriate posts around them, and set up monitoring. You do not write or invent reviews.

## Step 1: Verify Reviews and Permissions

For each review, record: source (where originally posted), date, reviewer, exact text, rating, permission status.

A review qualifies only when:

1. It is genuine and from a real customer or user of the product.
2. The reviewer has given permission for the quote and, if relevant, the name or photo. If the review was posted publicly on a platform, still follow that platform's terms for reposting and consider asking.
3. It was not written, edited, or selectively rewritten by the brand. Light formatting (trimming obvious typos with the reviewer's agreement, or excerpting with an ellipsis that does not change meaning) is the limit, and an excerpt must be marked as one.
4. Any incentive is recorded. If the reviewer received a discount, free product, payment, or an affiliate relationship, the post must disclose it clearly. Reviews that were incentivized on the condition of positive content are excluded entirely.
5. The reviewer has a relevant relationship to the brand that is disclosed (employee, investor, partner, family).

Mark unknowns `[CLIENT TO CONFIRM]` and do not draft posts for those reviews until resolved.

## Step 2: Check What Searchers See Now

Before publishing, record a baseline for each consideration query:

- "[brand] review", "[brand] reviews", "[brand] rating", "[brand] testimonials"
- "is [brand] legit", "is [brand] real", "is [brand] a scam", "is [brand] worth it", "[brand] complaints", "[brand] vs [competitor]"

For each, note the top results (owned, review platform, forum, social, news), the sentiment of each, any SERP features (review snippets, People Also Ask, video), and what AI assistants answer when asked the same question (see Step 7). Use the Ahrefs MCP SERP overview, a manual search in a private window, or `scripts/fetch_page.py` for specific result pages.

If a negative result such as a fair complaint thread ranks, the answer is to fix the underlying issue and respond honestly, not to bury it with fake content. Flag it to the client.

## Step 3: Pick the Reviews and Map Them to Queries

Choose reviews that are specific (they name the product, the problem, and an outcome), recent, and credible. Avoid generic praise with no detail.

For each chosen review, assign one opening phrase per platform from this bank, chosen to fit the review's content:

- "[Brand] review: ..." / "[Brand] reviews: ..."
- "Is [brand] legit? ..." (works when the review mentions delivery, trust, or results)
- "Is [brand] worth it? ..." (works when the review mentions value or price)
- "[Brand] rating: ..." (works when the review includes a score)
- "[Brand] testimonial: ..."
- "Is [brand] a scam? ..." (use only where it reads naturally and the reviewer speaks to trust; avoid it if it would feel manipulative or off-brand, and check platform rules)

The opening line carries the query phrase and answers it honestly, followed by the real quote.

## Step 4: Draft Posts Per Platform

For each review, write one draft per platform, each starting with a different phrase from Step 3. Include the verbatim quote in quotation marks, attribution as the reviewer permitted, a one-sentence context line (what they used the product for), and a link where it makes sense. Typical shapes:

- **LinkedIn:** an opener question or "[Brand] review" line, the quote, one line of context, a link. Professional tone.
- **Facebook page:** "[Brand] review!" opener, quote, optional photo with permission, link.
- **X:** short opener plus the quote or an excerpt (marked as an excerpt), link. Use a screenshot only if it is an unaltered capture and the source allows it.
- **Instagram:** quote graphic or Reel; caption opens with the phrase; follow `video-seo` caption rules for Reels.
- **YouTube community post or video:** opener in the title or first line; a short video with the reviewer's consent is stronger than a graphic.
- **Threads, Pinterest, other:** short variants with a different opener.

Rules for the set:

- No two platforms use the same opening phrase for the same review.
- Do not post all variants the same hour; space them over days.
- Include a disclosure line wherever an incentive or relationship exists.
- Do not reply to or tag competitors in a misleading way.
- Do not run the same post through many accounts. Post from official brand accounts and the reviewer's own account only with their consent.

## Step 5: On-Site Review Page and Schema

1. Plan a "Reviews" or "Customer stories" page on the site that lists real reviews, ideally with source links to the originals (third-party platforms where the reviewer posted). Use the brand name plus "reviews" in the title and H1 naturally.
2. Include rating context honestly: number of reviews, source, date range. Do not display ratings you cannot support. Include mixed reviews where they are real; a page with only perfect scores reads as curated.
3. Hand off to `schema-markup` for structured data. Note the limit: Google does not show review rich results (star snippets) for a business's own reviews of itself marked up on its own pages, a self-serving review markup case, so do not promise stars in search. Review markup is better used on third-party review content, product pages with legitimate aggregate ratings from genuine users, and where Google's current guidelines allow. Check current Google documentation before implementing.
4. Link the review page from the footer or an "about" or "trust" hub, and from landing pages near the call to action (see `bofu-hub-pages`).

## Step 6: Respond Honestly to Negative Reviews

- Reply publicly and promptly, acknowledge the issue, and offer a way to fix it.
- Never ask for removal of legitimate negative reviews or offer rewards for changing them.
- Report reviews that violate a platform's rules through its official process.
- Share patterns with the client so the product or service gets fixed.

## Step 7: Monitor Before and After

At baseline, then at 2, 4, and 8 weeks:

- Re-check each consideration query: which results appear, their sentiment, and whether new owned or social posts are visible.
- Ask the major AI assistants the same questions ("Is [brand] legit?", "What do people say about [brand]?") and record the answer and cited sources. Hand off to `aeo-audit` for a structured test and `geo-brand-mentions` for mention tracking. Ahrefs Brand Radar can supply mention and citation data if available.
- Record GSC impressions for branded queries and branded click-through.
- Log what changed and when, in the same style as the `publish-and-track` change log.

Results can take weeks, and AI answers change without notice. Treat movement as a signal, not proof.

## Step 8: Optional Press Release Tie-In

If the client already plans a press release (for example for a milestone), a real customer outcome or rating can be part of the announcement. Draft the headline and body so the brand name and the claim are plain, and only cite figures that can be sourced. The human decides whether to pay for distribution and submits it; the skill does not buy or send. Wire services mostly produce nofollow links and syndication copies, which can still appear in branded searches and AI answers, so treat it as a supporting asset only. Hand off to `authority-campaign`.

## Guardrails

- Only genuine reviews from real customers, with permission. No fabricated, composite, or AI-written reviews, quotes, ratings, or customer names.
- No edited quotes beyond marked excerpts; no changing sentiment or ratings.
- Disclose incentives and material connections. Follow FTC Endorsement Guides and Consumer Review rules, which cover disclosure and prohibit fake and suppressed reviews, and any similar rules in the client's market.
- Do not selectively gate reviews (asking only happy customers to review).
- Follow each platform's terms on reposting content, branded content, and review solicitation.
- No fake accounts, sockpuppets, or astroturfing.
- The skill drafts. The human gets permission, posts, and approves.

## Output

1. **Review register:** ID, source, date, reviewer, quote, rating, permission, incentive/disclosure, status.
2. **Baseline table:**

| Query | Top results (type, sentiment) | SERP features | AI answer summary | Notes |
|---|---|---|---|---|

3. **Post drafts:** per review, per platform: opening phrase, full text, disclosure, link, suggested date.
4. **On-site plan:** page outline and schema hand-off notes.
5. **Monitoring log:** dates and observed changes.

## Next Step

- Schema implementation: `schema-markup`
- AI answer tests: `aeo-audit`, `geo-brand-mentions`
- Press and expert coverage to supplement reviews: `authority-campaign`
- Video reviews: `video-seo`
- Overall sequencing: `bofu-playbook`
