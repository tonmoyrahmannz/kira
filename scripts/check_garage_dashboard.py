#!/usr/bin/env python3
import json, sys, re, subprocess

# Get the dashboard file from HA
result = subprocess.run(
    ['ssh', 'ha', 'cat /config/.storage/lovelace.dashboard_garage'],
    capture_output=True, text=True, timeout=10
)
data = json.loads(result.stdout)
views = data.get("data", {}).get("views", [])
print(f"Total views: {len(views)}")
for v in views:
    title = v.get("title", v.get("path", "?"))
    cards = v.get("cards", [])
    print(f'\nView: "{title}" ({len(cards)} cards)')
    for i, c in enumerate(cards):
        cstr = json.dumps(c)
        entities = re.findall(r'entity["\']\s*:\s*["\']([^"\']+)["\']', cstr)
        if entities:
            for e in entities:
                if any(x in e.lower() for x in ["ps5", "playstation", "sony", "245"]):
                    card_type = c.get("type", "?")
                    print(f'  Card {i}: type="{card_type}" => entity={e}')
                    print(f'    Full: {json.dumps(c, indent=2)[:400]}')
                    print()

# Also search for any entity that appears in this dashboard
all_entities = set()
for v in views:
    for c in v.get("cards", []):
        for e in re.findall(r'entity["\']\s*:\s*["\']([^"\']+)["\']', json.dumps(c)):
            all_entities.add(e)

# Find the PS5-related ones
for e in sorted(all_entities):
    if any(x in e.lower() for x in ["ps5", "playstation", "sony", "245"]):
        print(f"Entity in dashboard: {e}")
