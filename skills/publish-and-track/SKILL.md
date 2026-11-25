---
name: publish-and-track
description: Use when a page is ready to go live or is already live and needs QA, indexing, rank tracking, or a fix plan. Produces a pre-publish checklist, indexing steps, a per-page tracking sheet, a change log, and a weekly check routine. Also use when the user mentions "publish checklist", "request indexing", "rank tracking setup", "page not ranking", "how long to rank", "stuck on page 2", "change log", or "new queries in GSC".
user-invocable: true
argument-hint: "<url or draft file> [target keyword(s)] [site/GSC property]"
license: MIT
metadata:
  author: aabrole
  version: "1.0.0"
  category: seo
---

# Publish and Track

Takes a finished page through go-live, indexing, and rank tracking, then runs a light weekly routine that tells you when to wait, when to fix, and when a new query deserves its own page.

Why this works: most ranking losses on new pages come from skipped basics (typos, broken social previews, an unindexed URL, no tracking) or from editing a page that was already climbing. A fixed sequence plus a change log removes both problems. Timelines are ranges, so the routine is built around patience first and a defined fix ladder second.

## Input

- **Page** (required): live URL or draft file
- **Target keywords** (required): 1-3 variants the page should rank for (primary plus close variants)
- **Site access** (optional): GSC property, Ahrefs project, or CSV exports
- **Hub/category** (optional): which hub page or category the page belongs to, used for tags

## Role

You are a careful release manager for SEO pages. You do the checks, record what changed and why, and refuse to tweak pages that are moving in the right direction.

## Step 1: Pre-Publish QA

Run these before the page goes live. Report each as pass, fix, or needs-human.

1. **Spelling and grammar.** Ask for errors only, not a rewrite. Prompt template: "List spelling, grammar, and punctuation errors in the text below with the exact location. Do not rewrite the passage." Run it on the body, title tag, meta description, H1, image alt text, and social preview text.
2. **Awkward keyword phrasing.** If the target keyword is a fragment or misspelling, the title and H1 should read as natural language, with correct spelling. A slightly lower exact-match score is fine.
3. **On-page check.** Confirm the keyword appears in the URL, title, H1, meta description, and the first sentence of the body. Confirm it does not appear in every section. If an on-page grader is available (Moz, Ahrefs, Semrush, or the `seo-page` skill), aim for a strong score but not a perfect one; a page tuned to the maximum is more likely to read as stuffed. Treat roughly 90-98 on a 100 scale as the target band, and judge by reading the page.
4. **Social preview (Open Graph).** After the page is live, test the URL in a sharing debugger (Facebook Sharing Debugger, LinkedIn Post Inspector). Check og:url, og:title, og:description, and og:image. Re-scrape if the preview is empty or stale. Confirm the image is relevant and not obviously generated filler.
5. **Above the fold.** The first screen has a relevant image, the keyword in the opening sentence, and enough specific detail that a visitor knows they are in the right place.
6. **Copy hygiene.** Run any AI-assisted copy through `copy-watermark-hygiene` and `scripts/clean_copy.sh` if the client has asked for it. Remove invisible characters and tell-tale phrasing. Do not state or imply that copy was not AI-assisted unless that is true.
7. **Facts.** Every number, quote, review, or credential on the page has a source or is flagged `[NEEDS SOURCE]` / `[CLIENT TO CONFIRM]`.
8. **Technical basics.** Indexable (no noindex), not blocked in robots.txt, canonical points to itself, page is in the XML sitemap, at least one internal link from the relevant hub, not an orphan. If several new pages share a problem, hand off to `seo-technical`.

## Step 2: Go Live

The human publishes. Provide the final title, meta description, URL, and OG values in one block so the person can paste them. After publishing:

1. Open the live URL and confirm it renders, returns 200, and is not a staging copy.
2. Re-run the social preview check (Step 1.4) on the live URL.
3. Record the go-live date in the tracking sheet.

## Step 3: Request Indexing

- **GSC URL Inspection.** Inspect the URL. If it reports "URL is not on Google", use Request Indexing. Do the same after any meaningful update to an existing page. With credentials set up, `scripts/gsc_inspect.py <url> --site-url sc-domain:<domain>` returns the inspection result, and `--batch urls.txt` handles several URLs. The Request Indexing button itself is only available in the GSC interface, so the human clicks it.
- **IndexNow (Bing, Yandex and others).** If the site supports IndexNow, submit the new or changed URL with `scripts/indexnow_submit.py --host <host> --key <key> --key-location <url> --urls <url>`. This does not notify Google. It is optional and worth doing only when the key file is already hosted.
- **Sitemap.** Make sure the sitemap lists the new URL and its lastmod is accurate. See `seo-sitemap`.
- Do not submit the same URL repeatedly. One request per meaningful change is enough.

## Step 4: Set Up Rank Tracking

For each page:

1. **Keywords:** track 1-3 variants per page (the primary keyword plus the variants the page might also rank for). More variants add noise without insight.
2. **Tags:** apply a tag for the hub or category, a tag for the page type (landing page, alternative, use case, blog), and a `branded` tag for any keyword containing the brand name. Segment branded keywords out of reports because they rank easily and distort averages.
3. **Location and device:** set the country or city the buyers search from. For local services use the city or a zip code. Track mobile if most traffic is mobile.
4. **Tool:** Ahrefs Rank Tracker (via the Ahrefs MCP or project import) is first choice. Fallback: GSC. Pull `scripts/gsc_query.py` or the GSC MCP with `query,page` dimensions weekly and record average position. GSC averages across impressions, so a new page with few impressions looks noisy; note that in the sheet.
5. **Baseline:** record position at go-live ("not ranking" is a valid baseline).

