#!/usr/bin/env python3
"""
Schema validator — extracts and validates JSON-LD schema.org markup.

Returns per-page findings and a site-level summary usable by the
aeo-audit Phase 2 schema subagent.

Usage:
    python schema_validator.py <url>
    python schema_validator.py --urls url1,url2,url3 --output schema.json
"""

import argparse
import json
import re
import sys

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: install: pip install requests beautifulsoup4 lxml --break-system-packages",
          file=sys.stderr)
    sys.exit(1)


# Priority schemas for AEO, with required and recommended properties
SCHEMA_REQUIREMENTS = {
    "Organization": {
        "required": ["name", "url"],
        "recommended": ["logo", "sameAs", "description", "foundingDate", "address",
                        "contactPoint", "knowsAbout"],
    },
    "LocalBusiness": {
        "required": ["name", "address", "telephone"],
        "recommended": ["geo", "openingHoursSpecification", "priceRange",
                        "aggregateRating", "sameAs"],
    },
    "Person": {
        "required": ["name"],
        "recommended": ["jobTitle", "worksFor", "sameAs", "knowsAbout",
                        "alumniOf", "hasCredential"],
    },
    "WebSite": {
        "required": ["url", "name"],
        "recommended": ["publisher", "potentialAction", "inLanguage"],
    },
    "FAQPage": {
        "required": ["mainEntity"],
        "recommended": [],
    },
    "Article": {
        "required": ["headline", "author", "datePublished"],
        "recommended": ["image", "dateModified", "publisher", "description", "mainEntityOfPage"],
    },
    "BlogPosting": {
        "required": ["headline", "author", "datePublished"],
        "recommended": ["image", "dateModified", "publisher", "description"],
    },
    "NewsArticle": {
        "required": ["headline", "author", "datePublished"],
        "recommended": ["image", "dateModified", "publisher", "description"],
    },
    "Product": {
        "required": ["name"],
        "recommended": ["description", "image", "brand", "offers",
                        "aggregateRating", "review", "sku"],
    },
    "SoftwareApplication": {
        "required": ["name"],
        "recommended": ["applicationCategory", "operatingSystem", "offers",
                        "aggregateRating", "softwareVersion"],
    },
    "Service": {
        "required": ["name", "provider"],
        "recommended": ["serviceType", "areaServed", "offers"],
    },
    "HowTo": {
        "required": ["name", "step"],
        "recommended": ["image", "totalTime", "estimatedCost", "supply", "tool"],
    },
    "BreadcrumbList": {
        "required": ["itemListElement"],
        "recommended": [],
    },
    "Event": {
        "required": ["name", "startDate", "location"],
        "recommended": ["endDate", "description", "organizer", "offers"],
    },
    "VideoObject": {
        "required": ["name", "description", "thumbnailUrl", "uploadDate"],
        "recommended": ["duration", "contentUrl", "embedUrl", "transcript"],
    },
}


def extract_jsonld(url: str) -> dict:
    """Fetch a URL and extract all JSON-LD blocks."""
    try:
        r = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0 (aeo-audit)"},
            timeout=30,
        )
        r.raise_for_status()
    except Exception as e:
        return {"url": url, "error": f"Fetch failed: {e}"}

    soup = BeautifulSoup(r.text, "lxml")
    blocks = []
    errors = []

    for script in soup.find_all("script", type="application/ld+json"):
        raw = script.string or script.get_text() or ""
        raw = raw.strip()
        if not raw:
            continue
        try:
            parsed = json.loads(raw)
            blocks.append(parsed)
        except json.JSONDecodeError as e:
            errors.append(f"Invalid JSON-LD block: {e}")

    # Flatten @graph containers
    flattened = []
    for b in blocks:
        if isinstance(b, list):
            flattened.extend(b)
        elif isinstance(b, dict) and "@graph" in b:
            flattened.extend(b["@graph"])
        else:
            flattened.append(b)

    return {"url": url, "blocks": flattened, "parse_errors": errors}


def classify_schemas(blocks: list) -> dict:
    """Count schemas by @type."""
    counts = {}
    for b in blocks:
        if not isinstance(b, dict):
            continue
        t = b.get("@type")
        if isinstance(t, list):
            for ti in t:
                counts[ti] = counts.get(ti, 0) + 1
        elif t:
            counts[t] = counts.get(t, 0) + 1
    return counts


