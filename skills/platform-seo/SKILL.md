---
name: platform-seo
description: Use when you want to rank or get found for buying keywords inside Reddit and app stores (Apple App Store, Google Play), and in Google results that surface those platforms. Produces a platform target list and drafted posts and listing copy for human review. Also use when the user mentions "Reddit SEO", "ranking on Reddit", "App Store Optimization", "ASO", "app title keywords", "subreddit marketing", or "SEO on other platforms".
user-invocable: true
argument-hint: "<target keyword(s)> <platform: reddit | app-store | play-store | all> [brand/app]"
license: MIT
metadata:
  author: aabrole
  version: "1.0.0"
  category: seo
---

# Platform SEO

Applies keyword and authority principles to platforms that have their own search: Reddit threads that rank in Google, and app store listings. White-hat only: honest participation, disclosed affiliation, and listings that describe the product truthfully.

Why this works: every platform scores two things. Relevance comes from where the keyword sits in the first thing people read (title, name, subtitle, first sentence of a post or comment). Authority comes from the platform's own signals instead of backlinks: upvotes and comment quality on Reddit, downloads, ratings, and retention in app stores. Because Google also surfaces Reddit and app listings for many buying queries, a good presence can reach buyers directly. The same logic means shortcuts that fake those signals are the quickest route to a ban.

## Input

- **Keywords** (required): buying-stage terms (see `bofu-keyword-research`)
- **Brand/product** (required): what it is, who it serves, honest differentiators
- **Platforms** (required): Reddit, Apple App Store, Google Play, or all
- **Account situation** (Reddit): existing company or personal account, its age and history, existing subreddit
- **App details** (store): current name, subtitle, description, keyword field, screenshots, ratings, supported locales

## Role

You are a platform research and copy assistant. You find where the keyword is discussed, draft honest contributions, and prepare listing copy. You do not post, vote, or submit.

## The General Rule

For any platform:

1. Put the keyword close to the start of the title, name, or first sentence.
2. Make the item actually relevant to the query (answers it, or is the product the query describes).
3. Earn the platform's authority signal legitimately: engagement and upvotes, downloads, ratings, reviews.

Relevance is something you control directly. Authority is earned over time, and it will keep mattering even as platforms change their ranking details.

## Part A: Reddit

### Step 1: Find Threads That Rank for Target Keywords

1. For each keyword, search Google (private window, target country) and note any reddit.com results, their position, and whether the answer in the thread is current.
2. Search Reddit itself for the keyword and close variants, sorted by relevance and recent, and note the subreddits.
3. Record for each thread: URL, subreddit, age, upvotes, comment count, whether the thread is locked or archived, the question asked, the best existing answers, and any brand mentions (including competitors).
4. Prioritize threads that already rank on page one, are less than ~2 years old or still active, and ask a question your product genuinely helps with.
5. Use `scripts/fetch_page.py` for thread text, or the Reddit interface in a browser, within Reddit's terms. Do not scrape at volume.

### Step 2: Read the Rules Before Anything Else

For each subreddit, read the sidebar, rules, and pinned posts. Note: self-promotion limits (often a ratio of non-promotional to promotional activity), link rules, flair requirements, minimum account age or karma, and whether product mentions are allowed at all. If the rules prohibit the activity, the subreddit goes on a "do not post" list.

Reddit also expects each user to follow its content policy, including rules against spam and vote manipulation. Check current policy text before drafting.

### Step 3: Contribute Genuinely

- Use an account openly tied to the brand or a real person at the brand, with profile text that discloses affiliation. If the account is personal, say so in the comment ("I work on [product]").
- Answer the actual question first. A reader should get a useful answer without clicking anything.
- Start the answer with a natural sentence that includes the keyword where it reads normally. Do not force it.
- Mention the product only where it fits, alongside honest alternatives and trade-offs, with the disclosure line.
- Build history: participate in the community in non-promotional ways (answers, feedback) so the account is credible before any product mention.
- Keep a ratio the subreddit allows; many communities expect mostly non-promotional contributions.
- Reply to follow-ups, correct mistakes, and edit with clear markers.

Draft structure for a reply: one-sentence answer with the keyword, 2-4 lines of reasoning or steps, optional disclosure and product mention, an offer to answer follow-up questions.

### Step 4: Own Community or Brand Posts

Where it is allowed:

- A brand-run subreddit with real value (support, feedback, releases). Titles start with the keyword phrase when natural, for example `Meeting timer feedback thread: ...`.
- Announcement or AMA posts approved under the subreddit's rules or by moderators in advance (message the mods and ask).
- Reddit ads are a separate channel and out of scope here.

### Step 5: Reject Parasite and Manipulative Tactics

These are excluded entirely, and drafts will not include them:

