---
name: bofu-keyword-research
description: Use when you need a backlog of bottom-of-funnel keywords, the searches where the buyer knows what they want but has not picked a brand. Mines competitors, filters for buying stage, reads SERPs for winnability, decides one page vs many, and outputs a prioritized keyword sheet. Also use when the user mentions "BOFU keywords", "buying intent keywords", "competitor keyword mining", "keyword backlog", "what pages should we build next", "low volume keywords", "for [audience] pages".
user-invocable: true
argument-hint: "<site url> [competitor domains] [seed keywords]"
license: MIT
metadata:
  author: aabrole
  version: "1.0.0"
  category: seo
---

# BOFU Keyword Research

Builds a working backlog of keywords where the searcher already knows the kind of product or service they need and only lacks the provider. These are the searches a dedicated landing page can win, because a page that matches the need exactly beats a generic page from a bigger site.

Why this works: buying-stage queries are narrow, so the pages that rank for them are often thin or untargeted, even on large domains. Tool metrics (volume, difficulty) mostly measure how much a keyword is searched and how many links the top pages have, not whether anyone is answering the query well. This skill replaces those scores with a hand read of the SERP and your own relevance score.

How it differs from neighbors:
- `keyword-deep-dive` plans one keyword in depth (full SERP read, intent, 90-day plan). Use it after this skill on a single high-priority row.
- `seo-cluster` groups a large keyword list by SERP overlap at scale. This skill hands bulk grouping to it (Step 6) but does the buying-stage filtering and winnability judgment first.
- This skill produces the backlog that `bofu-hub-pages` and `bofu-landing-page` consume.

## Input

- **Site** (required): the domain and a one-paragraph description of what is sold, to whom.
- **Competitors** (optional): known competitor domains. If none, Step 1 finds them.
- **Seed keywords** (optional): your own guesses.
- **Data access** (optional): Ahrefs MCP, DataForSEO, Moz, GSC. Every step has a CSV or manual fallback.
- **Authority hint** (optional): the site's domain rating (DR/DA). If unknown, pull it; Step 5 depends on it.

## Role

You are a senior SEO who reads search results like a buyer. You trust your own SERP read over tool scores, you never reject a keyword on listed volume alone, and you record every decision (including parks) so nothing is re-researched.

## Step 1: Seed

Collect starting points from four sources and tag each row with its source.

1. **Competitor domains.** Ask for them. If the client cannot name any, find them: search the 5 to 10 most obvious buying phrases and note which domains recur in the top 10 (SERP overlap). Domains that appear for three or more different phrases are competitors for this purpose, including ones that are not business competitors (directories, comparison sites). Ahrefs: `site-explorer-organic-competitors` on the client domain gives the same list.
2. **Seed guesses.** The client's own phrases, sales-call language, support tickets, and the words customers use for the problem (not the product category the company uses internally).
3. **Keyword suggestions.** For two or three seeds, pull suggestions and matching terms (Ahrefs `keywords-explorer-matching-terms`, DataForSEO suggestions, or `scripts/keyword_planner.py`).
4. **LLM brainstorm.** Prompt template, adapt freely:

```
We sell [what it does, in one sentence] to [who]. List 40 search queries
where someone clearly needs this kind of thing but is not yet naming a
brand. Group them by use case, audience, and situation. Exclude how-to,
definition, and "best of" queries.
```

Treat LLM output as a list of guesses. It cannot tell you which are open; Step 5 does.

## Step 2: Export competitor keywords

For each competitor (aim for 3 to 6):

1. Export all organic keywords: Ahrefs `site-explorer-organic-keywords` (country set to the market you sell in), or the Organic Keywords CSV export from any tool.
2. Keep these columns: keyword, volume (min and max if the tool gives ranges), their position, ranking URL.
3. **Strip branded terms.** Filter out any keyword containing the competitor's name or obvious misspellings. Branded queries are not winnable for you. The exception is deliberate alternatives and comparison pages, which belong to `competitor-alternatives`.
4. **Keep zero and low volume.** Blank or 0 volume usually means "not enough data", not "nobody searches". Set blanks to 1 so they sort and survive filters.
5. One sheet tab per competitor, so you can see who owns which topic.
6. For each competitor's top 5 to 10 pages by traffic (Ahrefs `site-explorer-top-pages`), look at the keywords that single URL ranks for. A page title on their site often names a use case you had not thought of.

Large exports can run to thousands of rows. Do not read them by hand; use Step 3.

## Step 3: Filter for buying stage

The buying-stage test: the searcher knows what they want but has not chosen a brand.

Passes: "invoice software for freelancers", "wedding photographer in [city]", "dog training collar with gps".
Fails: "what is invoicing" (learning), "best invoicing apps" (comparing a list), "[brand] login" (already chose), "how to write an invoice" (task help, no purchase).

