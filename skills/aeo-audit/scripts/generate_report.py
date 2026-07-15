#!/usr/bin/env python3
"""
Generate final AEO audit report from raw phase data.

Expected input files (all optional — graceful degradation):
    --live-citation     live citation test JSON
    --citability        citability scorer site output JSON
    --schema            schema validator site output JSON
    --brand-authority   brand authority findings JSON (produced by subagent)
    --technical         technical AEO findings JSON (produced by subagent)
    --core-eeat         CORE-EEAT findings JSON (produced by subagent)

    --brand, --url, --category    basic metadata
    --output-md    path for markdown report (default: AEO-AUDIT-REPORT.md)
    --output-json  path for raw data aggregate (default: AEO-AUDIT-DATA.json)

If a subagent output is missing, its section in the report is stubbed with a note.
The composite score is computed from available dimensions, with weights
renormalized to sum to 1 across what's present.
"""

import argparse
import json
import os
import sys
from datetime import datetime

DEFAULT_WEIGHTS = {
    "live_citation":    0.15,
    "citability":       0.20,
    "brand_authority":  0.20,
    "core_eeat":        0.20,
    "technical":        0.15,
    "schema":           0.10,
}


def load_json(path):
    if not path or not os.path.isfile(path):
        return None
    try:
        with open(path) as f:
            return json.load(f)
    except Exception as e:
        print(f"WARN: failed to load {path}: {e}", file=sys.stderr)
        return None


def rating_from_score(s):
    if s >= 90:
        return "Excellent"
    if s >= 75:
        return "Good"
    if s >= 60:
        return "Fair"
    if s >= 40:
        return "Poor"
    return "Critical"


def compute_composite(scores: dict) -> dict:
    """Composite score with renormalized weights based on available dimensions."""
    available = {k: v for k, v in scores.items() if v is not None}
    if not available:
        return {"score": 0, "weights_used": {}, "rating": "Unknown"}

    total_weight = sum(DEFAULT_WEIGHTS[k] for k in available.keys())
    normalized = {k: DEFAULT_WEIGHTS[k] / total_weight for k in available.keys()}
    composite = sum(available[k] * normalized[k] for k in available.keys())
    return {
        "score": round(composite, 1),
        "weights_used": normalized,
        "rating": rating_from_score(composite),
    }


def format_live_citation_section(data):
    if not data:
        return "_Live Citation Test was not run (no API keys configured)._\n"

    scoring = data.get("scoring", {})
    score = scoring.get("composite_score", 0)
    sub = scoring.get("sub_scores", {})
    n_mentions = scoring.get("n_mentions", 0)
    n_total = scoring.get("n_queries_total", 0)

    out = []
    out.append(f"**Score: {score}/100** · Mentions: {n_mentions}/{n_total} across "
               f"{', '.join(data.get('providers_used', []))}\n")

    out.append("### Sub-scores\n")
    out.append("| Prompt type | Score |\n|---|---:|")
    out.append(f"| Name query hit rate | {sub.get('name_query_hit_rate', 0)}/100 |")
    out.append(f"| Category query position | {sub.get('category_query_position_score', 0)}/100 |")
    out.append(f"| Problem query hit rate | {sub.get('problem_query_hit_rate', 0)}/100 |")
    out.append(f"| Comparison framing | {sub.get('comparison_framing_score', 0)}/100 |")
    out.append(f"| Alternative query hit rate | {sub.get('alternative_query_hit_rate', 0)}/100 |")
    out.append("")

    # Representative responses — pick up to 4 most-revealing results
    raw = data.get("raw_results", [])
    representative = [r for r in raw if r.get("response_text") and not r.get("error")][:4]
    if representative:
        out.append("### Representative AI responses\n")
        for r in representative:
            out.append(f"**Prompt:** _{r['prompt_label']}_  ")
            out.append(f"**Platform:** {r['provider'].title()}  ")
            out.append(f"**Mentioned?** {'✓' if r['mentioned'] else '✗'}  "
                       f"| **Position:** {r.get('position', '—')}  "
                       f"| **Sentiment:** {r.get('sentiment', '—')}  ")
            comp = r.get("competitors_mentioned", [])
            if comp:
                out.append(f"**Competitors cited:** {', '.join(comp)}  ")
            snippet = r["response_text"][:400].strip().replace("\n", " ")
            out.append(f"> {snippet}{'...' if len(r['response_text']) > 400 else ''}\n")
    return "\n".join(out)


