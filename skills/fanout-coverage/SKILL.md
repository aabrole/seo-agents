---
name: fanout-coverage
description: Use when a client needs to be retrievable across the sub-questions an AI answer engine generates from one head query, not just rank for the head query itself. Observes the real fan-out from AI Mode, Perplexity, and ChatGPT, gaps it against the site, kills duplicate-intent pages, rewrites top pages for passage independence, and sets a citation baseline. Also use when the user mentions "query fan-out," "fan-out," "sub-queries," "AI Mode coverage," "facet coverage," "why aren't we cited," "impressions up but clicks flat," "keyword variant pages," "duplicate intent," "passage independence," "chunk-level retrieval," or "AI search visibility baseline."
---

# Fan-Out Coverage

One user query becomes many machine sub-queries before an AI answer is written. Each sub-query runs its own retrieval and fills its own slot. This skill makes a site retrievable across that whole branch set instead of competing for a single head-term position.

Why this works: fan-out generation rewards *semantic breadth* and penalizes redundancy. Google's published research on the approach optimizes three competing rewards, groundedness (every sub-query must map to something real and retrievable), diversity (measured so the model explores distinct aspects rather than synonym restatements), and alignment (no drift from the original prompt). The practical consequence is blunt: twelve pages targeting synonyms of one keyword collapse into one branch, while twelve pages covering distinct facets of the same topic are twelve separate shots at a citation slot. Cheap fan-out also means more branches per query, so a site that cannot win the head term can still own several narrow branches under it.

Scope honesty: the underlying research was validated on abstract retrieval over item databases, not open-web document search. Treat the mechanism as directionally real and the specifics as unconfirmed. Do not sell this as a Google update, and do not use it to diagnose a traffic drop.

## Input

- **Site** (required) plus the **head topic** to work (one money topic per run, not the whole site)
- **Access** (optional but better): GSC property via MCP, Ahrefs Brand Radar, a crawl or sitemap
- **Depth** (optional): `standard` (default, one topic) or `cluster` (the topic plus its sibling topics)

## Role

You are a senior SEO working retrieval coverage, not rankings. You add pages only when a facet has no home, you consolidate aggressively, and you never rewrite a page that is already winning.

## Step 1: Observe the Fan-Out

Do not theorize the sub-queries. Collect them.

Run the head query through at least three surfaces: Google AI Mode, Perplexity, and ChatGPT search. For each answer, write down every **distinct sub-question the answer actually resolves**, in the answer's own framing. Also capture the cited URL per sub-question, since that tells you who currently owns each branch.

Three passes minimum per surface, because fan-out is non-deterministic. A sub-question appearing on two or more surfaces is a **stable branch** and gets priority. One appearing once is a **volatile branch**, note it and move on.

Supplement, do not substitute, with: People Also Ask, the related-searches rail, and Ahrefs `brand-radar-ai-responses` if available.

Target 15 to 30 distinct sub-questions for a commercial head topic. Fewer than 10 usually means the head query was too narrow to fan out, pick a broader one.

Then classify each sub-question by facet type so you can see the shape of the gap rather than a flat list. Facet taxonomy in `references/facet-taxonomy.md`.

## Step 2: Gap It Against the Site

Build the coverage map. One row per observed sub-question:

| Sub-question | Facet | Stable/Volatile | Covering URL | Verdict | Current citee |
|---|---|---|---|---|---|

Verdicts:

- **Owned**: a page answers it directly, in a retrievable block, under a matching heading.
- **Buried**: the site has the answer but it is spread across sections or sits under an unrelated heading. Cheapest possible win, fix in place.
- **Orphan**: the answer exists on a page whose main intent is something else, so the page will never be retrieved for this branch. Decide: promote to its own page, or restructure into a proper block.
- **Missing**: no answer anywhere. Needs a page or a block.

Rank the work by Missing and Buried on **stable** branches first. Volatile branches are cheap to serve once the stable ones are covered, never lead with them.

## Step 3: Duplicate-Intent Audit

This is the step that frees up the budget for Step 2.

Cluster existing pages by **intent, not keyword**. Two pages share intent when a reader arriving at either wants the same outcome, regardless of the phrasing in the title. Synonym variants, near-identical "best X" and "top X" pages, and thin location or modifier spins are the usual offenders.

For each cluster with more than one page:

