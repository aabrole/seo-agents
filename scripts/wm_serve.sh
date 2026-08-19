#!/usr/bin/env bash
# Start the watermarks-remover HTTP service (Layer A text + container metadata).
# Idempotent. Auto-clones the upstream service repo if missing. Needs Python 3.10+.
#
# Env overrides:
#   WATERMARKS_SERVICE_URL   default http://127.0.0.1:8765
#   WM_REPO                  default $HOME/seoagent/tools/watermarks-remover
#   WM_PYTHON                default: first of python3.12/3.13/3.11/3.10 on PATH
set -euo pipefail

WM="${WATERMARKS_SERVICE_URL:-http://127.0.0.1:8765}"
WM_REPO="${WM_REPO:-$HOME/seoagent/tools/watermarks-remover}"
UPSTREAM="https://github.com/guillaumemeyer/watermarks-remover"
LOG="${WM_LOG:-/tmp/wm-service.log}"

if curl -sf "$WM/health" >/dev/null 2>&1; then
  echo "watermarks service already up at $WM"; exit 0
fi

# Resolve a Python 3.10+ interpreter.
PY="${WM_PYTHON:-}"
if [ -z "$PY" ]; then
  for c in python3.12 python3.13 python3.11 python3.10; do
    if command -v "$c" >/dev/null 2>&1; then PY="$(command -v "$c")"; break; fi
  done
fi
if [ -z "$PY" ]; then
  echo "ERROR: need Python 3.10+ (set WM_PYTHON). Base service uses 3.10+ syntax." >&2
  exit 1
fi

# Clone the service repo if we don't have it yet.
if [ ! -d "$WM_REPO" ]; then
  echo "cloning watermarks-remover into $WM_REPO ..."
  mkdir -p "$(dirname "$WM_REPO")"
  git clone --depth 1 "$UPSTREAM" "$WM_REPO"
fi

cd "$WM_REPO"
nohup "$PY" service/scripts/server.py --host 127.0.0.1 --port 8765 > "$LOG" 2>&1 &
for _ in $(seq 1 12); do
  sleep 0.5
  if curl -sf "$WM/health" >/dev/null 2>&1; then
    echo "watermarks service started at $WM (log: $LOG)"; exit 0
  fi
done
echo "ERROR: service did not become healthy; see $LOG" >&2
tail -5 "$LOG" >&2 || true
exit 1
