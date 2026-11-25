---
name: bofu-hub-pages
description: Use when bottom-of-funnel pages need to be discoverable: builds or audits hub pages (/uses/, /solutions/, /alternatives/, /services/, /industries/), footer links, click depth and internal links so every buying-intent page is within 2-3 clicks of home. Also use when the user mentions "hub page", "orphan pages", "click depth", "footer links", "internal linking for landing pages", or "information architecture for BOFU".
user-invocable: true
argument-hint: "<site URL or crawl export> [list of BOFU pages]"
license: MIT
metadata:
  author: aabrole
  version: "1.0.0"
  category: seo
---

# BOFU Hub Pages

Makes sure the buying-intent pages you build can be found. A hub page is a category index that lists related landing pages, is linked from the site-wide footer, and keeps each landing page about two clicks from the homepage.

Why this works: crawlers and users judge importance partly by how easily a page is reached. A page linked from nowhere, or buried five clicks deep, signals that the site does not care about it. A hub gives every landing page a strong, crawlable parent, groups related keywords so the category context is clear, and gives visitors a way to browse to the page that fits their case.

## Input

- **Site** (required): URL, or a crawler export (Screaming Frog or similar, HTML pages only, with crawl depth and inlinks columns).
- **BOFU page list** (required): URLs, H1s and primary keywords of the pages that should rank. If it does not exist yet, take it from `bofu-keyword-research` and `bofu-landing-page`.
- **Navigation facts**: how the header and footer are edited in this CMS, and who can change them.

## Role

You are an information architect for a site that sells something. You design the smallest set of hub pages that makes every landing page reachable, and you do not restructure the rest of the site.

## Step 1: Orphan check

An orphan is an indexable page with zero internal links pointing to it. A page listed only in the XML sitemap counts as an orphan: the sitemap helps discovery but does not pass the signal that the site links to it.

How to check:

1. Get the full URL list from three sources: the XML sitemap, a crawl that follows links from the homepage, and (optionally) GSC pages with impressions.
2. Orphans = URLs in the sitemap or GSC that the link crawl did not reach, or crawl rows with inlinks = 0.
3. For a single page, save the HTML of its would-be parents and run `claude-seo run parse_html.py <file> --url <base URL>` to confirm the link exists in the rendered markup, not only in a script or an image map.

Every BOFU page needs at least one link from a hub and one or more from related pages (Step 7). Fix orphans before any other work in this skill.

## Step 2: Click depth target

Click depth is the minimum number of link hops from the homepage (home = 0).

| Depth | Verdict for a BOFU page |
|---|---|
| 1 | Fine for the few highest-value pages (can be linked directly in the footer or header) |
| 2 | Target. Footer or header > hub > page |
| 3 | Acceptable |
| 4 or more | Risk. Add a link from a shallower page or a new hub |

Read depth from the crawler's crawl-depth column. If you only have a URL list, build the link graph from `parse_html.py` outputs and compute the shortest path yourself. Pagination of blog archives is the one place where depth is expected to climb; do not use paginated lists as the only route to a landing page.

Competitor check (optional): crawl 1-2 competitors that rank for your keywords and note the depth of the pages that outrank you.

## Step 3: Choose hub types

Pick hubs by what the business sells and how searchers phrase the need.

| Hub | URL | Fits |
|---|---|---|
| Uses | /uses/ | Software or products found by use case ("invoice software for freelancers") |
| Solutions | /solutions/ | Products or services sold by problem or goal |
| Services | /services/ | Service businesses, often by service and location |
| Alternatives | /alternatives/ | Pages targeting "[competitor] alternative" keywords |
| Industries | /industries/ | The same offer sold to different sectors or audiences |

A site can have several hubs. Use the folder as the parent: `/uses/free-task-management-software`, not a flat root URL. Name the hub plainly (title "Uses | Brand" beats "Explore the many ways to use our platform") so the hub name gives context to every keyword listed under it.

Do not create a hub for fewer than about 5 pages. Until then, link the pages from the footer or a relevant parent page.

## Step 4: Design the hub layout

Top to bottom:

1. **H1**: the hub name, in plain words ("Solutions", "Invoice Software Uses", "Alternatives").
2. **Intro of 1-2 sentences** that restates the outcome the visitor wants, in the visitor's terms, and says what the list below is.
3. **H2 category groups**, each with a short descriptive name that gives context to the pages under it.
4. **Bulleted links** under each group, using each linked page's H1 as the anchor text by default. Vary the wording only when two H1s would otherwise read as identical.
5. **CTA at the bottom**, the same action the landing pages use.

Style it as a real page: spacing, readable list, brand styling, a hero if the template has one. A bare list of links dumped on a blank page looks like a link farm to both visitors and reviewers.

### Intro copy examples (fictional brands)

| Hub | Intro |
|---|---|
| /uses/ (TallyLeaf, invoicing) | Get paid on time without a spreadsheet. These are the most common ways freelancers, studios and small teams use TallyLeaf to invoice. |
| /solutions/ (HarborDesk, helpdesk) | Answer customers faster with less manual sorting. Pick the support problem you are trying to solve to see how HarborDesk handles it. |
| /services/ (BlueCopper Plumbing) | Fix a leak, a blocked drain or a boiler fault without waiting days. These are the repairs we handle across Leeds, with callout details for each. |
| /alternatives/ (RiseForm, standing desks) | Comparing options before you buy? These pages set RiseForm next to other desks on height range, motor type, and price. |
| /industries/ (LexaVerse, translation) | Legal, medical and technical text each need different checks. Choose your field to see how LexaVerse handles it. |

