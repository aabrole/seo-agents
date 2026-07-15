# Schema & Structured Data Rubric

> Adapted from geo-seo-claude `geo-schema` and marketingskills `schema-markup`.

## Core insight

Schema.org markup (via JSON-LD) is how you tell AI systems what your content *is*, not just what it says. For AEO, priority is different from traditional SEO: AI systems preferentially use schemas that expose structured facts (Organization relationships, FAQ Q&A pairs, HowTo steps, Person credentials).

## Scoring formula

```
Schema_Score = (Foundation_Schema * 0.35)   # Organization, Website, Person
             + (Content_Schema    * 0.30)   # FAQ, HowTo, Article, Product
             + (Completeness      * 0.20)   # Required + recommended properties
             + (Validation        * 0.15)   # No errors, passes Google Rich Results Test
```

---

## 1. Foundation Schema (35%)

Every site should have these minimum schemas on key pages.

### Organization schema (homepage)

Required properties:
- `@type`: Organization (or LocalBusiness, Corporation subtypes)
- `name`: Official brand name
- `url`: Canonical homepage URL
- `logo`: URL to high-res logo (ImageObject)

Strongly recommended:
- `sameAs`: Array of social/authority URLs (LinkedIn, Wikipedia, Wikidata Q-number, Crunchbase, YouTube, Twitter/X)
- `description`: 150-300 char description
- `foundingDate`, `founders` (Person array)
- `address` (PostalAddress)
- `contactPoint` (ContactPoint with email/phone)
- `knowsAbout`: Array of topics (entity-building signal for AI)
- `slogan`: Tagline

**The `sameAs` array is critical for AEO.** This is the single strongest schema-level signal for entity recognition. Claude and ChatGPT use it to connect a brand to its Wikidata Q-number, which is the canonical entity identifier.

### Website schema (homepage)

- `@type`: WebSite
- `url`, `name`
- `publisher`: reference to Organization
- `potentialAction`: SearchAction (if site has search)
- `inLanguage`: BCP 47 language tag

### Person schema (about/author pages)

Required for every named author or founder:
- `@type`: Person
- `name`, `jobTitle`, `worksFor` (Organization)
- `sameAs`: LinkedIn, Twitter, personal site, Wikipedia, ORCID
- `knowsAbout`: Topic array
- `alumniOf`, `award`, `hasCredential` where applicable

---

## 2. Content Schema (30%)

Apply to appropriate pages based on content type.

| Schema | Use on | Key properties |
|---|---|---|
| `FAQPage` | Any page with Q&A | `mainEntity`: array of `Question` with `acceptedAnswer` (Answer). AI systems extract these directly. |
| `HowTo` | Step-by-step guides | `step`: array of `HowToStep` with `text` and optional `image` |
| `Article` / `BlogPosting` / `NewsArticle` | Blog posts, articles | `author` (Person), `datePublished`, `dateModified`, `headline`, `image`, `publisher` |
| `Product` | Product pages | `name`, `description`, `brand`, `offers` (Offer with price), `aggregateRating`, `review` |
| `SoftwareApplication` | SaaS product pages | Like Product + `applicationCategory`, `operatingSystem`, `softwareVersion` |
| `Service` | Service pages | `serviceType`, `provider`, `areaServed`, `offers` |
| `LocalBusiness` | Local businesses | Organization + `address`, `geo`, `openingHoursSpecification`, `telephone`, `priceRange` |
| `Event` | Events | `name`, `startDate`, `endDate`, `location`, `organizer` |
| `Recipe` | Food/cooking | `recipeIngredient`, `recipeInstructions`, `cookTime`, `nutrition` |
| `VideoObject` | Video content | `name`, `description`, `thumbnailUrl`, `uploadDate`, `duration`, `contentUrl`, `transcript` |
| `BreadcrumbList` | Any non-home page | `itemListElement`: array of `ListItem` with position and item |

### FAQPage is the highest-leverage content schema for AEO

AI systems directly extract FAQ pairs as potential answers. Implementation tips:
- Natural-language questions (how real users ask, not stuffed keywords)
- Complete, self-contained answers (AI might quote verbatim)
- 5-10 Q&A pairs per page minimum
- Answers 40-60 words each (optimal extraction length)

---

## 3. Completeness (20%)

Check each implemented schema for:
- All Google Rich Results required properties present
- All Google Rich Results recommended properties present
- No empty, placeholder, or obviously wrong values (e.g., "John Doe" in Author)
- Consistent entity references (Organization schema referenced from Article.publisher)

## 4. Validation (15%)

- Zero errors in Google Rich Results Test
- Zero warnings for required properties
- Valid JSON-LD syntax (script tag correctly formatted)
- Schema visible in initial HTML (not JS-injected post-load)
- Schema matches actual page content (not misleading)

---

## Scoring thresholds

| Score | Criteria |
|---|---|
| 90-100 | Complete Organization + Website + Person schemas with rich `sameAs`. Appropriate content schemas on every page type. Zero validation errors. FAQ/HowTo where relevant. |
| 70-89 | Foundation schemas complete. Content schemas on most relevant pages. Minor validation warnings. |
| 50-69 | Foundation schemas present but missing key properties. Content schemas inconsistent. Some validation errors. |
| 30-49 | Basic Organization schema only. No content schemas. Multiple validation errors. |
| 0-29 | No schema markup or severely malformed. |

---

## Priority schema implementations for AEO (in order)

If a site has zero schema, implement in this order:

1. **Organization (homepage)** with complete `sameAs` array including Wikidata Q-number — this is the single highest-leverage addition
2. **Person (for founder + key authors)** with `sameAs` links
3. **FAQPage (on top 5 landing pages)** with 5-10 natural Q&A each
4. **Article/BlogPosting** on all blog content with full author attribution
5. **BreadcrumbList** on all non-homepage pages
6. **Product/Service/SoftwareApplication** based on business type
7. **HowTo** on guide/tutorial content
8. **LocalBusiness** for brick-and-mortar operations
