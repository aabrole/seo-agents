---
name: video-seo
description: Use when you want short or long videos to rank for buying keywords on YouTube, Shorts, Instagram Reels, and TikTok, and to surface in Google and AI answers. Produces a per-keyword video brief and a posting plan. Also use when the user mentions "video SEO", "YouTube SEO", "rank a video", "Reels keyword", "TikTok SEO", "video title and description", or "repurpose video".
user-invocable: true
argument-hint: "<target keyword(s) or keyword list> [brand/product] [platforms]"
license: MIT
metadata:
  author: aabrole
  version: "1.0.0"
  category: seo
---

# Video SEO

Turns buying-stage keywords into short, honest videos with titles, descriptions, captions, and chapters built so each platform's search can match them. One recording is repurposed across platforms.

Why this works: every video platform is also a search engine, and few brands optimize for it, so competition for a buying phrase is often thinner than in web results. Google also shows video results (and Shorts, Reels, and TikTok clips) in its main SERPs, and AI answers sometimes cite videos. Relevance on a platform comes mostly from where the keyword sits in the first thing a viewer or crawler reads, and authority comes from engagement rather than backlinks. The trade-off: video rankings are fast and volatile, so this complements ranked web pages rather than replacing them.

## Input

- **Keywords** (required): buying-stage terms, normally the same ones used for landing pages (see `bofu-keyword-research`)
- **Brand/product facts** (required): what it does, who it is for, real differentiators, links
- **Platforms** (optional): default YouTube long-form, YouTube Shorts, Instagram Reels, TikTok
- **Existing assets** (optional): recordings, demos, screen captures, transcripts
- **Competitors** (optional): brands to compare against

## Role

You are a video SEO planner and scriptwriter's assistant. You write the metadata, structure, and brief. The creator records, approves, and posts.

## Step 1: Pick Keywords and Check the Platform SERP

1. Start from the buying keywords already chosen for landing pages: "[tool] for [use case]", "[category] software", "best [category] for [audience]", "[brand] alternative", "[brand] vs [brand]".
2. Search each keyword on YouTube, Instagram, and TikTok. Note what ranks: format (long, short), view counts, channel size, age, and whether the videos actually answer the query.
3. Where available, `scripts/youtube_search.py search "<keyword>"` returns YouTube results (needs a YouTube Data API key and `google-api-python-client`). Use `video <id>` to read title, description, and stats of a competing video.
4. Also search the keyword on Google and note whether a video carousel or video results appear, and which platform they come from. A video SERP feature raises the keyword's priority.
5. Score each keyword: low competition (small channels or low views in the top results, or results that do not answer the query), SERP feature present, and relevance to a product you can show. Keep 5-10 to start.

If the top results are large, well-made videos from big channels, deprioritize the keyword for now.

## Step 2: Choose the Format and Angle

Match the format to intent:

- **Demo or walkthrough** ("how [product] does X"): the default for buying keywords.
- **Comparison** ("[brand A] vs [brand B]", "[brand] alternative"): see Step 7 for rules.
- **Review or results** (first-hand use of a product or service): show the real thing.
- **Short answer** (30-90 seconds): one direct answer plus a clear proof moment.

The video has to answer the keyword within the first few seconds. A clip that is entertaining but off-topic may rank briefly, then drop as viewers click back to results. Use the video to show the product as the solution.

## Step 3: Write the Metadata per Platform

### YouTube long-form

- **Title:** exact keyword at the very start, then a hook or benefit. Aim for under ~70 characters so the keyword is not truncated. Example: `Stopwatch for meetings: a free timer your whole team can share`.
- **Description:** first sentence repeats the keyword near its start and says what the viewer gets. Then write a longer, readable description of 150-300 words in short paragraphs with the keyword's variants used naturally, a link to the relevant landing page, and a short list of resources.
- **Chapters:** timestamps starting at 0:00, at least three, each a short phrase that includes a variant or sub-question where natural.
- **Tags and hashtags:** one to three relevant hashtags; tags carry little weight, so do not spend time there.
- **Thumbnail and on-screen text:** keyword or its core benefit in few words; consistent with the title.
- **Pinned comment:** link to the landing page and a one-line summary.

### YouTube Shorts

- **Title:** same pattern as long-form, keyword first.
- **Description:** first sentence is the keyword sentence. Paste a corrected transcript of the narration as the remainder, proofread and lightly edited. Add one link to the landing page.
- Spoken keyword in the first seconds of narration helps captions and transcripts reinforce the title.

### Instagram Reels and TikTok

There is no title field, so the opening of the caption carries the keyword.

