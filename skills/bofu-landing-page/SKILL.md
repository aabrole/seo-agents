---
name: bofu-landing-page
description: Use when you need a spec and draft copy for one bottom-of-funnel landing page that targets one buying-intent keyword (or a small merged keyword group). Covers title, meta, H1, layout, images, compact copy, multi-product and "[competitor] alternative" variants, and QA. Also use when the user mentions "BOFU landing page", "write a landing page for this keyword", "alternative page", "page spec", "title tag formula", or "compact page".
user-invocable: true
argument-hint: "<primary keyword> [secondary keywords] [brand/site] [variant: single|multi|alternative]"
license: MIT
metadata:
  author: aabrole
  version: "1.0.0"
  category: seo
---

# BOFU Landing Page

Produces a page spec and full draft copy for one bottom-of-funnel landing page. The page targets a searcher who already knows what they want and is choosing a provider, so it stays short, literal about the keyword, and built around one action.

Why this works: a buyer-intent query is answered best by a page that confirms in seconds that it matches the query, shows the real thing being sold, and offers the next step. Long pages dilute that. Compact pages with specific, original copy rank because they match the query closely and keep visitors from bouncing back to the results page.

## Input

- **Primary keyword** (required), plus up to 2 close variants. Start with one keyword per page; merge variants only when the SERP shows the same page type ranking for all of them.
- **Brand and site context**: brand name, product or service facts, pricing facts, allowed claims, existing CTA and its destination.
- **Variant** (optional): `single` (default), `multi` (several products or plans), `alternative` (a "[competitor] alternative" keyword).
- **Keyword research output** (optional): the SERP notes from `bofu-keyword-research`. If absent, look at the top 5 results yourself (Step 2).
- **Assets** (optional): screenshots, photos, testimonials, logos, FAQ source material.

## Role

You are a conversion-minded SEO copywriter. You write short, specific, factual pages. You do not invent facts: anything you cannot source from the client's materials gets a marker.

## Step 1: Pre-write intent notes

Spend a few minutes writing three short answers before any copy. Keep them in the deliverable.

1. **Who searches this?** Role, company size or life situation, and what they probably already tried.
2. **What do they want?** The concrete thing: a feature, a price, a service area, a file format, a fast quote.
3. **What outcome are they after?** The result they want after buying, in their words, not marketing language.

Use these answers to pick the H1 angle, the order of sections, the image, and the CTA wording. If you cannot answer one of them from the client's materials, ask or mark it `[CLIENT TO CONFIRM]`.

## Step 2: Read the SERP for this keyword

Open the top 5 results (Ahrefs SERP overview, DataForSEO SERP, or manual search). Record in a small table: page type (product page, landing page, listicle, directory), whether the exact keyword is in the title, slug and H1, and what each page offers above the fold. Use this to decide:

- Which title angle is still unused (Step 3).
- Whether the variant should be `alternative` (results are comparison pages) or `single`.
- What the consensus facts are, so your copy does not contradict what every result says without a reason.

Fallback without tools: search manually in a private window and note the same fields by hand.

## Step 3: Write the page title

Formula: `Target keyword | differentiating benefit or searcher goal | Brand`

Rules:

- The keyword comes first, written close to how the searcher types it.
- The middle part names a benefit or the goal the searcher has. Add it especially when the competing titles all carry the same keyword and nothing else.
- The brand goes last. If it gets cut off, that is acceptable.
- Check truncation in a SERP preview tool (or count: roughly 55-60 characters on desktop, fewer pixels on mobile). The keyword and most of the benefit must survive the cut.
- Write the title as if it will be shown unchanged. Search engines often rewrite titles, so do not depend on the exact string.

Fresh examples (fictional brands):

| Keyword | Title |
|---|---|
| invoice software for freelancers | Invoice Software for Freelancers \| Get Paid Faster \| TallyLeaf |
| emergency plumber leeds | Emergency Plumber Leeds \| 60-Minute Callout \| BlueCopper Plumbing |
| standing desk for tall people | Standing Desk for Tall People \| Up to 53 Inches High \| RiseForm |
| translate legal documents online | Translate Legal Documents Online \| Certified Option \| LexaVerse |

Generate 3 candidates, pick one, and list the others in the spec. Keep the claim in the middle part true: "60-Minute Callout" or "Up to 53 Inches High" must come from the client's facts, otherwise mark `[CLIENT TO CONFIRM]`.

## Step 4: Place the keyword

Place the exact or close keyword in these spots and nowhere else on purpose:

| Spot | Rule |
|---|---|
| URL slug | Exact keyword, lowercase, hyphens, no stop-word tricks. Sits under the right hub folder (see `bofu-hub-pages`). |
| Title | At the start (Step 3). |
| Meta description | Keyword near the start, then the benefit and a hint of the action. About 120-158 characters. |
| H1 | The keyword, or a natural reading of it. |
| First sentence | Keyword within the first few words. |
| First image alt | Describes the image and carries the keyword if it reads naturally. |