Each intro is true to the offer, short, and free of claims you cannot support.

## Step 5: Group and order

Grouping:

- 3-8 groups per hub, each with 3-10 links. Group by the visitor's mental model (problem, function, audience), not by your internal team structure.
- A page lives in one primary group. Cross-listing is allowed for pages that truly fit two groups, but keep it rare.

Ordering inside a group:

1. Highest buying intent and highest demand first (use GSC impressions, Ahrefs volume or the priority from `bofu-keyword-research`).
2. Most relevant to the group heading next.
3. Do not stack near-duplicates. If three links differ only by a modifier, put them apart or merge the pages.
4. New or low-demand pages go at the bottom of their group.

Re-sort when rank tracking and GSC show which pages convert.

## Step 6: Footer and header links

- Link each hub from the site-wide footer (a "Resources", "Solutions" or "Explore" column) so it is one click from every page. The header is optional, and fits a hub that is also a main navigation item.
- The few pages that matter most commercially can be linked in the footer directly. Keep the footer list short, around 5-8 landing links, or it becomes a link block that nobody reads.
- Links are plain HTML anchors, not buttons that need JavaScript to navigate, and not hidden in a collapsed element that only renders after interaction.
- Do not link the same landing page from many footer positions with different anchors.

## Step 7: Internal links from related pages

Each BOFU page needs links in as well as out.

- From the hub (required).
- From 2-3 closely related landing pages ("Related uses" or a short "Also used for" block). Anchor with the linked page's H1 or a natural variant.
- From relevant blog or help content, where the mention reads naturally.
- From the homepage or a main category page for the top few pages.
- From the page back to its hub with a breadcrumb or a "All uses" link, which also supports BreadcrumbList schema (hand to `schema-markup`).

Avoid mass auto-linking every page to every other page. Link where the visitor would plausibly want to go next.

## Step 8: When to split a hub

Split when:

- A hub has more than roughly 40-50 links, or groups of more than 10, so scanning becomes hard.
- One group has its own audience or search demand (for example "/industries/healthcare/" with 12 pages).
- Two distinct page types are mixed (use cases and competitor pages), which want different hubs.

How: promote the big group to a sub-hub (`/uses/accounting/`), keep the parent hub listing the sub-hub with a short description plus the top 3-5 pages, and check depth again, because a sub-hub adds a click. A BOFU page under a sub-hub is then depth 3, which is the acceptable limit.

## Step 9: Audit an existing site

1. Export a crawl (HTML, status 200, indexable) with columns for URL, title, H1, crawl depth, inlinks, word count. If you only have pages as files, run `scripts/parse_html.py` on each and collect links.
2. List every BOFU page (by folder or by a list from the client).
3. Flag by rule:
   - inlinks = 0: orphan (Step 1).
   - depth >= 4: too deep. Depth 3: note.
   - no hub parent: needs a hub or an existing one.
   - hub with a mix of unrelated pages, or more than 50 links: restructure (Step 8).
   - links using non-descriptive anchors ("click here", "learn more") to BOFU pages: rewrite.
4. Check that footer and header links appear in the crawled HTML (not injected late by a script the crawler did not render). If the crawler shows depth 1 for everything, you probably have a mega-menu or footer inflating the numbers; check it matches what a user can actually see.
5. Produce the fix list in the Output format below.

If indexing or crawl problems remain after links are fixed (blocked paths, canonicals, soft 404s), hand off to `seo-technical`. For XML sitemap composition hand off to `seo-sitemap`.

## Guardrails

- Hubs list real pages that exist and are useful. Do not create hubs of thin or duplicate pages to inflate links.
- Do not hide links (white text, off-screen, display none) or build link lists for crawlers only.
- Do not restructure existing URLs without a redirect plan (301 old to new, update internal links, update the sitemap). Get approval before moving indexed pages.
- Hub and footer edits are drafted for the site owner to approve and publish.

## Output

**1. Findings table**

| URL | Depth | Inlinks | Hub parent | Issue | Fix |
|---|---|---|---|---|---|

**2. Hub spec (one per hub)**

```
Hub URL:
Title:
H1:
Intro (1-2 sentences):
Groups:
  H2 name: list of pages in order (anchor text = H1, URL)
Bottom CTA:
Footer placement:
Related-page links to add (from, to, anchor):
```

**3. Summary**: count of orphans, pages by depth (1, 2, 3, 4+), hubs to create, hubs to split, and the order to ship the fixes (orphans first, then hub creation, then footer links, then related links).

See `references/hub-page-template.md` for a filled example.

## Next Step

- Full-site structure, navigation and URL design: `site-architecture`.
- XML sitemap issues: `seo-sitemap`. Crawl, index and canonical issues: `seo-technical`.
- Write or improve the landing pages that sit under the hubs: `bofu-landing-page`.
- Structured data for breadcrumbs: `schema-markup`.
- Index and track the new hubs: `publish-and-track`.
