---
name: striking-distance
description: Use when you want fast ranking wins from pages already ranking positions 9-30. Pulls GSC data, finds queries each page gets impressions for but never directly answers, and writes self-contained answer blocks to close the gap. Also use when the user mentions "striking distance," "positions 9-30," "GSC quick wins," "page 2 rankings," "low-hanging fruit," "answer gap," "queries I rank for but don't answer," or "update existing pages instead of writing new ones."
---

# Striking Distance

Finds pages Google already trusts but hasn't committed to (positions 9-30), identifies the queries each page earns impressions for without ever directly answering, and produces ready-to-paste answer blocks that close the gap. No new pages, no new links — just finishing what already exists.

Why this works: a page sitting at 9-30 has already passed Google's quality filters for the query. It's being tested. The usual reason it stalls is that the query is answered *implicitly* (or not at all) instead of in a retrievable block. Retrieval doesn't work like ranking — pages get split into chunks/passages, and if the answer is in one chunk and the evidence in another, the model pulls one without the other. Self-contained blocks are the difference between being extracted and being skipped.

## Input

- **Site** (required) — GSC property via MCP/API, or a Performance CSV export (last 90 days)
- **Scope** (optional) — specific pages/directory to focus on, or a max page count (default: top 10 pages by striking-distance impressions)
- **Mode** (optional) — `informational` (default) or `bofu` (bottom-of-funnel variant, see Step 7)

## Role

You are a senior SEO who specializes in content refreshes. You never rewrite pages wholesale — you make contained, surgical additions and leave everything that's working alone.

## Step 1: Pull the Striking-Distance Set

Query GSC for the last 90 days, dimensions `query,page`. Filter to:

- Average position between 8 and 30
- Impressions above a floor (default ≥ 20 over 90 days; lower for small sites)
- Exclude branded queries

Group by page. Rank pages by total striking-distance impressions. These are pages Google is already testing — you're not fighting for entry, only for the answer.

If GSC API/MCP is unavailable, ask for the CSV export (Performance → last 90 days → export) and apply the same filters.

## Step 2: Find the Answer Gaps

This is the step almost nobody does. For each page in scope:

1. Fetch the full rendered page content.
2. For each striking-distance query on that page, check: **does the page directly answer this query anywhere?** Not "mentions the topic" — a reader landing here with exactly that question gets a direct answer within one scroll of a matching heading.
3. Classify each query:
   - **Answered** — direct answer exists under a matching or near-matching heading. Skip.
   - **Buried** — answer exists but is spread across sections, or sits under an unrelated heading. Fix by restructuring into one block.
   - **Missing** — page gets impressions for it but never answers it. Write a new block.

Google is telling you exactly what it thinks the page is about and exactly where it fails to deliver. The Buried + Missing lists are your work queue.

## Step 3: Check Competitor Consensus

For the top 2-3 Buried/Missing queries per page, fetch the top 2-3 currently-ranking competitor pages. Note:

- What their answer says (the consensus you must match to be a credible candidate)
- What they all miss (the uniqueness you can add to win)

You're aiming for **consensus + uniqueness**: agree with the established facts, then add one thing — a number, an example, a first-hand observation — that no competitor has.

## Step 4: Write Self-Contained Answer Blocks

For each Buried/Missing query, write one block:

1. **Heading matching the query as literally as possible** — H2 if standalone, H3/H4 if it fits under an existing section
2. **1-2 sentence direct answer** immediately below the heading
3. **2-3 supporting lines, bullets, or claims** depending on the query type

Rules:

- **Claim and evidence sit in the same block.** A chunk retrieved without its proof is a chunk that doesn't get cited.
- No intro, no padding, no "in this section we'll explore." The block starts with the answer.
- Don't ask for "optimize this page" output — 400 words of air. Every block must survive being extracted alone and still make sense.
- Placement note for each block: which existing section it goes under, or where a new H2 slots in.

Apply the anti-slop rules from `improve-content` if that skill is available — banned vocabulary, varied rhythm, practitioner voice.

## Step 5: Internal Links

Map semantically related pages on the site (use the sitemap plus a crawl if available) and plan links **both ways**:

- Roughly 1 internal link per 50 words of new content, 1 external per 150
- **Anchors carry the entity and the relationship** — "ABA therapy insurance coverage in Washington," never "click here" or "read more." Generic anchors pass link value and zero association.
- Priority sources: pages Google *already surfaces* for the target query (visible in the same GSC data — other pages with impressions for the query). Google has told you which pages it considers relevant; link from exactly those.

## Step 6: Date It

Add or update a **visible** last-updated date in the HTML, not just in schema. Freshness is a live retrieval signal — an unmaintained page loses to a mediocre one updated last week. Only date pages you actually changed.

## Step 7: BOFU Variant (mode: bofu)

Same pipeline, different filter: instead of all striking-distance queries, isolate commercial/bottom-of-funnel queries (pricing, vs, alternatives, "best X for Y", near-me, hire/buy intent). For each uncovered BOFU query:

- Decide **block vs. new page**: if the query fits an existing page's intent, write a block; if it's a distinct purchase intent, flag it for a new page (hand off to `content-brief`)
- Use the pages Google initially surfaced for the query as the internal-link sources into whatever you build

Run this as a recurring (weekly/monthly) check — new striking-distance queries appear constantly as Google tests pages.

## Guardrails

- **Keep changes contained.** Insert blocks; don't let the update touch existing copy that already ranks. Anything at position 1-7 for its query is load-bearing — leave it alone.
- **One page at a time, verifiable diffs.** Never batch-rewrite the whole site in one pass.
- **No cannibalization.** If a Missing query is better answered by a *different* existing page, link to it instead of duplicating the answer.
- **Don't fabricate evidence.** If a block needs a stat or example you don't have, mark it `[NEEDS SOURCE]` for the owner instead of inventing one.

## Output

Per page, in priority order:

### Page: [URL]
**Striking-distance queries:** table of query / position / impressions / status (Answered, Buried, Missing)

**Answer blocks:** the ready-to-paste blocks from Step 4, each with placement note and competitor-consensus note

**Internal links:** from-page → anchor → to-page, both directions

**Date:** where the visible last-updated stamp goes

End with a site-level summary: pages updated, blocks added, links planned, and which queries to watch in GSC over the next 2-4 weeks (position 9-30 → page 1 movement typically shows within a crawl cycle or two).

## Next Step

- Full rewrite needed instead of blocks? → `improve-content`
- Uncovered BOFU query deserves its own page? → `content-brief`
- Block targets a featured snippet? → `featured-snippet-optimizer`
- Want the deeper entity-level gap analysis for a page that still won't move? → `semantic-gap-analysis`

## Credit

Process popularized by Charles Floate (the 9-30 strike zone + self-contained block structure) with the BOFU weekly-routine variant from Luka (@lukagoesindie).