- **Caption:** first sentence starts with the exact keyword and a quotable line. Short paragraphs of one sentence each. Add a transcript-style body or key points, then a call to action.
- **On-screen text:** keyword in the first frame, large enough to read on a phone, matching the caption.
- **Spoken line:** say the keyword in the first few seconds.
- **Hashtags:** a few specific ones (the keyword variant, category). Skip mass tag lists.
- **Alt text and cover text:** fill them in where the platform offers fields.
- Reuse the same caption on Shorts and TikTok with small edits.

## Step 4: Per-Keyword Video Brief

For each keyword, produce:

- Keyword, intent, platform targets, and why this keyword (SERP notes)
- Angle and format, target length, and the one claim the video proves
- Hook line (first 3 seconds) and outline (3-5 beats), including the on-screen proof moment
- Title for YouTube, Shorts, and a placeholder opening line for Reels/TikTok
- First description sentence and description body outline
- Chapters list
- Captions for Reels and TikTok (openers differ slightly per platform)
- Thumbnail text idea and first-frame text
- Landing page link and call to action
- Fact sources (`[NEEDS SOURCE]` for any claim not provided)

## Step 5: Multiple Videos per Keyword

Unlike web pages, several videos can target the same keyword, and more than one can rank. Platforms test videos against each other and favor recent, well-performing ones.

- Plan 3-5 videos per priority keyword with different angles: demo, use case, comparison, myth, results.
- Vary the exact keyword wording slightly across videos (plural, order, close variants).
- Do not mass-produce near-duplicate or automated low-quality clips. Videos with no engagement tend to fall out of results, and low-quality repetition can hurt the channel.
- Post on a steady cadence the creator can sustain; consistency beats bursts.

## Step 6: Repurpose One Recording

1. Record one 5-10 minute demo or conversation as the master.
2. Cut a long-form YouTube version, then 2-4 vertical clips from it, each built around one keyword variant.
3. Rewrite the opening line and caption per platform from the brief; do not copy the long description into captions unchanged.
4. Cross-posting tools exist but platform rules change; follow each platform's terms, and have the human approve before anything is scheduled. Keep watermarks from other platforms off the upload.
5. Track each clip by its keyword and platform in the posting plan.

## Step 7: Competitor and Comparison Videos, Done Fairly

- Say what the video compares and on which criteria. Use only facts you can verify (pricing pages, feature docs) and cite them in the description.
- Show competitor products accurately, with no edited-to-mislead footage, and no claims you cannot support.
- Mention brand names in titles factually, in the way a viewer would search. Do not imply endorsement or affiliation. Disclose your own relationship to the product you favor.
- Include where the competitor is the better fit. This builds trust and retention.
- Check platform advertising and comparison rules, and for regulated claims have the client's legal contact review.
- Mark unverified comparisons `[NEEDS SOURCE]` and leave them out until confirmed.

## Step 8: Measure

- Platform analytics: impressions, click-through rate, average view duration, retention, search as a traffic source, and which queries bring views (YouTube Studio).
- Google: check whether the video appears for the keyword (desktop and mobile, since layouts differ) and record it in the tracking sheet weekly.
- Site: referral clicks to the landing page in GA4 (UTM-tag the description links), and assisted conversions.
- Volatility is normal. Positions can swing within days, hold for months, or vanish. Judge over 4-6 weeks, not day to day.
- Retire or rework videos with high impressions and poor retention; double down on those with strong retention.
- For AI visibility, see `geo-brand-mentions` to check whether videos are cited.

## Guardrails

- Only claim what the creator can show or source. No fabricated reviews, results, or stats.
- No fake accounts, bought views, bought engagement, or engagement pods.
- Disclose sponsorships, affiliate links, and material relationships as platform rules and FTC guidance require.
- Respect copyright for music, footage, and screenshots; use licensed or original assets.
- The skill drafts and plans. The human records, uploads, and publishes.
- Keep metadata honest: the title and caption must match the content, and clickbait that the video does not deliver on is excluded.

## Output

1. **Keyword shortlist:** keyword, platform SERP notes, competition, priority.
2. **Per-keyword video briefs** (Step 4 fields).
3. **Posting plan:**

| Week | Keyword | Video | Platform | Format | Title / opener | Link target | Status | Result (views, rank seen) |
|---|---|---|---|---|---|---|---|---|

4. **Measurement notes:** what to review weekly and at 4-6 weeks.

## Next Step

- More keywords: `bofu-keyword-research`
- Landing page for the link target: `bofu-landing-page`
- Review clips as social proof: `review-amplification`
- AI answer visibility: `geo-brand-mentions`, `aeo-audit`
- Full sequence: `bofu-playbook`
