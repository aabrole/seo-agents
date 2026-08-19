#!/usr/bin/env bash
# Finalize SEO/AEO copy: strip invisible provenance marks (Layer A) + AI
# metadata (container frontmatter) via the watermarks-remover service.
#
# Usage:
#   clean_copy.sh <file>             # -> <file>.cleaned.<ext>, prints actions
#   clean_copy.sh --in-place <file>  # overwrite the file
#   clean_copy.sh --inspect <file>   # report only, no write
#
# Layer B (statistical-watermark rewrite) is a separate paraphrase/humanize pass
# — weaker when Claude paraphrases Claude; prefer a non-Claude model. See the
# copy-watermark-hygiene skill.
set -euo pipefail

WM="${WATERMARKS_SERVICE_URL:-http://127.0.0.1:8765}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PY="${WM_PYTHON:-}"
if [ -z "$PY" ]; then
  for c in python3.12 python3.13 python3.11 python3.10 python3; do
    if command -v "$c" >/dev/null 2>&1; then PY="$(command -v "$c")"; break; fi
  done
fi

MODE="clean"
case "${1:-}" in
  --in-place) MODE="inplace"; shift ;;
  --inspect)  MODE="inspect"; shift ;;
esac

FILE="${1:-}"
if [ -z "$FILE" ] || [ ! -f "$FILE" ]; then
  echo "usage: clean_copy.sh [--in-place|--inspect] <file>" >&2; exit 2
fi

# Ensure the service is up (starts + clones on first use).
"$HERE/wm_serve.sh" >/dev/null

NAME="$(basename "$FILE")"
B64="$(base64 -i "$FILE" 2>/dev/null || base64 < "$FILE")"
EP="clean"; [ "$MODE" = "inspect" ] && EP="inspect"

RESP="$(curl -s -X POST "$WM/$EP" -H 'Content-Type: application/json' \
  -d "{\"file\": \"$B64\", \"name\": \"$NAME\"}")"

if [ "$MODE" = "inspect" ]; then
  echo "$RESP" | "$PY" -c "import sys,json;r=json.load(sys.stdin);print(json.dumps(r.get('report',r),indent=1))"
  exit 0
fi

OUT="$FILE"
if [ "$MODE" = "clean" ]; then
  DIR="$(dirname "$FILE")"; BASE="${NAME%.*}"; EXT="${NAME##*.}"
  OUT="$DIR/$BASE.cleaned.$EXT"
fi

echo "$RESP" | "$PY" -c "
import sys, json, base64
r = json.load(sys.stdin)
if not r.get('cleaned'):
    print('no cleaned payload:', json.dumps(r)[:300], file=sys.stderr); sys.exit(1)
open('$OUT','wb').write(base64.b64decode(r['cleaned']))
print('wrote: $OUT')
print(json.dumps(r.get('report',{}).get('actions', r.get('report',{})), indent=1))
"
