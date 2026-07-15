# Example audit outputs

This directory shows what the skill actually produces. The audit below was run against anthropic.com without API keys (Phase 1 skipped) — so it demonstrates how the composite score renormalizes gracefully when some dimensions aren't measured.

## Files

- **`anthropic-audit-report.md`** — the client-deliverable markdown report
- **`anthropic-audit-report.html`** — the presentation-ready HTML version (dark theme, designed for screen-recording or client presentations)

## What to look at

Open the HTML file in a browser to see:
- The composite AEO Score hero card with rating
- Per-dimension score breakdown table
- The placeholder Live Citation Test section (shows what the empty state looks like)
- Real citability scores from actual anthropic.com pages
- Detected schemas with validation

Open the markdown file to see the same content formatted for copy/paste into Notion, Slack, Linear, etc.

## Reproducing this output

```bash
# From the repo root
python scripts/citability_scorer.py \
    --urls "https://www.anthropic.com/news/claude-opus-4-7,https://www.anthropic.com/claude/opus" \
    --output cit.json

python scripts/schema_validator.py \
    --urls "https://www.anthropic.com/news/claude-opus-4-7,https://www.anthropic.com/claude/opus" \
    --output schema.json

python scripts/generate_report.py \
    --brand "Anthropic" --url "https://www.anthropic.com" \
    --category "AI models" --mode standard \
    --citability cit.json --schema schema.json

python scripts/generate_html_report.py --data AEO-AUDIT-DATA.json
```

## A full example (with Phase 1)

Coming soon — I'll run a complete audit (all API keys configured) on a public brand and add it here. If you've run the skill and want your audit featured as an example, open a PR.
