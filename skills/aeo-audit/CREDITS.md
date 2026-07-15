# Credits & Attribution

This skill is a synthesis of several excellent open-source works in the AEO/GEO space. The original authors deserve credit — please consider starring and contributing to their repositories.

## Primary sources

### [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) by Zubair Trabzada
**License:** MIT
**What we used:**
- Citability scoring rubric (5 categories: Answer Block Quality, Self-Containment, Structural Readability, Statistical Density, Uniqueness) — see `references/citability-rubric.md`
- `scripts/citability_scorer.py` adapted from their `citability_scorer.py` with modifications
- Brand authority platform weighting research (Ahrefs Dec 2025 findings, YouTube ~0.737 correlation) — see `references/brand-authority-rubric.md`
- Technical AEO rubric structure (crawler access, llms.txt, rendering, CWV) — see `references/technical-aeo-rubric.md`
- Overall audit orchestration pattern (5-subagent parallel delegation + composite scoring)

### [core-eeat-content-benchmark v3.0](https://github.com/aaron-he-zhu/core-eeat-content-benchmark) by Aaron He-Zhu (part of [seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills))
**License:** Apache-2.0
**What we used:**
- 80-item CORE-EEAT checklist (8 dimensions: Contextual Clarity, Organization, Referenceability, Exclusivity × Experience, Expertise, Authority, Trust) — see `references/core-eeat-checklist.md`
- MECE boundary rule (CORE = content body, EEAT = source credibility)
- Priority tagging system (GEO-First 🎯 / SEO-First 🔍 / Dual ⚡)

### [marketingskills](https://github.com/coreyhaines31/marketingskills) by Corey Haines
**License:** MIT
**What we used:**
- `ai-seo` skill interview framework for gathering client context
- Platform-specific AI ranking factors reference
- Schema markup priority ordering for different business types

## What's original to aeo-audit

The following elements are our own contributions built on top of the above:

- **Live Citation Test (Phase 1)** — the entire workflow of running 5 strategic prompts against ChatGPT / Claude / Perplexity APIs in parallel, parsing responses for mentions/position/sentiment/competitors. No source skill does this. `scripts/live_citation_test.py` is original.
- **Composite scoring weights** — our specific weighting (Live Citation 15% / Citability 20% / Brand Authority 20% / CORE-EEAT 20% / Technical 15% / Schema 10%) with the rationale in `SKILL.md`
- **Report template structure** — organized around Live Citation as hero section with site audit as supporting evidence, rather than the typical site-first structure
- **Business-type adjustments** — reweighting guidance by SaaS/Local/E-commerce/Publisher/Agency — synthesized from source material
- **Operating modes** (quick/standard/deep) — tiered audit depth with time/output tradeoffs

## Research citations used in rubrics

- Princeton / Georgia Tech / IIT Delhi (2024) — GEO optimization study showing 30-115% visibility lift
- Bortolato (2025) — 134-167 word optimal passage length for AI citation
- Ahrefs (Dec 2025) — 75,000-brand analysis showing YouTube mentions correlate ~0.737 with AI citation
- Profound (2025), Terakeet (2025) — corroborating platform-importance research
- Answer.AI (2024) — llms.txt proposed standard

## License

This skill is released under MIT license. You may use, modify, and redistribute it freely. When using rubrics derived from the sources above, please preserve their attribution.

## How to contribute improvements back

If you improve this skill materially (e.g., better CSR handling in the citability scorer, a new provider in the live citation test, a more accurate brand authority heuristic), please:

1. Open a PR on our repo (if public)
2. Credit your contribution in this file
3. Consider also contributing improvements back to the upstream sources where applicable — the AEO research space benefits from shared improvements

## Author

Initial synthesis: Aman Abrole (amanabrole.com) — with substantial assistance from Claude.