def format_citability_section(data):
    if not data:
        return "_Citability analysis not available._\n"
    site_avg = data.get("site_avg_citability", 0)
    site_coverage = data.get("site_coverage_pct", 0)
    out = [f"**Score: {site_avg}/100** · Coverage: {site_coverage}% of blocks score above 70\n"]

    pages = data.get("pages", [])
    if pages:
        successful = [p for p in pages if "error" not in p]
        if successful:
            top = sorted(successful, key=lambda p: p.get("average_citability_score", 0),
                         reverse=True)[:3]
            bottom = sorted(successful, key=lambda p: p.get("average_citability_score", 0))[:3]

            out.append("### Top pages\n| URL | Score | Coverage |\n|---|---:|---:|")
            for p in top:
                out.append(f"| {p['url']} | {p.get('average_citability_score', 0)} | "
                           f"{p.get('citability_coverage_pct', 0)}% |")

            out.append("\n### Rewrite priorities\n| URL | Score |\n|---|---:|")
            for p in bottom:
                out.append(f"| {p['url']} | {p.get('average_citability_score', 0)} |")
    return "\n".join(out) + "\n"


def format_schema_section(data):
    if not data:
        return "_Schema analysis not available._\n"
    summary = data.get("summary", {})
    score = summary.get("score", 0)
    schemas = summary.get("schemas_site_wide", {})
    missing = summary.get("missing_critical", [])

    out = [f"**Score: {score}/100**\n"]
    out.append("### Schemas found site-wide\n")
    if schemas:
        for t, n in sorted(schemas.items(), key=lambda x: -x[1]):
            out.append(f"- `{t}`: {n}")
    else:
        out.append("_None detected._")

    if missing:
        out.append("\n### Missing critical schemas\n")
        for m in missing:
            out.append(f"- {m}")
    return "\n".join(out) + "\n"


def format_generic(data, name):
    if not data:
        return f"_{name} analysis not available._\n"
    score = data.get("score", 0)
    notes = data.get("notes", "")
    return f"**Score: {score}/100**\n\n{notes}\n"


