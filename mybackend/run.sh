#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
export PYTHONPATH="$ROOT/venv/lib/python3.14/site-packages${PYTHONPATH:+:$PYTHONPATH}"
exec /usr/bin/python3.14 "$ROOT/manage.py" "$@"
