---
name: authority-campaign
description: Use when you need to run an executed, tracked off-site authority program that earns links and gives AI assistants third-party sources to cite about a brand. Covers directories, launch platforms, expert quotes, press releases, a press kit, podcast guesting, events, and linkable assets. Also use when the user mentions "authority campaign", "brand mentions", "get listed in directories", "HARO", "press release for AI answers", "podcast guesting for links", or "off-site plan".
user-invocable: true
argument-hint: "<domain> [niche] [budget] [expert available]"
license: MIT
metadata:
  author: aabrole
  version: "1.0.0"
  category: seo
---

# Authority Campaign

An executed off-site program, not a strategy deck. It takes a brand from "few third-party mentions" to a steady stream of listings, quotes, interviews, and coverage, and it records every action in one tracker so results can be traced back to effort.

Why it works: search engines weigh links and brand mentions from other sites, and AI assistants build brand answers ("what is X", "is X legit", "X vs Y") from whatever third-party pages they can retrieve. A brand with only its own site as a source gets thin, hedged answers. Each listing, quote, and interview adds an independent source, and the cheap tactics add up faster than one expensive one.

This skill complements `linkbuilding`. That skill classifies the site's authority phase and holds the tactic playbooks (guest posting, resource pages, skyscraper, partnerships). This one runs the repeatable, operational tactics week after week with a tracker. Use `linkbuilding` to decide strategy; use this to execute.

## Input

- **Domain and brand facts** (required): legal name, one-line description, founding year, location, offer, pricing model, social profiles, logo files. Anything missing is marked `[CLIENT TO CONFIRM]`.
- **Expert(s) available** (required for quotes and podcasts): who can answer questions, their real credentials, and hours per week they can give.
- **Budget** (optional): monthly and one-off. Default assumption is near zero, which still supports most of this program.
- **Niche and location** (required): drives directory choice, meetup choice, and journalist request filters.
- **Target pages** (optional): the money pages or hub pages that should receive links. If none, use the homepage plus the top 3 commercial pages.

## Role

You are a senior digital PR and link practitioner. You prepare drafts, lists, and trackers. You do not send, submit, post, or pay. The human reviews and sends every outward action.

## Step 1: Baseline

Capture before any outreach so progress is measurable.

1. **Link baseline.** Referring domains, total backlinks, top anchors, and follow/nofollow split. Use `seo-backlinks` or the Ahrefs MCP (referring domains, anchors). Fallback: ask for a CSV export from any backlink tool, or use Search Console's Links report for a rough count.
2. **Branded search baseline.** Branded query impressions and clicks from GSC (last 90 days). Fallback: a screenshot or CSV of the Performance report filtered to the brand name.
3. **Brand SERP.** Google the brand name plus "reviews", "legit", "alternatives". Record which third-party domains appear on page 1 and whether the brand owns the results.
4. **AI answer baseline.** Run `aeo-audit` or `geo-brand-mentions` (or manually ask 3 or more assistants the same 8 to 10 questions: what is [brand], is [brand] legit, [brand] vs [competitor], best [category] for [use case]). Save the answers and the cited sources verbatim with the date.
5. **Competitor reference.** Pick 2 or 3 competitors and note their referring domain counts and the directories and publications they appear in.

Write the baseline into the tracker's `Baseline` tab (see Step 3).

## Step 2: Pick Tactics by Priority and Effort

Default priority is ordered by certainty, cost, and effort. Work down the list; do not skip to the glamorous items first.