Run it in two passes, relevance first, then stage. In Google Sheets with `=AI()` or as an LLM batch pass over a CSV.

**Pass A, relevance** (one column):

```
=AI("Answer only Yes or No. Is this search query about [your product category or problem space]?", A2)
```

**Pass B, buying stage** (second column, on Yes rows only):

```
=AI("Answer only Yes or No. The text is a search query. Does the person already know what kind of product or service they need, so that a single page offering it would satisfy them, without needing to pick a brand? Learning queries, how-to queries, and queries naming a specific brand are No.", A2)
```

**Pass C, stacked filter for list-seekers** (third column, on Yes rows):

```
=AI("Answer only Yes or No. The text is a search query. Is the person asking to see several options or a ranked list (for example 'best', 'top', 'alternatives', 'vs', plural product names)?", A2)
```

Keep rows that are Yes on A and B and No on C into the main backlog. Rows that are Yes on C go to a separate "list-intent" tab: they feed `competitor-alternatives` or are parked (Step 5).

Batch advice:
- Run 100 to 200 rows at a time. Sheets `=AI()` skips cells silently on larger selections, so after each run check for blanks and re-run them.
- Availability of `=AI()` varies by account and region. Fallback: paste batches of 100 keywords into an LLM with the same question and ask for a CSV of keyword plus Yes/No.
- Spot-check 20 random rows per pass against your own judgment. If you disagree on more than 3, tighten the prompt with two or three counterexamples and re-run.
- The classifier is a first cut. Anything on the borderline gets a human look in Step 5 anyway.

## Step 4: Expand

Take every passing keyword and grow it. The goal is more precise queries, each of which can have its own page.

**The "[solution] for [plural audience]" pattern.** This is the highest-leverage expansion. Combine a passing solution keyword with groups that buy in volume or carry influence: teams, schools, clinics, agencies, startups, nonprofits, lawyers, accountants, property managers, restaurants, enterprise companies, government employees, students, remote teams. Examples with fictional products: "badge printing for coworking spaces", "shift scheduling for restaurants", "expense reports for law firms". These queries read as low volume but represent a decision-maker or a purchase order, and a page that wins one often also earns links and shares from that audience.

Other variants to generate for each keyword:
- **Use case**: the job it does ("track time on client projects").
- **Audience** (singular and plural): roles, industries, company sizes.
- **Location**: cities, regions, neighborhoods, only where the service is bought locally. For remote services location is optional; build the non-local version first.
- **Service or product line**: each distinct offer gets its own query.
- **Attributes everyone has but nobody states**: "no sign up", "works offline", "same-day", "free tier". People search for these.

**Why listed volume understates value.** Tools report volume for one exact phrase. A page that ranks #1 for "scheduling software for dental clinics" usually also ranks for the sibling queries "dental practice scheduling tool", "appointment software for dentists", and a dozen more, none of which show up in your sheet as separate rows. Keep keywords with listed volume of 0 to 10 when they are open and relevant. When two keywords are equally open, take the higher-volume one first.

## Step 5: Read the SERP for winnability

Do this by hand for every shortlisted keyword, not by tool difficulty score. Open the live results (or Ahrefs `serp-overview`) and fill four checks for the top 10:

1. **Exact phrase in title and URL.** Count how many top results have the keyword (or a close natural form) in the page title and in the URL. If few or none do, nobody is targeting it.
2. **Authority.** Note the domain rating of each ranking domain. Compare to your site's DR.
3. **Intent match.** What type of page ranks: product or service pages (good), how-to articles, definitions, forums, list articles, or a mix? A SERP of product pages confirms buying intent. A SERP dominated by tutorials means searchers want to learn; a product page may bounce.
4. **List-style SERP.** If the top 10 are mostly "best X" roundups, the query is list-intent (see Step 3 Pass C).

Decision rules:

| Observation | Decision |
|---|---|
| Product/service pages rank, few have the phrase in title/URL, DRs mostly at or below yours plus 15 | take |
| One page targets it directly but has a weak hero (unclear offer, no screenshot, phrase buried) and DR within reach | take, plan to beat it |
| Phrase is in titles and URLs across the page, DRs well above yours | park |
| DR 70+ across the page even though targeting is weak | park until the site's authority grows |
| Roundup lists dominate | park, or route to `competitor-alternatives` |
| Intent is mixed or mostly informational | park, or take only if the page can open with the buying hook and add short explanatory sections |
| Not clearly related to what you sell (relevance 4 or lower) | drop from this backlog |

As a rough guide, a site with DR under 20 should start where the top results are DR 40 or lower and mostly untargeted. A new site can still take any open keyword regardless of the DRs above it if the pages ranking do not target the phrase. Treat these as starting heuristics and adjust from the first batch of results.