Do not bold, repeat or stuff beyond this. Further mentions are allowed only where a human writer would say it again.

### Fragment keywords

Many buying keywords are fragments, not sentences. Keep the fragment in the slug if you want, and write readable copy everywhere else.

| Fragment keyword | Slug | H1 and title phrasing | First sentence |
|---|---|---|---|
| kids bike helmet size 5 year old | /products/kids-bike-helmet-size-5-year-old | Bike Helmets for 5-Year-Olds, Sized Right | Choosing a kids bike helmet for a 5 year old comes down to head circumference, not age. |
| roof repair after hail denver | /services/roof-repair-after-hail-denver | Hail Roof Repair in Denver | Roof repair after hail in Denver starts with a free inspection and a written damage report. |
| csv to qbo converter bank | /uses/csv-to-qbo-converter-bank | Convert Bank CSV Files to QBO | A CSV to QBO converter for bank statements turns a spreadsheet export into a file your accounting software can import. |

Method: keep the words and their order where possible, add the small connecting words a person would say, and make the first sentence complete. Accept a slightly lower grader score before accepting stilted copy.

## Step 5: Build the standard layout

Single product or service page, top to bottom:

1. **H1** (keyword).
2. **Short intro**, 2-3 sentences, keyword in the first sentence, outcome for the searcher in the second.
3. **Primary CTA button** (specific text: "Get a quote", "Start free", "Book an inspection"). Same destination everywhere on the page.
4. **Real product or service image** above the fold, matched to the keyword (Step 7).
5. **Alternating sections**: H2, 2-4 short sentences or 3-5 bullets, image on alternating sides, optional text-only section, light dividers.
6. **Reusable trust sections** lower on the page: customer logos, FAQ, testimonials, certifications. These can be templated blocks shared across pages, because they are not what makes the page match the query.
7. **Same CTA again** at the end, with one line of context.

Placement rule: put most of the keyword-specific unique copy and images in the top half. Visitors who land and see generic reused blocks first tend to leave. Reused sections go below the unique material.

Mobile order: H1, intro, CTA, then the hero image. In later sections the image follows its text. Check that the CTA is visible without scrolling on a 375px-wide screen.

## Step 6: Length and voice

- Target 350-550 words of unique copy including headings. Shorter pages can rank if the copy is specific. Reused template blocks do not count toward this target but also should not bury the unique copy.
- Short paragraphs (1-3 sentences), bullets for features and steps.
- Neutral, factual tone. State what the product does, who it fits, what it costs or how pricing works, and what happens next. No superlatives ("best", "leading", "revolutionary"), no hype, no vague promises.
- Every claim is either a fact from the client's materials or carries `[NEEDS SOURCE]`.

**Scope note:** for BOFU landing pages this overrides the 800-word service-page floor in `seo-content`. That floor suits broad service or informational pages that must cover a topic. A BOFU page answers one decision, and a visitor who is ready to act is better served by 450 specific words than 900 padded ones. Keep the 800-word guidance for non-BOFU service pages and for informational content, where depth and answer-first coverage still matter (see `striking-distance` for refreshing those).

AI drafting: allowed for structure and first drafts from the client's own product documentation, but the final copy needs a human editor who knows the product. Unreviewed generic AI landing pages are a risk for both quality and trust. Run the copy-watermark-hygiene pass at the end (Step 10).

## Step 7: Images

Use real images that match the keyword. Stock photography is the last resort.

Acceptable types: product photos, app or dashboard screenshots, packaging, the service being delivered, the team on site or in uniform, the office or workshop, before and after shots, an actual deliverable (a sample report, a finished job), a diagram of how the product works that you built yourself.

Rules:

- Hero image is unique to the page and clearly shows what the keyword describes.
- File names: `<hub>_<slug>_<descriptor>.webp`, for example `uses_invoice-software-for-freelancers_dashboard-overview.webp`.
- Alt text: the first image describes the image and carries the keyword when natural. Later images get plain descriptions of what they show, without repeating the keyword.
- A reused image gets a new file name and page-specific alt text, unless it sits in a shared block.
- Compress and convert to WebP, set width and height, and do not lazy-load the hero image.
- Do not put critical text (prices, comparison tables) inside images.

If no real images exist, list them in the spec as "images needed" with a one-line shot brief each, and do not fill the gap with irrelevant stock.

## Step 8: Variants

### Multi-product layout

Use when the keyword covers several products or plans (for example a category term).

- H1 and intro as in the standard layout, then the CTA.
- A short product block for each item: image, one-line description, 2-3 bullets of differences, a link or CTA per item.
- A "how to choose" section of 3-5 bullets tied to the searcher's situation.
- Keep unique copy per product to about 60-100 words so the total stays near the target. Each product that deserves its own keyword gets its own page and is linked from here.