| Order | Tactic | Effort | Cost | Reliability | Reference |
|---|---|---|---|---|---|
| 1 | Directories and citations | Low, front-loaded | Free to low | High | `references/directories-and-launches.md` |
| 2 | Launch platforms | Low per launch | Free to low | Medium-high | `references/directories-and-launches.md` |
| 3 | Expert quotes (journalist requests) | Daily, 15-30 min | Free to about 100 USD/mo | High, steady | `references/expert-quotes.md` |
| 4 | Press kit page | One-off, 2-4 hours | Free | Supports every other tactic | `references/press-kit.md` |
| 5 | Event and meetup link building | Medium, slow | Low | Medium, local | `references/events-and-linkable-assets.md` |
| 6 | Podcast guesting | Medium, recurring | Free to low | Medium-high | `references/podcast-guesting.md` |
| 7 | Linkable assets (tools, data, templates) | High | Time or dev cost | Uncertain | `references/events-and-linkable-assets.md` |
| 8 | Press releases | Low effort, real cost | Check current pricing | Low for rankings, useful for brand answers | `references/press-releases.md` |

Adjust by situation:

- **No budget:** do 1, 2, 3, 4, 5, 6. Skip paid tiers of everything.
- **No expert time:** do 1, 2, 4, 8 (brand-answer release). Expert quotes and podcasts need a real person; do not substitute generated answers.
- **Local or service-area business:** hand NAP and citation consistency to `seo-local` before bulk directory submission.
- **Software or app:** launch platforms and a micro-tool move up; local events move down.
- **Regulated niche (health, finance, legal):** every public claim needs a source, and quotes need expert review. Slow down on press releases.
- **Brand answers are the main problem** (people searching "is [brand] legit"): move the brand-answer press release and the press kit up to positions 3 and 4, and pair with `review-amplification`.

Set a quarterly target in the tracker (for example 40 live listings, 12 published quotes, 3 podcast episodes) so the weekly cadence has a finish line.

## Step 3: Build the Campaign Tracker

One tracker for the whole program. A spreadsheet or CSV is enough. Columns:

| Column | Notes |
|---|---|
| Tactic | directory, launch, quote, press release, press kit, podcast, event, asset |
| Target | Site, show, outlet, or event name |
| Target URL | Where the submission or pitch goes |
| Status | idea, drafted, approved, submitted, pending, live, rejected, dead |
| Date submitted | ISO date |
| Live URL | The page that contains the link or mention |
| Link type | link, brand mention without link, profile, citation, embed |
| Anchor | Exact anchor or mention text |
| Follow / nofollow | Check the rel attribute on the live page, not the directory's claim |
| Target page | Which page on the client site the link points to |
| Notes | Login owner, renewal date, cost, contact, rejection reason |

Add two more tabs:

- **Baseline:** the Step 1 numbers with dates.
- **Credentials:** which email address, profile name, and boilerplate was used on each platform. Never store passwords in the file; point to the client's password manager entry instead.

Status rules: a row is `live` only after you have opened the live URL and confirmed the link or mention is present. Re-check live rows once a quarter; listings get removed.

## Step 4: Run Each Tactic

Open the reference for the tactic you are running and follow it. Every outward item is prepared as a draft in the tracker with status `drafted`; the human moves it to `approved` and sends it.

- Directories and launches: `references/directories-and-launches.md`
- Expert quotes: `references/expert-quotes.md`
- Press release: `references/press-releases.md`
- Press kit: `references/press-kit.md`
- Podcasts: `references/podcast-guesting.md`
- Events and linkable assets: `references/events-and-linkable-assets.md`

Build the shared assets once before starting (they are reused everywhere):

- **Brand fact sheet:** name, founding year, location, offer, 25-word, 50-word, and 100-word descriptions, founder names and titles, product list, categories, official URLs.
- **Asset folder:** logos (SVG and PNG, light and dark), headshots, 3 to 5 product screenshots, an OG image.
- **Expert bio:** 2 sentences and 5 sentences versions, with verifiable credentials only.

If the fact sheet has gaps, mark them `[CLIENT TO CONFIRM]` and stop for answers rather than guessing.

## Step 5: Weekly Cadence

A sustainable cadence for a one-person or small team program:

| When | Work | Volume |
|---|---|---|
| Daily (working days) | Triage journalist requests, draft answers for the expert | 1-2 answers per day |
| Monday | Review tracker, chase pending items, plan the week | 30 min |
| Tuesday-Wednesday | Directory batches (10-20 submissions per batch, drafted for human submission) | 1 batch per week until the list is done |
| Thursday | Podcast pitches and host follow-ups | 5-10 pitches per week |
| Friday | Verify new live links, update the tracker, log published quotes | 30 min |
| Monthly | One bigger item: a launch, a release, an event, or an asset update | 1 per month |

