# Press Kit

A press kit is a single, crawlable page (or small section) with everything a writer, podcast host, event organizer, or AI crawler needs to describe the brand accurately. It saves journalists time, so they use your preferred wording and link to the right page. It also gives retrieval systems one clean, authoritative source of brand facts.

## Where it lives

- **Standard version:** a page on the main domain, such as `/press` or `/press-kit`, linked from the site footer with the anchor text "Press kit" or "Press". Linking from the footer puts it one click from every page and lets crawlers find it.
- **Fast version:** a shared folder (cloud storage or similar) with the assets, linked from a short page or from outreach emails. Use this if the site cannot be changed this week, then upgrade to a page later.
- Hand page building to `write-content` and `site-architecture` if a template is needed; schema to `schema-markup`.

## Contents

1. **Boilerplate:** the "About" paragraph in 3 lengths (25, 50, 100 words), written in plain language. Matches the text used in releases, directories, and podcasts.
2. **Fact sheet:** legal name, founding date, headquarters, founders, number of employees (only if public), product list, pricing model, markets served, URL list. Unknowns marked `[CLIENT TO CONFIRM]` until resolved.
3. **Founder and expert bios:** short and long versions, a headshot, links to professional profiles. Credentials must be verifiable.
4. **Logos:** SVG and PNG, light and dark backgrounds, with clear-space and usage rules, and a note on what not to do (stretching, recoloring).
5. **Product screenshots and images:** high resolution, with captions and alt text. Include at least one hero image and 3 to 5 product views.
6. **Brand details:** brand colors (hex), fonts, and naming rules (how to write the brand name).
7. **Media contact:** a named person, email, phone, and expected response time.
8. **Coverage:** a list of published mentions with outlet, date, and link. Only real, verified items. Update monthly from the tracker.
9. **Press releases and news:** archive of releases with dates.
10. **Downloads:** a ZIP of assets, plus a plain-text file of boilerplate and the fact sheet for easy copy and paste.
11. **FAQ (optional):** 5 to 8 questions journalists commonly ask (what the company does, how it is funded if public, how customers are served), answered factually.

## On-page and technical details

- **Title and H1:** "[Brand] Press Kit" and a short description in the meta description.
- **Alt text** on every image: describe what it shows and include the brand name where natural, for example "Dashboard view of [Brand] scheduling app". No keyword stuffing.
- **File names:** descriptive, lowercase, hyphenated (`brand-logo-dark.svg`).
- **OG image and social metadata:** set Open Graph and Twitter card tags so shared links display a clean preview.
- **Crawlability:** make sure the page is indexable (no noindex), included in the sitemap, linked in the footer, and its text is in HTML rather than inside images or PDFs. Provide PDFs as extra downloads, not the only version.
- **Schema:** Organization schema on the page or site-wide, with `sameAs` links to official profiles; Person schema for founders where appropriate (see `schema-markup`).
- **Download links:** direct links that work without a form. Do not gate assets behind an email wall.
- **Page weight:** keep image previews compressed; provide full-resolution files in the ZIP.
- Keep the page current. An out-of-date logo or old pricing gets copied by writers and AI answers alike.

## Why it helps

- Journalists and hosts pick the easiest source. A complete kit means correct names, logos, and links.
- Link anchors in the coverage list and the boilerplate are under your control, because writers copy them.
- LLM research and search answers often draw from clear, consistent brand pages. A single canonical source reduces conflicting or hallucinated brand facts.
- Press kit links become a natural target for press mentions, directories, and podcast show notes.

## Workflow

1. Gather inputs from the brand fact sheet and asset folder. List gaps and ask the client.
2. Draft the page copy and file list. Mark unconfirmed items.
3. Client approves every claim and image.
4. Developer or the client publishes the page; add the footer link.
5. Verify: page loads, indexable, in sitemap, images have alt text, downloads work, OG preview renders. Use `seo-technical` or a quick fetch to confirm.
6. Add the URL to every outreach template, release, directory profile, and podcast pitch.
7. Review quarterly and after every new coverage item or rebrand.

## Tracker entry

Log: page URL, status, publish date, footer link confirmed, last update date, and owner. Use it as the target page for "press kit" anchors in directories and bios.
