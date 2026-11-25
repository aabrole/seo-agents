---
name: bofu-playbook
description: Use when you need to sequence a bottom-of-funnel SEO engagement end to end, from the defensive audit through keyword research, landing pages, tracking, video, reviews, off-site authority, and AI citation retests. Produces a 90-day plan, weekly rhythm, and KPI list. Also use when the user mentions "BOFU playbook", "SEO engagement plan", "90-day SEO plan", "what order should we do SEO in", "landing page cadence", "BOFU-first strategy".
user-invocable: true
argument-hint: "<site url> [goals] [constraints]"
license: MIT
metadata:
  author: aabrole
  version: "1.0.0"
  category: seo
---

# BOFU Playbook

Orchestrates a bottom-of-funnel SEO engagement. It does not do the work of each step; it puts the steps in a sensible order, sets a cadence, says what "done" means at each stage, and names the skill that does each one.

Why this order: the site must be crawlable and fast before new pages can be judged, keywords must be chosen before pages are written, and pages need a hub and tracking before off-site work starts sending authority to them. Video, review, and platform work reuse the same keywords, so they run in parallel once the keyword sheet exists. Off-site work comes after there are pages worth linking to.

## Input

- **Site** (required): domain, what is sold, to whom, and the conversion that matters (sign-up, booking, purchase, lead form).
- **Current state** (optional): existing audit, GSC access, analytics, competitor list.
- **Capacity** (optional): who writes, who publishes, who approves. Default assumption: one practitioner plus one client contact who approves.
- **Horizon** (optional): default 90 days.

## Role

You are the engagement lead. You decide sequence, hold the cadence, and say no to work that does not serve the plan. You hand work to the specialist skills and check their outputs against the done criteria below. Outward actions (outreach, submissions, posting, paid distribution) are prepared as drafts for the human to send; nothing here sends or pays.

## Step 1: Intake and baseline (week 0)

Collect, and write down with dates:
- GSC and GA4 access, and the conversion event definition. If conversions are not tracked, fixing that is the first task (GA4 checks via `seo-google`).
- A baseline snapshot: indexed pages, clicks and impressions (90 days), top 20 queries, current rankings for 10 to 20 money keywords, referring domains, DR.
- An AI visibility baseline: run `aeo-audit` on the brand and 10 to 15 buying-stage prompts. Record which sources are cited and whether the brand is named. This is the before measurement for Step 9.
- Constraints: CMS limits, who can ship code, legal or compliance review, claims that cannot be made.

Done check: a baseline file exists with dated numbers, and every later KPI can be compared to it.

## Step 2: Defensive technical audit (weeks 1 to 2)

Run `seo-audit` for the full picture and `seo-technical` for crawlability, indexability, rendering, and speed. Fix before publishing new pages:
- Crawl blockers, noindex mistakes, staging site indexed, duplicate hosts, redirect chains.
- Thin or duplicate pages that are indexed (consolidate or noindex).
- Orphan pages, broken internal links.
- Page speed and rendering. Balance note: this plan is BOFU-first, but a large or JavaScript-heavy site still needs real performance and rendering work (server-side rendering or prerendering, bundle size, Core Web Vitals) before new pages will perform. Do not skip this to publish faster.

Done check: no critical or high technical findings open, a clean sitemap submitted, and the fix list shipped or scheduled with owners.

## Step 3: Keyword research (weeks 1 to 3, overlaps Step 2)

Run `bofu-keyword-research`. Start it in week 1 because it does not depend on the fixes.

Done check: keyword sheet with decisions on every row, a parking list with revisit triggers, and a first batch of about five pages. Aim for 30 or more take rows before moving on; the backlog should always be at least one batch ahead of the writing.

## Step 4: Hub pages (week 2 to 3)

Run `bofu-hub-pages` to design one or two hub pages that list the landing pages by category, how they link from the footer (and nav or home page if appropriate), and click depth. Publish the hub before the first landing page so each new page has a home from day one. Use `site-architecture` if the whole site structure needs rework.

Done check: hub live, linked from the footer on every page, reachable in three clicks or fewer from the home page.

## Step 5: Landing pages at a steady cadence (week 3 onward)