**Parking list.** Never delete parked keywords. Record the reason and a revisit trigger on each row, for example "revisit when site DR reaches 30", "revisit after 5 pages live and 10 referring domains", or "revisit after video ranks". Re-read the parking list every quarter, and after any authority campaign (`authority-campaign`).

**Relevance score (1 to 10).** Your own score, where 10 means the product does exactly this and 1 means barely related. Score while the SERP is open. Higher is better.

## Step 6: One page or many

Put two similar keywords side by side and compare their top 10.

- Same pages rank for both (roughly 70% or more overlap) and the meaning is the same: one page, target both. Put the stronger phrase in title, URL, and H1 and the variant in a subheading or the opening paragraph.
- Same pages rank but the meaning differs, or a searcher for one would be confused by a page titled for the other: separate pages. Example: "app for dog walkers" (a tool for the walker running a business) and "dog walking app" (often an owner looking to book a walker) can share results, yet they serve different buyers.
- Different SERPs: separate pages.

Adding a modifier like "online" or "free" rarely changes the SERP. If the results are identical, the modifier does not escape the competition and does not need its own page.

Plan about five pages at a time. Seeing them together exposes variants that belong on one page and keeps the hub categories coherent.

For lists of 50 or more keywords, hand the list to `seo-cluster` for bulk SERP-overlap clustering, then bring the clusters back as rows here.

## Step 7: Mine Search Console

Queries the site already earns impressions for are the cheapest wins. Pull the last 90 to 180 days with `scripts/gsc_query.py` (dimensions: query, page) or the GSC MCP, or take a Performance export CSV. Exclude branded queries.

Decision rule by average position, with impressions of at least 20 in the window (lower on small sites):

| Position | Action |
|---|---|
| 1 to 5 | leave alone, no edits |
| about 6 to 13 | expand the existing page: add or deepen the section that covers the query. Hand off to `striking-distance` in `bofu` mode |
| about 14 to 25 | build a new dedicated page for the query and link to it from the page that currently ranks |
| any position, but the query has its own distinct intent or does not fit the existing page naturally | new dedicated page, linked from the old one |

Add these as rows with source "GSC" and the current ranking URL in the target column (for expand) or blank (for new).

## Step 8: Build the sheet and the first batch

Create the keyword sheet (Google Sheets, Excel, or CSV) with these columns:

| Column | Meaning |
|---|---|
| keyword | exact phrase |
| hub category | the hub page the page will live under (for example uses, services, industries, alternatives); becomes the URL folder |
| sub-category | optional modifier: product line, audience, location |
| buying-stage | yes or no from Step 3 |
| relevance (1-10) | higher is more relevant |
| min volume, max volume | the tool range; use 1 for blank |
| SERP notes | one or two lines from Step 5: who ranks, targeting, DRs, intent |
| decision | take, park, or merge |
| target URL | proposed URL, or the existing URL for expand and merge rows |
| status | backlog, planned, live, parked, dropped |

Add two optional columns when useful: source (competitor, seed, LLM, GSC) and revisit trigger (parked rows only).

**Prioritize the first batch of about five pages.** Sort take rows by relevance descending, then:
1. High-leverage rows first: plural audience and decision-maker keywords.
2. Then the easiest SERPs (fewest targeted results, lowest DRs).
3. Among near ties, higher volume wins.
4. Avoid picking five near-duplicates; pick a spread across hubs so the first hub page has real content.

For each of the five, write one line: keyword, hub, target URL, why it is open, the one thing that will make the page better than what ranks.

## Guardrails

- Do not discard keywords on volume alone. Park or take them on SERP evidence.
- Do not treat LLM suggestions or `=AI()` output as verified. Every taken keyword must have a SERP note you wrote yourself.
- Do not target competitor brand names here; that is the alternatives workflow.
- Do not promise rankings. Winnability is a judgment, and the first batch calibrates it.
- Do not create separate pages for keywords that share a SERP and meaning; that produces competing pages.
- Where listed volume or DR is missing, write `[NEEDS DATA]` in the cell rather than estimating.
- White-hat only. This skill does no outreach and sends nothing.

## Output

1. The keyword sheet (CSV or table) with the columns in Step 8.
2. A parking list: keyword, reason, revisit trigger.
3. A first batch of about five pages, one line each.
4. A short note: competitors used, filters applied, number of rows at each stage (exported, relevant, buying-stage, taken, parked, merged), and anything that needs client input.

## Next Step

- `bofu-hub-pages`: design the hub pages and footer links that will list these pages.
- `bofu-landing-page`: spec and write each page in the first batch.
- `keyword-deep-dive`: go deep on any single row that is unusually valuable or unclear.
- `seo-cluster`: bulk clustering for large lists.
- `striking-distance` (bofu mode): expand rows from Step 7 that point at existing pages.
- `bofu-playbook`: for the engagement-level sequence and cadence.
