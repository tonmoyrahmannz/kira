#!/usr/bin/env bash
set -euo pipefail

cd "$(cd "$(dirname "$0")/.." && pwd)"

echo "== Kira Resume Snapshot =="
echo

for f in \
  SOUL.md \
  USER.md \
  system/kira_identity.md \
  system/boot_prompt.md \
  docs/session_state.md \
  tasks/active.md; do
  echo "--- $f ---"
  if [[ -f "$f" ]]; then
    sed -n '1,120p' "$f"
  else
    echo "(missing)"
  fi
  echo
 done

echo "Tip: update docs/session_state.md and tasks/* after major progress."
