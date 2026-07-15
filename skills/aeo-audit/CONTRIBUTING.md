# Contributing to aeo-audit-skill

Thanks for the interest. Here's how to propose changes that actually make it in.

## Philosophy

The skill is deliberately opinionated. Keep these principles in mind when proposing changes:

1. **Measurement > inference.** The Live Citation Test is the spine of this skill. Changes that strengthen real-world measurement of AI behavior are prioritized. Changes that add more site-signal heuristics should be carefully justified.

2. **Rubrics are evidence-based.** Every scoring threshold in the rubrics is tied to published research or direct empirical data. If you propose changing a threshold, cite the source.

3. **Client-deliverable output.** The report template exists to produce something a consultant can hand to a paying client. Additions to the report should serve that goal.

4. **Graceful degradation.** The skill must work with zero API keys, missing subagents, failed fetches, or CSR-only sites. If you add a feature, add the degradation path.

## Ways to contribute

### Report a bug

Open an issue with:
- What you ran (full command or prompt)
- What you expected
- What happened instead (include logs, stack traces, partial outputs)
- OS / Python version / which API providers you were using

### Improve a rubric

This is the highest-leverage contribution. If you have empirical evidence that a scoring threshold is off (e.g., you ran 50 audits and the citability score doesn't correlate with real citation rates), open an issue with:
- Which rubric file and which threshold
- Your evidence (data, research, or pattern you observed)
- Your proposed revised threshold
- Any known counter-examples

Then submit a PR with the rubric revision AND an update to the `research citations used` section of `CREDITS.md`.

### Add a new provider to the Live Citation Test

Currently supports Claude, GPT-4o, and Perplexity. PRs for Gemini, Mistral, Cohere, and DeepSeek welcome. Requirements:
- Async implementation (see `query_perplexity` pattern in `scripts/live_citation_test.py`)
- Graceful handling of missing API key
- Same response-parsing interface (text + optional citations list)
- Test against at least one real brand before submitting

### Add a scoring script

If you want to add a new phase-2 analysis (e.g., a dedicated `llms.txt` validator, a Wikipedia presence checker, a Reddit sentiment scanner), the pattern is:

1. Script in `scripts/` that takes inputs via argparse and outputs JSON
2. Reference rubric in `references/` if there's a scoring dimension
3. Integration hook in `generate_report.py`
4. Documentation block in `SKILL.md` under the appropriate phase

### Improve documentation

If you hit a confusing moment using the skill, please fix it in the README, `SKILL.md`, or a reference file. Documentation PRs are reviewed fast.

## What won't be accepted

- Rubric changes without evidence or research citation
- Features that require specific paid third-party SaaS APIs (unless behind an explicit feature flag with free fallback)
- Changes that break graceful degradation (e.g., making API keys mandatory)
- Removal of upstream attribution — CREDITS.md is load-bearing

## PR process

1. Fork, branch, commit, PR to `main`
2. Describe what's changing and why
3. Include before/after for rubric changes with test evidence
4. Run the three evals in `evals/evals.json` before submitting
5. Update CREDITS.md if you're adding new upstream inspiration

## Tests

There are no automated tests yet (the skill-creator eval pattern is coming — see [skill-creator docs](https://github.com/anthropics/skills)). For now, manual validation:

```bash
# Each script has a --help and should run without errors on a real URL
python scripts/citability_scorer.py https://linear.app
python scripts/schema_validator.py https://linear.app
python scripts/live_citation_test.py --brand "Linear" --url "https://linear.app" \
    --category "project management" --competitors "Jira,Asana"
```

## Questions

Open a discussion issue on GitHub.