## Step 5: Set Expectations

Use ranges, not promises:

| Stage | Typical range for a new page on an established site |
|---|---|
| First appearance in results | roughly 1-6 weeks, sometimes longer |
| Page one | often 1-3 months |
| Settling into a stable position | several months |
| Weekly movement | up and down by several positions is normal |

Weaker or newer sites, competitive SERPs, and pages with few internal links run slower. Late bloomers happen: a page can sit beyond position 50 for months and then jump. A page that is climbing or oscillating within a few positions of a better rank is behaving normally.

**Rule: leave climbing pages alone.** If position has improved or held over the last 3-4 checks, make no copy edits. Edits reset the signal and make results impossible to attribute.

## Step 6: Change Log

Every edit to a tracked page gets a row, including re-requested indexing. Template:

| Date | URL | Change | Reason | Expected effect | Check date | Result |
|---|---|---|---|---|---|---|
| YYYY-MM-DD | /path | e.g. rewrote title to add differentiator | CTR low at position 6 | CTR up within 2-4 weeks | +28 days | fill in later |

Rules: one change per row, state the hypothesis before the result, and review the result at the check date. Reverse a change only if a clear drop follows and no other cause is plausible.

## Step 7: Stuck-Page Fix Ladder

Use after about 3-4 months with no appearance, or when a page is stuck on pages 2-3 or below its likely ceiling, and only if the Step 5 rule does not apply. Work down the list, one change at a time where possible, logging each.

1. **Technical check first.** If most new pages fail, the cause is almost always site-wide: noindex, robots.txt block, orphaned pages, a staging copy indexed, thin indexed junk. Hand off to `seo-technical` and `seo-audit`. Do not edit copy until this is ruled out.
2. **Above the fold.** Weak opening sentence, vague detail, irrelevant or obviously generated hero image. Rewrite the first screen so a searcher confirms they are in the right place.
3. **Title differentiator.** When many results use the same keyword in the title, add a real benefit or access detail after the keyword (for example a free tier, no signup, a limit, a speed). Only claim what is true. Check CTR in GSC to confirm this is the problem.
4. **De-optimize repetition.** If the keyword appears in nearly every section, remove it from some body sections. Keep it in URL, title, H1, meta description, and opening sentence.
5. **Natural phrasing.** Fix titles and headings that copy an awkward fragment verbatim; correct spelling and grammar.
6. **Internal links.** Add links from other relevant pages (not only the hub), with descriptive related anchors. Use GSC to find pages that already get impressions for similar queries and link from those. See `site-architecture`. Links only help if searchers want the destination.
7. **Intent mismatch.** Compare the page to what actually ranks. If the SERP shows mixed intent, keep the buying hook at the top and add short sections for the other intents (why, benefits, how it works), and widen the title and meta slightly. Length barely grows. If the SERP is clearly informational, the page may be the wrong asset; hand off to `bofu-keyword-research` for re-evaluation.
8. **Authority and demand.** If all of the above are fine and the SERP is dominated by much stronger domains, the page needs off-site support. Hand off to `authority-campaign` and `linkbuilding`, or consider a less competitive variant.

## Step 8: Weekly Check Routine

Run weekly, about 15 minutes:

1. Pull positions for all tracked keywords. Update the tracking sheet.
2. Flag pages by state: **new** (under 6 weeks, no action), **climbing** (leave alone), **plateau** (flat 6+ weeks at position 4-15, check CTR and consider a Step 7 item), **dropped** (down 5+ positions for 2 consecutive checks, check technical status and recent changes in the log), **stuck** (3-4 months, Step 7).
3. Check GSC Pages and Performance reports for **new queries**: queries with real impressions that no page targets directly. Apply the rule: if an existing page already ranks within roughly positions 8-30 for a query it half answers, expand that page (hand off to `striking-distance`). If the query shows a distinct buying intent the page does not serve, or no page ranks, plan a new page (hand off to `bofu-keyword-research`).
4. Look at the change log for rows whose check date has arrived and record results.
5. Note anything that needs a human decision.

## Guardrails

- The skill prepares; the human publishes, requests indexing, and approves edits.
- Never fabricate rankings, traffic, or results. Missing data is reported as missing.
- No mass resubmission of URLs or automated indexing spam.
- Do not edit climbing pages or change more than one major element at once without logging it.
- Timelines are ranges drawn from general experience, not guarantees. Do not promise a client a position or date.

## Output

1. **Pre-publish QA table:** check, status, notes.
2. **Go-live block:** final URL, title, meta description, OG values.
3. **Indexing log:** GSC inspection status, IndexNow status, sitemap status.
4. **Per-page tracking sheet:**

| URL | Hub/category | Tags | Keyword | Location/device | Go-live | Baseline | Wk1 | Wk2 | Wk3 | Wk4 | State | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

5. **Change log** (template above, empty or filled).
6. **Weekly routine** with this week's flags and new-query candidates (query, impressions, current page, recommendation).

## Next Step

- Pages stuck for technical reasons: `seo-technical`, `seo-audit`
- Page 2 queries and expansion: `striking-distance`
- New query to build a page for: `bofu-keyword-research`, then `bofu-landing-page`
- Off-site support: `authority-campaign`, `linkbuilding`
- Orchestrated engagement plan: `bofu-playbook`
