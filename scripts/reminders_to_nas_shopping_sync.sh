#!/usr/bin/env bash
set -euo pipefail

# Reverse sync: Apple Reminders (Family Shopping) -> NAS Shopping_List.md
# Canonical source remains NAS markdown; this only appends missing items under NEED TO BUY.

LIST_NAME="${REMINDERS_LIST_NAME:-Family Shopping}"
NAS_ROOT="${NAS_ROOT:-${HOME}/nas}"
NAS_MEALPREP_DIR="${NAS_MEALPREP_DIR:-${NAS_ROOT}/Documents/MealPrep}"
NAS_FILE="${NAS_SHOPPING_FILE:-${NAS_MEALPREP_DIR}/Shopping_List.md}"
BACKUP_DIR="${NAS_SHOPPING_BACKUP_DIR:-${NAS_MEALPREP_DIR}/.backups}"
STATUS_JSON="${NAS_REMINDERS_STATUS_JSON:-${NAS_MEALPREP_DIR}/.status/reminders_import_status.json}"

HA_HOST="${HA_HOST:-192.168.50.166}"
HA_PORT="${HA_PORT:-22}"
HA_USER="${HA_USER:-root}"
HA_KEY="${HA_KEY:-$HOME/.ssh/id_ed25519_kira_ha}"
HA_STATUS_DIR="${HA_STATUS_DIR:-/config/mealprep/.status}"

BRIDGE_SSH="${REMINDERS_BRIDGE_SSH:-${REMINDERS_BRIDGE_SH:-}}"   # optional: user@mac-host; leave empty to prefer local osascript
TEST_ITEMS_FILE="${REMINDERS_ITEMS_FILE:-}"      # optional: newline-separated items for testing

mkdir -p "$(dirname "$STATUS_JSON")" "$BACKUP_DIR"

now_iso() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

write_status_json() {
  local status="$1" imported="$2" backup_path="$3" note="$4"
  cat > "$STATUS_JSON" <<JSON
{
  "timestamp": "$(now_iso)",
  "status": "${status}",
  "items_imported": ${imported},
  "backup_path": "${backup_path}",
  "note": "${note//\"/\'}"
}
JSON
}

push_ha_status() {
  local status="$1" imported="$2" backup_path="$3"
  local ts
  ts="$(now_iso)"
  ssh -i "$HA_KEY" -p "$HA_PORT" "$HA_USER@$HA_HOST" "mkdir -p '$HA_STATUS_DIR' && \
    printf '%s' '$ts' > '$HA_STATUS_DIR/reminders_import_last_sync_iso' && \
    printf '%s' '$status' > '$HA_STATUS_DIR/reminders_import_status' && \
    printf '%s' '$imported' > '$HA_STATUS_DIR/reminders_import_items_count' && \
    printf '%s' '$backup_path' > '$HA_STATUS_DIR/reminders_import_backup_path'" >/dev/null 2>&1 || true
}

if [[ ! -f "$NAS_FILE" ]]; then
  write_status_json "failed_missing_markdown" 0 "" "Shopping markdown not found"
  push_ha_status "failed_missing_markdown" 0 ""
  exit 1
fi

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT
RAW_ITEMS="$TMP_DIR/reminders_raw.txt"

if [[ -n "$TEST_ITEMS_FILE" ]]; then
  cp "$TEST_ITEMS_FILE" "$RAW_ITEMS"
elif command -v osascript >/dev/null 2>&1; then
  if ! osascript <<APPLESCRIPT > "$RAW_ITEMS"
tell application "Reminders"
  if not (exists list "$LIST_NAME") then error "List not found: $LIST_NAME"
  tell list "$LIST_NAME"
    set _names to name of every reminder whose completed is false
  end tell
end tell
set AppleScript's text item delimiters to linefeed
if (count of _names) is 0 then
  return ""
else
  return _names as text
end if
APPLESCRIPT
  then
    write_status_json "failed_read_reminders" 0 "" "Failed reading reminders locally via osascript"
    push_ha_status "failed_read_reminders" 0 ""
    exit 1
  fi
elif [[ -n "$BRIDGE_SSH" ]]; then
  if ! ssh -T "$BRIDGE_SSH" 'osascript' <<APPLESCRIPT > "$RAW_ITEMS"; then
tell application "Reminders"
  if not (exists list "$LIST_NAME") then error "List not found: $LIST_NAME"
  tell list "$LIST_NAME"
    set _names to name of every reminder whose completed is false
  end tell
end tell
set AppleScript's text item delimiters to linefeed
if (count of _names) is 0 then
  return ""
else
  return _names as text
