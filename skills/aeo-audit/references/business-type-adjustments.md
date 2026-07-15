# Business-Type Adjustments

Different business types need different AEO priorities. When Phase 1 detects the business type from homepage signals, apply these adjustments to the audit focus and scoring weights.

## Detection signals

| Business Type | Detection Signals |
|---|---|
| **SaaS** | Pricing page, "Sign up" / "Free trial" CTAs, app.domain.com subdomain, feature comparison tables, integration pages |
| **Local Business** | Physical address on homepage, Google Maps embed, "Near me" content, LocalBusiness schema, service area pages |
| **E-commerce** | Product listings, shopping cart, product schema, category pages, price displays, "Add to cart" buttons |
| **Publisher / Media** | Blog-heavy navigation, article schema, author pages, date-based archives, RSS feeds, high content volume |
| **Agency / Services** | Case studies, portfolio, "Our Work" section, team page, client logos, service descriptions |
| **Hybrid** | Combination of above — classify by dominant pattern |

## Type-specific audit adjustments

### SaaS

**Audit focus:**
- Feature comparison tables (high citability)
- Integration pages
- Documentation quality and structure
- API documentation
- Changelog pages
- Knowledge base organization

**Key schemas:**
- `SoftwareApplication` (primary)
- `FAQPage` on pricing and features
- `HowTo` on tutorial content
- `Review` / `AggregateRating` on product pages

**Live citation test adjustments:**
- Add prompt: "Compare [brand] pricing to [competitors]"
- Add prompt: "Does [brand] integrate with [common tool in category]?"

**Typical AEO-win priorities:**
1. Add `SoftwareApplication` schema with full property set
2. Add FAQPage to every pricing/feature page
3. Build out comparison pages ("[brand] vs [competitor]") with tables
4. Ensure G2/Capterra profiles are complete and linked via `sameAs`

### Local Business

**Audit focus:**
- NAP consistency (Name, Address, Phone) across site, Google Business Profile, directories
- Service area pages
- Location-specific content
- Google Business Profile verification
- Review markup
- Local citations (Yelp, Foursquare, industry-specific directories)

**Key schemas:**
- `LocalBusiness` (with appropriate subtype: Restaurant, Dentist, AutoRepair, etc.)
- `GeoCoordinates`
- `OpeningHoursSpecification`
- `PostalAddress`
- `AggregateRating` with reviews

**Live citation test adjustments:**
- Add prompt: "Best [category] near [city]"
- Add prompt: "[category] open on [day/time]"
- Add prompt: "Recommend a [category] in [neighborhood]"

**Typical AEO-win priorities:**
1. Complete LocalBusiness schema with geo and hours
2. Ensure Google Business Profile is claimed and complete
3. NAP consistency audit across top 20 citations
4. Add location-specific landing pages if serving multiple areas

### E-commerce

**Audit focus:**
- Product description quality (citability of spec content)
- Comparison content ("best [category]" guides)
- Buying guides
- Product schema completeness
- Review aggregation
- FAQ sections on product pages

**Key schemas:**
- `Product` (with Offer, AggregateRating, Review)
- `BreadcrumbList`
- `FAQPage` on high-traffic product pages
- `Organization` at site level

**Live citation test adjustments:**
- Add prompt: "Best [product category] under $[price]"
- Add prompt: "Is [brand's product] worth buying?"
- Add prompt: "[product] reviews"

**Typical AEO-win priorities:**
1. Product schema with complete properties on every PDP
2. Add FAQPage to top 20 product pages
3. Create category buying guides optimized for answer-first structure
4. Get product listed in Wikipedia category lists where eligible

### Publisher / Media

**Audit focus:**
- Article quality, structure, depth
- Author credentials (EEAT-critical)
- Source citation practices
- Content freshness
- Original research/journalism

**Key schemas:**
- `Article` / `NewsArticle` / `BlogPosting`
- `Person` (author) with complete sameAs
- `Organization` (publisher) with editorial policy
- `ClaimReview` if fact-checking

**Live citation test adjustments:**
- Add prompt: "What is the latest on [topic]?"
- Add prompt: "Who reports on [beat/topic]?"
- Test recency — recent articles vs. older

**Typical AEO-win priorities:**
1. Build author pages with full Person schema and credentials
2. Implement editorial standards and publish the policy page
3. Ensure Article schema has datePublished AND dateModified on every post
4. Get pulled into Wikipedia as a reference for relevant topics

### Agency / Services

**Audit focus:**
- Case studies (the most citable agency content)
- Expertise demonstration
- Thought leadership content
- Team credentials
- Client logos and testimonials

**Key schemas:**
- `Organization` with detailed properties
- `Person` for team members with credentials
- `Service` for each offering
- `Review` from clients
- `CaseStudy` (custom, via Article type with specific properties)

**Live citation test adjustments:**
- Add prompt: "Best [service type] agencies for [industry]"
- Add prompt: "Who does [specific service] well?"
- Test competitive positioning heavily

**Typical AEO-win priorities:**
1. Publish 5-10 detailed case studies with named clients, specific outcomes, measurable results
2. Build team pages with Person schema for every member
3. Create "how we do X" thought leadership with methodologies and frameworks
4. Ensure founder/principals have strong personal brand entity graphs

## Scoring weight adjustments

The default composite formula works for most types, but these tweaks help calibrate:

| Business Type | Adjustment |
|---|---|
| SaaS | +5% to Schema weight (SoftwareApplication is heavily weighted by AI systems for SaaS queries) |
| Local | +10% to Technical (GBP signals), +5% to Schema |
| E-commerce | +5% to Schema (Product markup critical) |
| Publisher | +10% to CORE-EEAT (author credentials matter more) |
| Agency | +5% to Brand Authority (thought leadership signals matter more) |

Applied adjustments should be called out in the report methodology section so the client understands why weights differ from a default audit.
