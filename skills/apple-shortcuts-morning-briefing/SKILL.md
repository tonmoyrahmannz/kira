# Apple Shortcuts Morning Briefing

Use this skill when Tonmoy asks for the morning briefing source pull or wants an Apple Shortcut backed by local Mac Mini sources.

## Local workflow

- Main collector: /Users/tonmoyrahman/Kira/scripts/morning_briefing_source_pull.py
- Shortcut wrapper: /Users/tonmoyrahman/Kira/scripts/morning-briefing-source-pull.sh
- JSON output: /Users/tonmoyrahman/Kira/state/morning_briefing_sources.json
- Markdown output: /Users/tonmoyrahman/Kira/state/morning_briefing_sources.md

The collector pulls:

- Home Assistant states using /Users/tonmoyrahman/Kira/config/ha.env.
- Calendar events for the next 24 hours through local AppleScript.
- Incomplete Reminders through local AppleScript.
- A small Shortcuts CLI status check.

## Shortcut setup

The macOS shortcuts CLI can run and list shortcuts, but does not create rich shortcuts. To wire this into Shortcuts, create a Shortcut named Kira Morning Briefing Source Pull with one Run Shell Script action:

/Users/tonmoyrahman/Kira/scripts/morning-briefing-source-pull.sh

Grant permissions to Shortcuts, Terminal, and the Hermes host process when macOS prompts for Calendar, Reminders, Home folder, or network access.

## Safety

Never print Home Assistant tokens or other credentials. The collector reads tokens locally and only writes source summaries.