- **Keep** the page with the strongest existing signals (links, rankings, conversions)
- **Merge** the unique substance from the others into the keeper, as new blocks
- **301** the merged pages to the keeper
- **Kill** anything with no unique substance, no links, and no traffic

Do not merge pages that look similar but serve genuinely different facets. "CRM pricing" and "CRM pricing for nonprofits" are two branches, not one. The test is whether the *answer* differs, not whether the *keyword* differs.

Flag cannibalization to the owner before executing redirects. Never batch-redirect without sign-off.

## Step 4: Passage Independence Pass

Fan-out retrieval pulls passages, not pages. A passage that only makes sense in the context of the page above it will be skipped or, worse, retrieved and misread.

Take the top 10 pages by business value (or by the coverage map, whichever is more urgent) and fix:

1. **Pronoun and back-reference cleanup.** Restate the entity by name in each section. Ban "it," "this approach," "as mentioned above," "the platform" used as a standalone subject. A reader dropped into the section cold should know what the section is about from its first sentence.
2. **Question-shaped headings.** Rewrite H2s and H3s as the sub-query someone would actually issue, matched as literally as the observed fan-out allows. Headings are the strongest retrieval anchor on the page.
3. **Answer first, under the heading.** One or two sentences of direct answer immediately below the heading, then support. No throat-clearing, no "in this section."
4. **Claim and evidence in the same block.** A chunk retrieved without its proof does not get cited. If the stat lives three sections away, duplicate it into the block.
5. **Attribute density.** Replace vague prose with extractable specifics: prices, dates, numbers, eligibility rules, locations, version numbers. Groundedness binds sub-queries to things that concretely exist, so concrete beats eloquent every time.

Apply the anti-slop rules from `improve-content` if available. Strip watermark artifacts from any produced prose before delivery.

## Step 5: Set the Measurement Baseline

Do this **before** the fixes ship, or the work is unmeasurable.

- **Citation baseline**: record, per stable branch, who is currently cited across the three surfaces. Re-run monthly. Movement here is the primary KPI, and it moves before traffic does.
- **Ahrefs Brand Radar** if the client has it: `brand-radar-mentions-overview` and `brand-radar-cited-pages` snapshot.
- **GSC pattern to watch**: impressions climbing while clicks stay flat. That is fan-out pulling the site into answers without the click, and it is a **leading indicator of coverage working**, not a failure. Snapshot impressions, clicks, and CTR per target URL now so the pattern is legible later.
- **Re-run cadence**: fan-out coverage re-check monthly, full re-observation quarterly or after any major AI Mode change.

## Guardrails

- **One topic per run.** Coverage maps for a whole site are unusable and stale on arrival.
- **Do not fabricate the fan-out.** If you did not observe a sub-question in a live answer, it is a hypothesis, label it as one.
- **Do not create a page per sub-question.** Most branches belong as blocks on an existing page. New pages only for distinct intent with commercial value.
- **Never touch a page ranking 1 to 3 for its primary query** beyond additive blocks. It is load-bearing.
- **No traffic-drop diagnosis.** Nothing here explains a ranking loss. If the client's traffic fell, that is a different investigation.
- **Redirects need explicit owner approval.** Present the merge plan, do not execute it unilaterally.

## Output

### Coverage Map
The Step 2 table, sorted by verdict severity, stable branches first.

### Consolidation Plan
Intent clusters, keeper URL per cluster, merge-and-redirect list, kill list. Each row carries the signal evidence that justified the keeper.

### Page Work Queue
Per page: the blocks to add (heading, direct answer, evidence, placement note), and the passage-independence fixes to make. Ready to paste, not described.

### New Page Briefs
For Missing branches that justify their own page, a one-line intent statement and target sub-questions each, handed off to `content-brief`.

### Baseline Snapshot
Citation ownership per stable branch, Brand Radar numbers if available, GSC impressions/clicks/CTR per target URL, dated, with the re-check date.

Close with the three highest-leverage actions and what you expect to move first (citation ownership on Buried branches, typically within one to two crawl cycles).

## Next Step

- Missing branch needs a full page? → `content-brief`
- Page ranks 9-30 and needs answer blocks? → `striking-distance`
- Whole cluster needs architecture, not patches? → `seo-cluster` or `topic-cluster-planning`
- Want the citability score behind Step 4? → `geo-citability`
- Need the client-facing AI visibility report? → `aeo-audit` or `geo-report`
- Page still will not move after coverage work? → `semantic-gap-analysis`
