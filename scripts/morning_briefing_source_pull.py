#!/usr/bin/env python3
"""Pull local sources for Kira's morning briefing."""

from __future__ import annotations

import datetime as dt
import json
import subprocess
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATE_DIR = ROOT / "state"
JSON_OUT = STATE_DIR / "morning_briefing_sources.json"
MD_OUT = STATE_DIR / "morning_briefing_sources.md"
HA_ENV = ROOT / "config" / "ha.env"
HA_URL_DEFAULT = "http://192.168.50.166:8123"

HA_ENTITIES = {
    "guest_apartment_today": "sensor.guest_apartment_today",
    "booking_com": "calendar.booking_com",
    "airbnb": "calendar.airbnb",
    "weather_home": "weather.forecast_home",
    "living_room_temperature": "sensor.living_room_sensor_temperature",
    "living_room_humidity": "sensor.living_room_sensor_humidity",
    "master_bedroom_temperature": "sensor.master_bedroom_temperature",
    "master_bedroom_humidity": "sensor.master_bedroom_humidity",
    "study_temperature": "sensor.study_sensor_temperature",
    "study_humidity": "sensor.study_sensor_humidity",
    "guest_bedroom_temperature": "sensor.guest_sensor_temperature",
    "guest_bedroom_humidity": "sensor.guest_sensor_humidity",
    "garage_temperature": "sensor.garage_sensor_temperature",
}


def now_local() -> dt.datetime:
    return dt.datetime.now().astimezone()


def read_ha_env() -> tuple[str, str | None]:
    url = HA_URL_DEFAULT
    token = None
    if HA_ENV.exists():
        for raw in HA_ENV.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            value = value.strip().strip('"').strip("'")
            if key.strip() in {"HA_URL", "HOME_ASSISTANT_URL"}:
                url = value.rstrip("/")
            elif key.strip() in {"HA_TOKEN", "HOME_ASSISTANT_TOKEN", "SUPERVISOR_TOKEN"}:
                token = value
    return url.rstrip("/"), token


def ha_get_state(base_url: str, token: str, entity_id: str) -> dict:
    req = urllib.request.Request(
        f"{base_url}/api/states/{entity_id}",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=8) as response:
        return json.loads(response.read().decode("utf-8"))


def collect_home_assistant() -> dict:
    base_url, token = read_ha_env()
    result = {"ok": False, "base_url": base_url, "entities": {}, "errors": {}}
    if not token:
        result["errors"]["token"] = "No HA token found in config/ha.env"
        return result

    for label, entity_id in HA_ENTITIES.items():
        try:
            state = ha_get_state(base_url, token, entity_id)
            result["entities"][label] = {
                "entity_id": entity_id,
                "state": state.get("state"),
                "attributes": state.get("attributes", {}),
                "last_changed": state.get("last_changed"),
            }
        except Exception as exc:
            result["errors"][label] = f"{entity_id}: {exc}"
    result["ok"] = bool(result["entities"])
    return result


