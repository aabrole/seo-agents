#!/usr/bin/env bash
#
# One-shot push to github.com/aabrole/aeo-audit-skill
#
# PREREQUISITES:
#   1. You've already created an empty repo at github.com/aabrole/aeo-audit-skill
#      (no README, no LICENSE, no .gitignore — those are in this folder already)
#   2. You have a GitHub personal access token or SSH key configured locally
#   3. You are CD'd into the unzipped aeo-audit-skill directory
#
# USAGE:
#   chmod +x push.sh
#   ./push.sh
#
# This script does NOT delete itself — review before running and delete after
# the first successful push if you don't want it in the repo.

set -e  # exit on any error

echo "==> Sanity-checking you're in the right directory..."
if [ ! -f "SKILL.md" ] || [ ! -f "README.md" ]; then
  echo "ERROR: Run this from inside the unzipped aeo-audit-skill directory."
  exit 1
fi

echo "==> Sanity-checking no hardcoded API keys snuck in..."
# Match real keys (long suffix), not placeholders like "sk-or-v1-..."
if grep -rnE "sk-or-v1-[a-zA-Z0-9]{30,}|sk-ant-[a-zA-Z0-9]{30,}|sk-proj-[a-zA-Z0-9]{30,}|pplx-[a-zA-Z0-9]{30,}" . --exclude-dir=.git 2>/dev/null; then
  echo "ERROR: Potential API key found above. DO NOT push. Clean it first."
  exit 1
fi
echo "    Clean — no hardcoded keys."

echo "==> Initializing git repo..."
git init

echo "==> Staging all files..."
git add -A

echo "==> Confirming no .env file is staged..."
if git diff --cached --name-only | grep -E "^\.env$"; then
  echo "ERROR: .env is staged. Unstage it: git reset HEAD .env"
  exit 1
fi

echo "==> Creating initial commit..."
git commit -m "feat: initial release of aeo-audit-skill

Answer Engine Optimization audit for Claude Code.

- Live Citation Test: 5 prompts x up to 4 providers = real AI queries
- Site audit: citability, brand authority, technical AEO, CORE-EEAT, schema
- Composite AEO Score with prioritized action plan
- Markdown + JSON + HTML reports

Providers: Anthropic, OpenAI, Perplexity, OpenRouter (for Gemini/Llama/etc.)

Adapted from geo-seo-claude, core-eeat-content-benchmark, and marketingskills.
See CREDITS.md for full attribution."

echo "==> Setting main branch..."
git branch -M main

echo "==> Adding GitHub remote..."
git remote add origin https://github.com/aabrole/aeo-audit-skill.git

echo "==> Pushing to GitHub..."
git push -u origin main

echo ""
echo "==> Done. Repo is live at:"
echo "    https://github.com/aabrole/aeo-audit-skill"
echo ""
echo "Next steps:"
echo "  1. Go to the repo page and add topics: claude, claude-code, aeo, seo,"
echo "     generative-engine-optimization, llm, ai-audit"
echo "  2. Add an 'About' description with a link to amanabrole.com"
echo "  3. Pin the repo on your profile"
echo "  4. Delete this push.sh now that it's served its purpose:"
echo "     git rm push.sh && git commit -m 'chore: remove push helper' && git push"