def generate_report(args):
    live = load_json(args.live_citation)
    cit = load_json(args.citability)
    schema = load_json(args.schema)
    brand_auth = load_json(args.brand_authority)
    tech = load_json(args.technical)
    eeat = load_json(args.core_eeat)

    scores = {
        "live_citation":
            live.get("scoring", {}).get("composite_score") if live else None,
        "citability":
            cit.get("site_avg_citability") if cit else None,
        "brand_authority":
            brand_auth.get("score") if brand_auth else None,
        "core_eeat":
            eeat.get("score") if eeat else None,
        "technical":
            tech.get("score") if tech else None,
        "schema":
            (schema or {}).get("summary", {}).get("score") if schema else None,
    }
    composite = compute_composite(scores)

    # Build markdown
    md = []
    md.append(f"# AEO Audit: {args.brand}\n")
    md.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}")
    md.append(f"**URL:** {args.url}")
    md.append(f"**Category:** {args.category}")
    md.append(f"**Audit mode:** {args.mode}\n")
    md.append("---\n")

    md.append("## Executive Summary\n")
    md.append(f"**Overall AEO Score: {composite['score']}/100 "
              f"({composite['rating']})**\n")

    md.append("### Score breakdown\n")
    md.append("| Dimension | Score | Weight |\n|---|---:|---:|")
    for k, label in [
        ("live_citation", "Live Citation Test"),
        ("citability", "AI Citability"),
        ("brand_authority", "Brand Authority"),
        ("core_eeat", "Content CORE-EEAT"),
        ("technical", "Technical AEO"),
        ("schema", "Schema & Structured Data"),
    ]:
        s = scores[k]
        w = composite["weights_used"].get(k, 0)
        md.append(f"| {label} | {s if s is not None else '—'} | {round(100*w, 1)}% |")
    md.append(f"| **Overall** | **{composite['score']}** | 100% |\n")

    md.append("---\n")
    md.append("## 1. Live Citation Test\n")
    md.append(format_live_citation_section(live))

    md.append("---\n")
    md.append("## 2. AI Citability\n")
    md.append(format_citability_section(cit))

    md.append("---\n")
    md.append("## 3. Brand Authority\n")
    md.append(format_generic(brand_auth, "Brand Authority"))

    md.append("---\n")
    md.append("## 4. Content CORE-EEAT\n")
    md.append(format_generic(eeat, "CORE-EEAT"))

    md.append("---\n")
    md.append("## 5. Technical AEO\n")
    md.append(format_generic(tech, "Technical AEO"))

    md.append("---\n")
    md.append("## 6. Schema & Structured Data\n")
    md.append(format_schema_section(schema))

    md.append("---\n")
    md.append("## Next steps\n")
    md.append("This audit surfaces the gaps — closing them takes execution. The 30-day action plan above is a reasonable starting point; prioritize the Critical-severity items first, then work down by expected-impact-to-effort ratio.\n")
    md.append("To track progress, re-run this audit in 30 days and compare scores by dimension. Brand Authority moves slowly (90-180 days); Citability, Technical, and Schema can move in weeks.\n")

    md.append("---\n")
    md.append("## Appendix — Methodology & Attribution\n")
    md.append("- Citability rubric adapted from [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)")
    md.append("- Brand authority rubric based on Ahrefs December 2025 study of 75,000 brands")
    md.append("- CORE-EEAT framework from [core-eeat-content-benchmark](https://github.com/aaron-he-zhu/core-eeat-content-benchmark) v3.0")
    md.append("- Technical & schema frameworks adapted from geo-seo-claude and seo-geo-claude-skills")
    md.append("")
    md.append("This audit represents a point-in-time measurement. AEO is probabilistic. Re-run monthly to track trajectory.\n")

    report_md = "\n".join(md)

    # Raw data dump
    raw = {
        "brand": args.brand,
        "url": args.url,
        "category": args.category,
        "audit_mode": args.mode,
        "generated_at": datetime.now().isoformat(),
        "composite": composite,
        "scores": scores,
        "phase_outputs": {
            "live_citation": live,
            "citability": cit,
            "schema": schema,
            "brand_authority": brand_auth,
            "technical": tech,
            "core_eeat": eeat,
        },
    }

    # Write
    with open(args.output_md, "w") as f:
        f.write(report_md)
    with open(args.output_json, "w") as f:
        json.dump(raw, f, indent=2, default=str)

    print(f"Report: {args.output_md}", file=sys.stderr)
    print(f"Raw data: {args.output_json}", file=sys.stderr)
    print(f"Overall AEO Score: {composite['score']}/100 ({composite['rating']})",
          file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="Assemble AEO audit report")
    parser.add_argument("--brand", required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--mode", default="standard",
                        choices=["quick", "standard", "deep"])

    parser.add_argument("--live-citation", help="Phase 1 JSON path")
    parser.add_argument("--citability", help="Citability JSON path")
    parser.add_argument("--schema", help="Schema validator JSON path")
    parser.add_argument("--brand-authority", help="Brand authority JSON path")
    parser.add_argument("--technical", help="Technical AEO JSON path")
    parser.add_argument("--core-eeat", help="CORE-EEAT JSON path")

    parser.add_argument("--output-md", default="AEO-AUDIT-REPORT.md")
    parser.add_argument("--output-json", default="AEO-AUDIT-DATA.json")

    args = parser.parse_args()
    generate_report(args)


if __name__ == "__main__":
    main()