### Alternatives and comparison page ("[competitor] alternative")

Use the standard layout, plus:

1. An **H2 comparison section directly below the fold**, naming the comparison, for example "TallyLeaf vs ClearBooks: Features, Pricing, and Limits".
2. An **HTML text table** right under that H2. It must be real HTML, not an image or a screenshot, so searchers and language models can read it.
3. Table columns: feature or criterion, your product, the competitor. 6-10 rows chosen from what searchers compare (price, free plan, key features, limits, support, integrations).
4. Every cell is accurate, current, and sourced from the competitor's public pricing or documentation page. Add the retrieval date under the table. Mark any unverified cell `[NEEDS SOURCE]`. Do not write disparaging claims; state differences neutrally and include rows where the competitor is stronger if that is true.
5. A short "who each option fits" section after the table.

For deep competitor research, feature matrices across several rivals, and "X vs Y" pages, hand off to `competitor-alternatives`.

## Step 9: Anti-patterns

- **Keyword-swap clones.** Pages that are identical apart from a swapped keyword or city are doorway-page risk. Each page must reflect its own use case, audience or location: different pain points, examples, constraints, images, FAQs, and local facts (real service areas, regulations, climate, typical job types). If you cannot write a meaningfully different page, merge the keywords into one page.
- Generic stock hero images.
- Hype and superlatives.
- Unique copy buried under reused blocks.
- Several CTAs pointing to different goals.
- A title that repeats the keyword twice.
- Fabricated testimonials, ratings, client logos, awards or numbers. Never write these. Use only real ones the client supplies, and mark the rest `[NEEDS SOURCE]`.

## Step 10: QA

Run this checklist on the draft and again on the built page.

1. **Keyword presence** in the six spots from Step 4, without stuffing.
2. **Grader check.** If an on-page grader is available (Moz On-Page Grader or similar), run it against the live URL. Aim for a high score but not a perfect one: a score in the high 90s is the target. If it is 100, look for over-repetition (the keyword in every alt, bolded repeats, the same phrase in every heading) and de-optimize one or two spots. Most graders only re-check a URL once per day, so batch your fixes.
3. **Spellcheck** the whole page, including the title, meta and alt text.
4. **Title and description preview** in a SERP simulator, desktop and mobile.
5. **Social preview.** Check Open Graph tags (og:title, og:description, og:image) with a sharing debugger. The og:image should be the hero image at the right size.
6. **Structure check.** One H1, no skipped heading levels, CTA reachable above the fold on mobile, internal link from the hub (see `bofu-hub-pages`). `scripts/parse_html.py` extracts title, meta, headings, alt text and links from a saved page for this check.
7. **Fact check.** Every number, price, claim and comparison cell traces to a source or carries a marker.
8. **Copy-watermark-hygiene pass** (`copy-watermark-hygiene`) on all produced copy.
9. **Schema hand-off.** Pass the finished page to `schema-markup` for Organization, Product or Service, FAQPage (only if the FAQ is visible on the page; it no longer earns a rich result, so add it for clarity, not for SERP features), and BreadcrumbList. Do not add schema for content that is not on the page.

## Guardrails

- Never fabricate reviews, testimonials, quotes, statistics, credentials or press mentions. Unknowns get `[NEEDS SOURCE]` or `[CLIENT TO CONFIRM]`.
- Competitor facts come from public, current, citable pages.
- The skill drafts only. Publishing, requesting indexing and any outreach are the human's decision.
- Keep claims inside what the client can substantiate, and respect any industry rules on health, finance or legal wording.

## Output

Deliver three parts in this order.

**1. Page spec**

| Field | Value |
|---|---|
| URL | /hub/keyword-slug |
| Title (with char count) | ... |
| Meta description (with char count) | ... |
| H1 | ... |
| H2s | list |
| Primary keyword | ... |
| Secondary keywords (max 2) | ... |
| Variant | single / multi / alternative |
| CTA text and destination | ... |
| Images needed | file name, shot brief, alt text |
| Hub and internal links | hub page, related pages |
| Alternate title options | 2 more |

**2. Intent notes and draft copy.** The three answers from Step 1, then the full copy in page order with headings, CTA placements and image slots. Include a word count of unique copy. Mark `[NEEDS SOURCE]` and `[CLIENT TO CONFIRM]` inline. For the alternative variant include the HTML comparison table and the source line for each competitor cell.

**3. QA checklist.** The Step 10 list with pass, fix or open for each item.

See `references/page-spec-template.md` for a fill-in template and a worked example.

## Next Step

- Need the keyword and SERP work first: `bofu-keyword-research`.
- Deep competitor research or X-vs-Y pages: `competitor-alternatives`.
- Link the page from a hub and check click depth: `bofu-hub-pages`.
- Structured data: `schema-markup`.
- Publishing, indexing and tracking: `publish-and-track`.
- Copy cleanup before delivery: `copy-watermark-hygiene`.
