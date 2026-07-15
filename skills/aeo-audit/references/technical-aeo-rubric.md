# Technical AEO Rubric (Infrastructure for AI Crawlers)

> Adapted from geo-seo-claude `geo-technical` and seo-geo-claude-skills technical-seo-checker.

## Core insight

If AI crawlers can't fetch, render, or parse the site, nothing else matters. Technical AEO is the *prerequisite* layer — a score here below 70 makes every other dimension moot.

## Scoring formula

```
Technical_AEO_Score = (AI_Crawler_Access  * 0.30)
                    + (llms_txt_Quality   * 0.20)
                    + (Rendering          * 0.20)
                    + (Performance        * 0.15)
                    + (Meta_Hygiene       * 0.15)
```

---

## 1. AI Crawler Access (30%)

**What to check in robots.txt:**

Must be explicitly allowed (or not blocked) for these user agents:

| Crawler | Used by | Priority |
|---|---|---|
| `GPTBot` | OpenAI training | Critical |
| `ChatGPT-User` | ChatGPT browsing | Critical |
| `OAI-SearchBot` | ChatGPT Search | Critical |
| `ClaudeBot` | Anthropic training | Critical |
| `Claude-Web` | Claude browsing | Critical |
| `PerplexityBot` | Perplexity indexing | Critical |
| `Perplexity-User` | Perplexity live queries | Critical |
| `Google-Extended` | Gemini training | Critical |
| `CCBot` | Common Crawl (feeds many models) | High |
| `Applebot-Extended` | Apple Intelligence | High |
| `Bytespider` | TikTok/Doubao | Medium |
| `cohere-ai` | Cohere | Medium |
| `Diffbot` | Diffbot Knowledge Graph | Medium |

**Scoring:**

| Score | Criteria |
|---|---|
| 90-100 | All critical AI crawlers explicitly allowed; robots.txt well-formed; no overly broad `Disallow: /` blocks |
| 70-89 | Most critical crawlers allowed, 1-2 unintentionally blocked |
| 50-69 | Half of critical crawlers blocked; likely default CMS config |
| 30-49 | Most AI crawlers blocked or no explicit rules (defaults may allow but risk is high) |
| 0-29 | All AI crawlers blocked, or `Disallow: /` domain-wide |

**Critical issue flags:**
- Disallow: / with no User-agent exception — blocks everything
- Blocking `GPTBot` while allowing Googlebot — explicitly opting out of ChatGPT
- robots.txt returns 404 or 5xx — undefined behavior, usually treated as allow

---

## 2. llms.txt Quality (20%)

**What is llms.txt?** A proposed standard (2024, Answer.AI) for giving AI agents a curated index of a site's most important content. Similar to robots.txt but *positive* — it lists what you want AI to see.

**What to check:**
- File exists at `/llms.txt` (domain root)
- Well-formed (starts with `# [Site Name]`)
- Lists key pages with descriptions
- Includes sitemap reference
- Updated recently (within 90 days)

**Scoring:**

| Score | Criteria |
|---|---|
| 90-100 | Complete llms.txt with 20+ curated URLs, clear descriptions, recent update, well-organized sections |
| 70-89 | llms.txt exists with 10-19 URLs, basic descriptions |
| 50-69 | llms.txt exists but minimal (under 10 URLs) or outdated |
| 30-49 | Malformed llms.txt or placeholder only |
| 0-29 | No llms.txt |

**Bonus:** presence of `llms-full.txt` (full text dump) is a positive signal.

---

## 3. Rendering (20%)

AI crawlers vary in JavaScript execution capability. Pure client-side rendered (CSR) SPAs are invisible to most.

**What to check:**
- Fetch the page with JS disabled (simulate AI crawler). Is the main content present?
- Is the page server-side rendered (SSR), static-site generated (SSG), or uses dynamic rendering?
- Are critical metadata (title, description, Open Graph, JSON-LD) in the initial HTML?
- Is there a meaningful `<noscript>` fallback?
- If using React/Vue/Svelte: Next.js, Nuxt, SvelteKit, or static export?

**Scoring:**

| Score | Criteria |
|---|---|
| 90-100 | Full SSR or SSG. All content, metadata, structured data in initial HTML. Works with JS disabled. |
| 70-89 | Hybrid (SSR for critical pages + CSR for interactive). Critical content in initial HTML. |
| 50-69 | Partial SSR. Some pages render server-side, others don't. |
| 30-49 | CSR with basic prerendering for bots (user-agent sniffing). Fragile. |
| 0-29 | Pure CSR SPA. Empty HTML shell with all content injected via JS. AI crawlers see nothing. |

**Critical issue flag:** Pure CSR SPA detected — this is a showstopper. Recommend migration to Next.js SSR/SSG, Nuxt, or at minimum static prerendering.

---

## 4. Performance (15%)

AI crawlers have timeouts. Slow sites get less content indexed.

**What to check (use Lighthouse or equivalent):**
- Largest Contentful Paint (LCP) — target < 2.5s
- Cumulative Layout Shift (CLS) — target < 0.1
- Time to First Byte (TTFB) — target < 800ms
- Total page size — target < 1.5MB
- Number of requests — target < 80

**Scoring:**

| Score | Criteria |
|---|---|
| 90-100 | All Core Web Vitals pass. TTFB < 500ms. Lightweight pages. |
| 70-89 | Most CWV pass. TTFB < 1s. Page weight acceptable. |
| 50-69 | Some CWV fail. TTFB 1-2s. |
| 30-49 | Multiple CWV fail. TTFB > 2s. Heavy pages. |
| 0-29 | Performance disaster. Pages timeout or fail to render for crawlers. |

---

## 5. Meta Hygiene (15%)

Basic technical sanity that AI crawlers rely on for context.

**Check per page:**
- `<title>` present, unique, 30-60 characters
- `<meta name="description">` present, 120-160 characters
- `<link rel="canonical">` self-referencing or appropriate
- `<html lang="...">` declared
- Open Graph tags (og:title, og:description, og:type, og:image)
- Twitter Card tags
- No `<meta name="robots" content="noindex">` on indexable pages
- Proper HTTP status codes (200 for content, 301 for redirects, 404 for missing)
- HTTPS throughout (no mixed content)
- Valid sitemap.xml

**Scoring:**

| Score | Criteria |
|---|---|
| 90-100 | All meta elements present and well-formed across sampled pages. Valid sitemap. HTTPS clean. |
| 70-89 | Minor gaps (a few pages missing descriptions, etc.) |
| 50-69 | Inconsistent meta coverage. Some duplicate titles/descriptions. |
| 30-49 | Major gaps. Missing titles, broken canonicals, mixed content. |
| 0-29 | Meta metadata missing or broken site-wide. |

---

## Quick checklist (for fast triage)

- [ ] robots.txt fetches successfully
- [ ] robots.txt allows GPTBot, ClaudeBot, PerplexityBot
- [ ] llms.txt exists at `/llms.txt`
- [ ] Homepage HTML contains main content with JS disabled
- [ ] Homepage has valid `<title>`, `<meta description>`, canonical
- [ ] Homepage returns 200
- [ ] HTTPS with valid cert
- [ ] sitemap.xml exists and is current
- [ ] No domain-level noindex
- [ ] Core Web Vitals passing (LCP < 2.5s)

Any unchecked box = surface in report. Multiple unchecked = "Critical" severity.