def validate_block(block: dict) -> dict:
    """Check a single schema block for required/recommended properties."""
    if not isinstance(block, dict):
        return {"valid": False, "reason": "Not an object"}
    t = block.get("@type")
    if isinstance(t, list):
        t = t[0] if t else None
    if not t:
        return {"valid": False, "reason": "Missing @type"}

    spec = SCHEMA_REQUIREMENTS.get(t)
    if not spec:
        return {"type": t, "valid": True, "note": "Unrecognized type (not validated)"}

    missing_required = [p for p in spec["required"] if p not in block]
    missing_recommended = [p for p in spec["recommended"] if p not in block]

    return {
        "type": t,
        "valid": len(missing_required) == 0,
        "missing_required": missing_required,
        "missing_recommended": missing_recommended,
        "property_count": len([k for k in block.keys() if not k.startswith("@")]),
    }


def analyze_page(url: str) -> dict:
    """Per-page schema analysis."""
    raw = extract_jsonld(url)
    if "error" in raw:
        return raw

    blocks = raw["blocks"]
    counts = classify_schemas(blocks)
    validations = [validate_block(b) for b in blocks if isinstance(b, dict)]

    invalid = [v for v in validations if not v.get("valid", True)]
    has_sameas = any(
        isinstance(b, dict) and b.get("sameAs") for b in blocks
    )

    return {
        "url": url,
        "schemas_found": counts,
        "schema_count": len(blocks),
        "parse_errors": raw["parse_errors"],
        "validations": validations,
        "invalid_count": len(invalid),
        "has_sameAs": has_sameas,
    }


def site_summary(page_results: list) -> dict:
    """Aggregate per-page results into a site-level schema summary."""
    successful = [r for r in page_results if "error" not in r]
    if not successful:
        return {"error": "No pages successfully analyzed"}

    all_types = {}
    for r in successful:
        for t, n in r["schemas_found"].items():
            all_types[t] = all_types.get(t, 0) + n

    homepage = successful[0]  # assumption: first URL is homepage

    # Score dimensions
    foundation_types = {"Organization", "LocalBusiness", "WebSite", "Person"}
    content_types = {"FAQPage", "HowTo", "Article", "BlogPosting", "NewsArticle",
                     "Product", "SoftwareApplication", "Service", "LocalBusiness",
                     "Event", "VideoObject", "BreadcrumbList"}

    foundation_present = set(homepage["schemas_found"].keys()) & foundation_types
    content_present = set(all_types.keys()) & content_types

    foundation_score = min(35, len(foundation_present) * 12)  # out of 35
    content_score = min(30, len(content_present) * 5)         # out of 30

    # Completeness (% of all validations that passed)
    all_validations = []
    for r in successful:
        all_validations.extend(r["validations"])
    if all_validations:
        valid_pct = sum(1 for v in all_validations if v.get("valid", True)) / len(all_validations)
        completeness_score = round(20 * valid_pct)
    else:
        completeness_score = 0

    # Validation (inverse of parse errors)
    total_parse_errors = sum(len(r["parse_errors"]) for r in successful)
    validation_score = max(0, 15 - total_parse_errors * 3)

    total_score = foundation_score + content_score + completeness_score + validation_score

    missing_critical = []
    hp_types = set(homepage["schemas_found"].keys())
    if "Organization" not in hp_types and "LocalBusiness" not in hp_types:
        missing_critical.append("Organization schema on homepage")
    if not homepage.get("has_sameAs"):
        missing_critical.append("sameAs array on Organization (critical for entity graph)")
    if "FAQPage" not in all_types:
        missing_critical.append("FAQPage on any page (high-leverage for AEO)")

    return {
        "score": total_score,
        "sub_scores": {
            "foundation": foundation_score,
            "content": content_score,
            "completeness": completeness_score,
            "validation": validation_score,
        },
        "schemas_site_wide": all_types,
        "foundation_schemas_on_homepage": sorted(foundation_present),
        "content_schemas_present": sorted(content_present),
        "missing_critical": missing_critical,
        "total_parse_errors": total_parse_errors,
        "n_pages_analyzed": len(successful),
    }


def main():
    parser = argparse.ArgumentParser(description="Schema.org validator for AEO audit")
    parser.add_argument("url", nargs="?", help="Single URL")
    parser.add_argument("--urls", help="Comma-separated URLs for site summary")
    parser.add_argument("--output", help="JSON output path")
    args = parser.parse_args()

    if args.urls:
        urls = [u.strip() for u in args.urls.split(",") if u.strip()]
        page_results = [analyze_page(u) for u in urls]
        summary = site_summary(page_results)
        out = json.dumps({"summary": summary, "pages": page_results}, indent=2, default=str)
    elif args.url:
        out = json.dumps(analyze_page(args.url), indent=2, default=str)
    else:
        parser.error("Provide either a URL or --urls")

    if args.output:
        with open(args.output, "w") as f:
            f.write(out)
        print(f"Saved: {args.output}", file=sys.stderr)
    else:
        print(out)


if __name__ == "__main__":
    main()