Pace links so they look natural. Spread directory batches across weeks rather than submitting everything on one day. See `linkbuilding` (link velocity guidelines) for the ranges this should stay inside.

## Step 6: Monthly Report

Compare against the baseline. Report:

- Referring domains: net new, lost, and total (Ahrefs MCP, `seo-backlinks`, or CSV).
- Live links and mentions by tactic, with live URLs.
- Follow vs nofollow split and anchor mix.
- Branded impressions and clicks from GSC versus baseline.
- AI answer retest: rerun the same questions from Step 1, note any new cited third-party sources, and whether answers about the brand became more accurate or specific.
- Rankings for target pages (hand to `publish-and-track` if it is in use).
- Effort and cost by tactic, and cost per live link.
- Next month's plan with the three highest-yield tactics.

Link effects on rankings take weeks to months. Do not judge a tactic on its first 30 days; judge it on live-link count and quality, then on ranking movement over a quarter.

## Anchor Text Guidance

Consistent with `linkbuilding` (Step 3 and its anchor safety guide):

- Most anchors should be the brand name, the bare URL, or natural phrases. This is what directories, press, podcasts, and events produce by default.
- Exact-match keyword anchors are sparing. Never ask a directory, journalist, or host to use a keyword-stuffed anchor.
- Where you control a link description (a directory description, a signature line, a show-notes blurb), use a descriptive phrase that reads naturally, such as the brand plus what it does.
- Link to the most relevant page (a hub or service page) when the platform allows deep links; the homepage should not receive every link.
- Check the anchor mix monthly. If exact-match exceeds roughly 5 percent of new anchors, shift the next batch to branded and URL anchors.

## Guardrails

- Never fabricate reviews, testimonials, quotes, stats, credentials, or press claims. Mark unknowns `[NEEDS SOURCE]` or `[CLIENT TO CONFIRM]`.
- Journalist answers and expert quotes come from the client's real expertise. AI can structure and tighten them; the substance comes from the expert and the expert approves the final text before it is sent.
- Stay inside each platform's rules. No sockpuppet accounts, vote manipulation, fake launch upvotes, undisclosed self-promotion, or spam on Reddit, forums, or directories. Disclose affiliation where relevant.
- All outreach, pitches, submissions, and paid distribution (including press release purchase) are drafted for the human to send or approve. This skill does not send or pay.
- White-hat only. No PBNs, paid link schemes, link exchanges, or parasite SEO. Paid placements must be labeled as sponsored and use the right rel attributes.
- Do not pay a podcast or publication to feature the brand as if it were editorial. Sponsored content is fine only when disclosed as such.
- Treat directory and platform logins as client property. Use a shared role email the client controls, not a personal address of the practitioner.
- Do not scrape or mass-contact journalists. Use the platforms' own request flows.

## Output

Deliver:

1. **Baseline summary** (table of Step 1 numbers and the AI answer snapshot).
2. **Tactic plan**: ordered list with quarterly targets, owners, and cost.
3. **Campaign tracker** (CSV or spreadsheet with the columns above), pre-filled with the first batch of targets in `drafted` status.
4. **Draft pack** for the first two weeks: directory submission text, 5 sample quote answer shells awaiting expert input, podcast pitch, and the press kit content outline.
5. **Monthly report** template filled for the first month.

## Next Step

- `seo-backlinks` for ongoing link monitoring and toxic link review.
- `aeo-audit` and `geo-brand-mentions` for the AI answer retests.
- `seo-local` for NAP and citation consistency on local businesses.
- `video-seo` to turn podcast episodes into clips.
- `linkbuilding` for guest posting, resource pages, and partnership plays once the foundation here is in place.
- `striking-distance` to point new link equity at pages already ranking on page 2.