For each keyword in the batch run `bofu-landing-page`, then `publish-and-track`. Target one page every 1 to 2 working days. That cadence is realistic only because BOFU pages are short and built from a repeatable template; it is not a promise for long guides.

Scope note: for BOFU landing pages this plan intentionally overrides the word-count floors that apply to general service pages in `seo-content` and the quality gates. A focused page of a few hundred words that fully answers the buying query is the target; padding it to meet a floor works against the page. Programmatic or templated pages still need unique content per page; do not clone pages with only the keyword swapped (see `programmatic-seo` quality gates).

Per page, the loop:
1. Spec and write (`bofu-landing-page`).
2. Pre-publish QA, indexing request, tracking setup, change log entry (`publish-and-track`).
3. Add to hub and to the keyword sheet (status live, date).

After each batch of about five pages: re-audit. Run a crawl or `seo-audit` limited to the new URLs and check titles, meta descriptions, H1s, canonicals, and internal links against the spec. Fix and resubmit; 301 any URL that changed.

Done check per page: indexed, tracked, on the hub, linked from at least one other relevant page.

## Step 6: Existing pages and search data (every 2 to 4 weeks from week 4)

Mine Search Console (`bofu-keyword-research` Step 7). Expand pages sitting at about 6 to 13 with `striking-distance` in bofu mode. Spin off new pages for queries at about 14 to 25 or with a distinct intent.

Balance note: informational answer-first content still matters. AI answer engines pull from pages that answer sub-questions directly, and a BOFU-only site can be invisible there. Run `fanout-coverage` on the top 3 to 5 head topics and add short answer blocks to existing BOFU pages or a small number of supporting guides. Do not build a large top-of-funnel blog to do this.

## Step 7: Parallel channels on the same keywords (from week 4)