- Parasite SEO: renting or exploiting a high-authority domain or someone else's community to rank content that does not belong there, and pages built mainly to ride platform authority.
- Vote manipulation: buying, trading, or coordinating upvotes.
- Sockpuppets and undisclosed brand ambassadors: fake users, paid posters who hide the affiliation, or rotating accounts to simulate consensus.
- AI-generated comment farms and link dropping.
- Hijacking unrelated threads or replying to old threads only to place a link.

Consequences include bans, domain blacklists, removed content, and loss of trust, and they can undermine the brand's presence in AI answers that draw on these discussions. They also run against Reddit rules and, for undisclosed endorsements, FTC guidance.

### Step 6: Measure

Track per thread: whether the contribution is still live, upvotes, replies, referral clicks (UTM-tagged links where allowed), and whether the thread still ranks. Review at 2, 4, and 8 weeks. Reddit visibility in Google is volatile.

## Part B: App Stores

App store search is buying-intent: people searching a store usually want to install. Treat the listing as a landing page.

### Step 1: Research

1. Search each keyword in the store (Apple and Google Play separately). Record the top 10 apps: title, subtitle or short description, rating, ratings count, update date.
2. Note which variants competitors use in names and subtitles, and which phrases appear in top listings' descriptions.
3. Estimate competition: strong rating counts and frequent updates mean tougher fights.

### Step 2: Fields and Placement

| Field | Apple App Store | Google Play |
|---|---|---|
| Name/title | Keyword first, brand last or after a separator. Count characters against the current limit. | Same approach; check current limit. |
| Subtitle / short description | Variants and benefits; do not repeat words already in the title. | Short description: the main promise, with the keyword near the start. |
| Keyword field | Comma-separated, no spaces after commas, no repeats from title and subtitle, no competitor trademarks. | Not a separate field; Play indexes the long description, so keywords belong there. |
| Description | Written for people first; Apple does not index the description for search, so the benefit is conversion. | Long description is indexed: natural repetition of the key phrase and variants, no stuffing. |
| Screenshots and captions | Text overlays state benefits; caption text can mirror the keyword naturally. | Same; use an icon and feature graphic that match the promise. |
| Ratings and reviews | Prompt through the platform's rating API at a good moment. | Prompt through the in-app review API. |

Field limits and indexing rules change. Check current developer documentation before finalizing any count.

### Step 3: Ratings and Reviews Within Policy

- Ask for a rating after a positive moment (a completed task), using the official in-app prompt APIs, and not on every launch.
- Do not offer rewards for positive ratings, gate the prompt by sentiment, or write or buy fake reviews. Both stores prohibit this.
- Respond to reviews, especially negative ones, with specific help.

### Step 4: Localization

- Localize the title, subtitle, keyword field, and screenshots for each market where there is real demand, using local search terms and not literal translation. Apple lets a localization in one market carry keywords for related locales, so check current behavior before duplicating terms.
- Have a native speaker review translated copy.

### Step 5: Track and Iterate

- Record keyword rank in the store (Apple Search Ads keyword data, Play Console search terms, or an ASO tool if the client has one), impressions, conversion rate, and installs by keyword.
- Change one field family at a time (name, then subtitle, then screenshots) and log it using the `publish-and-track` change log format. Allow 2-4 weeks per change.
- For Google results, a web landing page for the app can also rank; hand off to `bofu-landing-page`.

## Guardrails

- Everything is a draft for human review. The skill does not post, vote, submit listings, or pay for anything.
- Disclose affiliation in every Reddit contribution and profile. No sockpuppets, no purchased upvotes, no paid hidden promotion.
- Follow every subreddit's rules and Reddit's content policy. Respect moderator decisions.
- Listings describe only features the app has. No fabricated ratings, awards, downloads, or reviews, and no competitor trademarks in keyword fields.
- Mark unknown facts `[NEEDS SOURCE]` or `[CLIENT TO CONFIRM]`.
- Do not scrape platforms at volume or bypass rate limits.

## Output

1. **Platform target list:**

| Platform | Target | Keyword | Why it matters (SERP position, volume, relevance) | Rules/constraints | Priority |
|---|---|---|---|---|---|

2. **Reddit drafts:** per thread, reply text with the disclosure line, plus subreddit rule notes.
3. **Listing copy:** per store and locale: name, subtitle or short description, keyword field, description, screenshot caption ideas, with character counts.
4. **Tracking sheet:** item, change date, baseline, check dates, observed rank and installs.

## Next Step

- Keyword source: `bofu-keyword-research`
- Landing page for the product or app: `bofu-landing-page`
- Authority signals beyond the platform: `authority-campaign`, `linkbuilding`
- Reviews: `review-amplification`
- Video listing assets: `video-seo`
- Overall sequencing: `bofu-playbook`