end if
APPLESCRIPT
    write_status_json "failed_read_reminders" 0 "" "Failed reading reminders via REMINDERS_BRIDGE_SSH"
    push_ha_status "failed_read_reminders" 0 ""
    exit 1
  fi
else
  write_status_json "failed_no_bridge" 0 "" "osascript not found; set REMINDERS_BRIDGE_SSH or REMINDERS_ITEMS_FILE"
  push_ha_status "failed_no_bridge" 0 ""
  exit 1
fi

BACKUP_FILE="$BACKUP_DIR/Shopping_List.md.$(date +%Y%m%d-%H%M%S).bak"
cp "$NAS_FILE" "$BACKUP_FILE"

if ! IMPORTED_COUNT="$(python3 - "$NAS_FILE" "$RAW_ITEMS" <<'PY'
import re, sys
from pathlib import Path

md_path = Path(sys.argv[1])
rem_path = Path(sys.argv[2])
text = md_path.read_text(encoding='utf-8')
lines = text.splitlines()

# parse reminders input
raw_lines = [s.strip() for s in rem_path.read_text(encoding='utf-8').splitlines() if s.strip()]

# identify NEED TO BUY block
need_start = None
pantry_start = None
for i, line in enumerate(lines):
    if re.match(r'^##\s+NEED TO BUY\s*$', line):
        need_start = i
    if re.match(r'^##\s+PANTRY ASSUMED\s*$', line):
        pantry_start = i
        break

if need_start is None or pantry_start is None or pantry_start <= need_start:
    print('parse_structure_error', file=sys.stderr)
    sys.exit(3)

need_block = lines[need_start+1:pantry_start]

# Remove old imported sections so we can re-sync them (supports removals from iOS)
clean_need = []
i = 0
while i < len(need_block):
    if need_block[i].strip() == '### Imported from Family Shopping':
        i += 1
        while i < len(need_block):
            ln = need_block[i]
            if re.match(r'^###\s+', ln) or re.match(r'^##\s+', ln):
                break
            i += 1
        continue
    clean_need.append(need_block[i])
    i += 1

# collect existing fixed items (outside imported block)
existing_norm = set()
for line in clean_need:
    m = re.match(r'^\s*-\s+(.+?)\s*$', line)
    if not m:
        continue
    item = m.group(1).strip()
    if item.endswith(':'):
        continue
    norm = re.sub(r'\s+', ' ', item).strip().casefold()
    if norm:
        existing_norm.add(norm)

# normalize + dedupe reminders
reminders = []
seen = set()
for item in raw_lines:
    norm = re.sub(r'\s+', ' ', item).strip().casefold()
    if not norm or norm in seen:
        continue
    seen.add(norm)
    reminders.append((item.strip(), norm))

managed_items = [item for item, norm in reminders if norm not in existing_norm]

new_need = list(clean_need)
if managed_items:
    if len(new_need) > 0 and new_need[-1].strip() != '':
        new_need.append('')
    new_need.append('### Imported from Family Shopping')
    for item in managed_items:
        new_need.append(f'- {item}')
    new_need.append('')

new_lines = lines[:need_start+1] + new_need + lines[pantry_start:]
new_text = '\n'.join(new_lines) + '\n'
old_text = text if text.endswith('\n') else text + '\n'
changed = 1 if new_text != old_text else 0

if changed:
    md_path.write_text(new_text, encoding='utf-8')

print(f"{len(managed_items)}|{changed}")
PY
)"; then
  cp "$BACKUP_FILE" "$NAS_FILE" || true
  write_status_json "failed_merge" 0 "$BACKUP_FILE" "Merge failed; restored backup"
  push_ha_status "failed_merge" 0 "$BACKUP_FILE"
  exit 1
fi

SYNC_ITEMS_COUNT="${IMPORTED_COUNT%%|*}"
SYNC_CHANGED_FLAG="${IMPORTED_COUNT##*|}"

if [[ "$SYNC_CHANGED_FLAG" == "1" ]]; then
  write_status_json "ok" "$SYNC_ITEMS_COUNT" "$BACKUP_FILE" "Synced imported reminders block into NEED TO BUY"
  push_ha_status "ok" "$SYNC_ITEMS_COUNT" "$BACKUP_FILE"
  echo "Synced reminders into NAS shopping list (managed items: $SYNC_ITEMS_COUNT)."
  exit 0
fi

write_status_json "ok_no_changes" "$SYNC_ITEMS_COUNT" "$BACKUP_FILE" "No markdown changes needed"
push_ha_status "ok_no_changes" "$SYNC_ITEMS_COUNT" "$BACKUP_FILE"
echo "No markdown changes needed."
exit 0