def run_osascript(script: str, timeout: int = 20) -> tuple[bool, str]:
    try:
        proc = subprocess.run(
            ["/usr/bin/osascript", "-e", script],
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except Exception as exc:
        return False, str(exc)
    output = (proc.stdout or "").strip()
    error = (proc.stderr or "").strip()
    if proc.returncode != 0:
        return False, error or output or f"osascript exited {proc.returncode}"
    return True, output


def collect_calendar() -> dict:
    script = r'''
set nowDate to current date
set endDate to nowDate + (24 * hours)
set outputText to ""
tell application "Calendar"
    launch
    repeat with c in calendars
        try
            set matchingEvents to every event of c whose start date is greater than or equal to nowDate and start date is less than or equal to endDate
            repeat with e in matchingEvents
                set eventLine to (summary of e) & " | " & ((start date of e) as string) & " | " & ((end date of e) as string) & " | " & (name of c)
                set outputText to outputText & eventLine & linefeed
            end repeat
        end try
    end repeat
end tell
return outputText
'''
    ok, output = run_osascript(script, timeout=8)
    events = []
    if ok and output:
        for line in output.splitlines():
            parts = [part.strip() for part in line.split(" | ")]
            if len(parts) == 4:
                events.append({"title": parts[0], "start": parts[1], "end": parts[2], "calendar": parts[3]})
            else:
                events.append({"raw": line})
    return {"ok": ok, "events": events, "error": None if ok else output}


def collect_reminders() -> dict:
    script = r'''
set outputText to ""
tell application "Reminders"
    repeat with l in lists
        try
            set incompleteReminders to reminders of l whose completed is false
            repeat with r in incompleteReminders
                set dueText to ""
                try
                    set dueText to (due date of r) as string
                end try
                set outputText to outputText & (name of l) & " | " & (name of r) & " | " & dueText & linefeed
            end repeat
        end try
    end repeat
end tell
return outputText
'''
    ok, output = run_osascript(script)
    reminders = []
    if ok and output:
        for line in output.splitlines():
            parts = [part.strip() for part in line.split(" | ")]
            if len(parts) >= 3:
                reminders.append({"list": parts[0], "title": parts[1], "due": parts[2] or None})
            else:
                reminders.append({"raw": line})
    return {"ok": ok, "reminders": reminders, "error": None if ok else output}


def shortcuts_available() -> dict:
    binary = Path("/usr/bin/shortcuts")
    if not binary.exists():
        return {"ok": False, "error": "/usr/bin/shortcuts not found"}
    proc = subprocess.run([str(binary), "list"], capture_output=True, text=True, check=False, timeout=10)
    shortcuts = [line.strip() for line in (proc.stdout or "").splitlines() if line.strip()]
    interesting = [s for s in shortcuts if any(k in s.lower() for k in ["morning", "brief", "shopping", "meal"])]
    return {"ok": proc.returncode == 0, "count": len(shortcuts), "interesting": interesting, "error": (proc.stderr or "").strip() or None}


def render_markdown(payload: dict) -> str:
    lines = [
        "# Kira Morning Briefing Source Pull",
        "",
        f"Collected: {payload['collected_at']}",
        "",
        "## Home Assistant",
    ]
    ha = payload["home_assistant"]
    if ha.get("ok"):
        for label in sorted(ha["entities"]):
            item = ha["entities"][label]
            attrs = item.get("attributes", {})
            unit = attrs.get("unit_of_measurement", "")
            suffix = f" {unit}" if unit else ""
            lines.append(f"- {label}: {item.get('state')}{suffix}")
    else:
        lines.append("- unavailable")
    for key, value in sorted(ha.get("errors", {}).items()):
        lines.append(f"- error {key}: {value}")

    cal = payload["calendar"]
    lines.extend(["", "## Calendar Next 24 Hours"])
    if cal.get("events"):
        for event in cal["events"][:20]:
            if "raw" in event:
                lines.append(f"- {event['raw']}")
            else:
                lines.append(f"- {event['title']} ({event['calendar']}): {event['start']} to {event['end']}")
    elif cal.get("ok"):
        lines.append("- no local Calendar events returned")
    else:
        lines.append(f"- Calendar read failed: {cal.get('error')}")

    rem = payload["reminders"]
    lines.extend(["", "## Reminders"])
    if rem.get("reminders"):
        for reminder in rem["reminders"][:40]:
            due = f" due {reminder['due']}" if reminder.get("due") else ""
            lines.append(f"- {reminder.get('list')}: {reminder.get('title')}{due}")
    elif rem.get("ok"):
        lines.append("- no incomplete reminders returned")
    else:
        lines.append(f"- Reminders read failed: {rem.get('error')}")

    sc = payload["shortcuts"]
    lines.extend(["", "## Shortcut Runtime"])
    lines.append(f"- shortcuts CLI available: {sc.get('ok')}")
    lines.append(f"- matching shortcuts: {', '.join(sc.get('interesting') or []) or 'none'}")
    return "\n".join(lines) + "\n"


def main() -> int:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "collected_at": now_local().isoformat(timespec="seconds"),
        "home_assistant": collect_home_assistant(),
        "calendar": collect_calendar(),
        "reminders": collect_reminders(),
        "shortcuts": shortcuts_available(),
    }
    JSON_OUT.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    markdown = render_markdown(payload)
    MD_OUT.write_text(markdown, encoding="utf-8")
    print(markdown)
    print(f"JSON: {JSON_OUT}")
    print(f"Markdown: {MD_OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
