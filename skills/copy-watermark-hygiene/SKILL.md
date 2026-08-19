---
name: copy-watermark-hygiene
description: "When finalizing any AI-produced copy before it ships to a client or CMS — strip invisible provenance marks, AI metadata, and (optionally) reduce statistical watermarks. Use when the user mentions 'remove watermark,' 'clean the copy,' 'invisible characters,' 'zero-width,' 'AI marks,' 'strip metadata,' 'de-AI the text,' 'humanize before publish,' 'content credentials,' 'C2PA,' or asks that produced articles/deliverables be cleaned before handoff. Run this as the last step on generated articles, landing-page copy, and briefs. For writing/humanizing prose itself, see content-humanize; this skill is the finalization/hygiene pass."
metadata:
  version: 1.0.0
---

# Copy Watermark Hygiene

Finalization pass that removes provenance marks from AI-produced copy before it
reaches a client or CMS. Thin client over the open-source **watermarks-remover**
service (`guillaumemeyer/watermarks-remover`) — all cleaning runs in a local HTTP
service; this skill just calls it and reports honestly.

## When to run

Run on **every** generated deliverable at handoff: articles, landing-page copy,
content briefs, meta descriptions pasted into a CMS. Invisible Unicode is the
concern that actually breaks CMS rendering and git diffs; provenance metadata is
the second.

## Tooling (bundled)

- `scripts/wm_serve.sh` — starts the service (auto-clones the upstream repo on
  first run; needs Python 3.10+). Idempotent.
- `scripts/clean_copy.sh <file>` — inspect + clean one file.

```bash
# Report only — what marks are present?
scripts/clean_copy.sh --inspect draft.md

# Clean → writes draft.cleaned.md, prints the actions taken
scripts/clean_copy.sh draft.md

# Overwrite in place (only when the user asked)
scripts/clean_copy.sh --in-place draft.md
```

## Two layers — be honest about which you did

**Layer A — deterministic (this is what the service does).** Removes zero-width
characters, normalizes no-break spaces / homoglyphs, and strips AI metadata from
`.md` / `.html` frontmatter and containers. Conservative: it leaves legitimate
typography (curly quotes, em dashes) intact. Fully verifiable — report the exact
counts from the `actions` / `report` field.

**Layer B — statistical-watermark rewrite (NOT automatic).** A paraphrase or
humanize pass on the cleaned text. The service does not hold a rewrite model —
**you** are the rewrite model. Caveat that matters here: when the copy was
Claude-authored and you are Claude, a Claude paraphrase is a *weak* Layer B for
token-sampling watermarks. Prefer a non-Claude / local open-weight model for that
pass, or state plainly that Layer B was best-effort same-model. Preserve all
facts, numbers, names, and identifiers. See `content-humanize` for the rewrite
prompts.

## Reporting rules

- State what Layer A **verifiably** removed (counts/actions).
- If you ran Layer B, call it best-effort — **never** claim output is
  "undetectable" or "proves human-written."
- Out of scope (say so if asked): pixel/audio/video watermarks, C2PA soft
  binding, secret-key vendor detectors. Optional ML backends (SynthID scorer,
  pixel removal) and `exiftool`/`qpdf` are usually not installed — check
  `curl -s "$WATERMARKS_SERVICE_URL/capabilities"` before promising image/PDF work.

## Ethics

For the user's own or client-authorized content only (hygiene, CMS
compatibility, privacy). Not for passing off deliverables under false pretenses,
academic fraud, or defeating a required disclosure. Do only the technical
cleaning the user owns.