Once the first batch of pages is live, reuse the keyword list on other surfaces. Each is its own skill:
- `video-seo`: videos and short-form clips for the buying keywords, keyword first in the title.
- `platform-seo`: Reddit participation (disclosed, within each community's rules) and app store listings, where the product is relevant.
- `review-amplification`: turn real customer reviews into content for "[brand] review" style searches and AI answers. Real reviews only.

Done check per channel: first assets published against the top 5 keywords, tracked in the same sheet.

## Step 8: Off-site authority (from week 6, in priority order)

Run `authority-campaign`, which sequences the tactics; `linkbuilding` classifies the site's phase and `seo-backlinks` audits the profile. Default priority, cheapest and most reliable first:
1. Directories and citations that fit the category.
2. Niche launch platforms.
3. Expert quotes through journalist-request platforms (the expert answers; AI only helps structure).
4. Event and meetup involvement.
5. Podcast guesting.
6. Linkable assets or small free tools (uncertain payoff, needs time).
7. Press releases, sparingly, aimed at branded AI answers.

White-hat only: no paid link schemes, networks of private sites, or parasite SEO. All pitches and submissions are drafted for a human to send.

## Step 9: AI citation retest (week 8 and week 12)

Rerun the Step 1 prompt set with `aeo-audit` and compare citations and brand mentions. Use `fanout-coverage` for the gaps and `geo-brand-mentions` to see which third-party surfaces are shaping answers. Report changes honestly, including no change.

## 90-day plan template

Adjust the dates and owners to the engagement. "Practitioner" is whoever runs the skills; "Client" approves and ships.

| Weeks | Deliverables | Owner | Done check |
|---|---|---|---|
| 0 | Baseline snapshot, conversion tracking confirmed, AEO baseline | Practitioner, Client (access) | Dated baseline file; conversion event fires in GA4 |
| 1-2 | Technical audit report, fix list; keyword research started | Practitioner; Client dev ships fixes | No critical findings open; sitemap clean |
| 2-3 | Keyword sheet with decisions, parking list, first batch of 5 pages; hub design | Practitioner; Client approves batch | 30+ take rows; batch approved |
| 3 | Hub page(s) live | Practitioner, Client | Hub in footer, three clicks or fewer |
| 3-5 | Landing pages 1-5 live, one per 1-2 working days | Practitioner writes, Client approves and publishes | Each page indexed and tracked |
| 5 | Batch 1 re-audit, fixes resubmitted | Practitioner | Titles, metas, H1s match spec |
| 5-8 | Landing pages 6-10; first GSC mining round | Practitioner | Existing-page expansions and spin-offs listed |
| 4-8 | Video and platform assets for top 5 keywords; review content | Practitioner drafts, Client approves and posts | Assets live and tracked |
| 6-12 | Authority campaign: directories, launches, expert quotes, podcasts | Practitioner drafts, Client sends | Submissions logged with date and status |
| 8 | Mid-point report; AI citation retest 1; parked keywords re-read | Practitioner | Report delivered; retest compared to baseline |
| 9-11 | Landing pages 11-15; striking-distance refreshes; stuck-page fixes | Practitioner | Change log current |
| 12 | Batch 3 re-audit; AI citation retest 2; 90-day report; next-quarter plan | Practitioner | Report with KPIs below and a ranked next-90-day list |

Expect new pages to take a few weeks to appear and one to three months to settle, with weekly volatility, and some pages longer. Do not edit pages that are climbing; use the stuck-page ladder in `publish-and-track` after about three to four months with no movement. A client who expects page-one results at week 4 should be told this at the start.

## Weekly operating rhythm

| Day | Work |
|---|---|
| Monday | Review rank tracker and GSC (7-day vs prior 7-day). Flag pages that moved 5 or more positions. Update the change log. Pick this week's pages from the sheet |
| Tuesday to Thursday | Write and publish 2 to 3 landing pages (`bofu-landing-page`, `publish-and-track`) |
| Wednesday | One off-site or channel task: a directory batch, an expert-quote draft, a video script, a review post |
| Friday | Check indexing of last week's pages; refill the backlog to one batch ahead; send the client a one-paragraph status with pages live, blockers, and approvals needed |
| Every 2 to 4 weeks | GSC mining round; parked-keyword scan; batch re-audit |

## KPIs to report

Report the same table every time, against the baseline.

| KPI | Source | Note |
|---|---|---|
| Pages live (BOFU, by hub) | CMS, keyword sheet | Count live and indexed, not drafted |
| Keywords in top 3 / top 10 | Rank tracker, or GSC average position if no tracker | Separate branded from non-branded |
| BOFU clicks and impressions | GSC filtered to BOFU URLs | Weekly and cumulative |
| BOFU conversions | GA4 key events filtered to BOFU landing pages | Sign-ups, bookings, purchases; define once |
| Referring domains and links earned | Ahrefs or Moz, `seo-backlinks` | List the link, the source, and the date |
| AI citation retest | `aeo-audit` prompt set, weeks 0, 8, 12 | Citations, brand mentions, which sources were cited |
| Pages stuck | Keyword sheet | Pages older than 12 weeks with no top-20 position |

Do not report vanity totals (total keywords tracked, total impressions across the site) as results. Do not report an estimated traffic value as revenue.

## Guardrails

- Never fabricate reviews, testimonials, quotes, statistics, credentials, or press claims. Mark unknowns `[NEEDS SOURCE]` or `[CLIENT TO CONFIRM]`.
- Expert quotes and journalist answers come from the client's real expertise and are approved by them before sending.
- Reddit, forum, and community work follows each platform's rules: no sockpuppets, vote manipulation, or undisclosed self-promotion; disclose affiliation.
- Outreach, submissions, posts, and any paid distribution are drafted for the human to send or approve.
- White-hat only. No private blog networks, paid link schemes, or parasite SEO.
- Where a client's industry has advertising or claims rules (health, finance, legal), get compliance sign-off on copy before publishing.

## Output

1. The engagement plan: the 90-day table filled with real dates, owners, and done checks.
2. The weekly rhythm with the first four weeks scheduled.
3. A KPI table with baseline values and the reporting cadence.
4. A risks list: technical blockers, approval bottlenecks, authority gap versus the SERPs, and where the BOFU-first approach needs balancing (informational coverage, performance work).
5. A skill map: which skill runs at which step for this client.

## Next Step

Start with `seo-audit` and `seo-technical` for Step 2, and `bofu-keyword-research` in parallel. After the first batch ships, move to `publish-and-track` and the parallel channels.
