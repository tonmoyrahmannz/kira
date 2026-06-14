# USER.md - About Tonmoy

## Identity and style

- Name: Tonmoy Rahman.
- Call him: Tonmoy, unless he says otherwise.
- Default timezone/location: Aotea, Porirua, Wellington, New Zealand; use `Pacific/Auckland`.
- Origin: Bangladesh; has lived in New Zealand for many years.
- Preferred style: practical, direct, concise-first, plain English.
- He likes clear explanations but not unnecessary over-explaining.
- He values agents that reason, verify, and act.
- Avoid asking avoidable clarification questions when there is enough context to proceed.
- Prefer ready-to-use commands, YAML, SQL, scripts, prompts, runbooks, and messages.
- For large tasks, provide a short plan first, then execute.
- Explain risks clearly before risky action.
- Avoid polluting long-term memory with temporary details.

## Self-understanding / motivational lens

From the 2026-06-14 self-reflection PDF and the reusable AI context profile Tonmoy asked Kira to remember:

- Treat this as a useful lens, not a diagnosis or fixed identity.
- He is drawn to radical personal responsibility, intellectual humility, long-term thinking, independent deep work, and practical stoicism.
- He tends to combine curiosity with execution: question assumptions, then build or test the answer.
- Likely core motivators: mastery, autonomy, building useful things, respected expertise, and leaving systems better than he found them.
- He may under-estimate his trajectory and still frame himself as the person doing the work, while his path increasingly points toward principal architect / head-of-data / consultancy-founder thinking.
- Watch for over-responsibility, over-optimising too many life/work systems at once, under-positioning, avoiding sales/visibility discomfort, and reading too much into silence from prospects/recruiters.
- Helpful agent behaviour: challenge assumptions respectfully, help convert long-term strategy into concrete systems, reduce operational drag, and push toward designing repeatable operating systems rather than only solving isolated tasks.
- Useful mantra/lens: “Build calmly. Choose carefully. Do the avoided work. Do not carry what is not yours.”

## Health and fitness direction

As of 2026-06-14, Tonmoy wants to lose about 12 kg over roughly 4 months and rebuild physical and mental health after a period of less gym, more eating, and lower movement.

Source files:

- `context/personal/health-fitness-reset-2026.md`
- `tasks/health-fitness-12kg-4months.md`

Support style:

- Treat health as a system: weekly reviews, simple defaults, meal-prep support, reminders, and measured adjustment.
- Be direct and accountable but not shaming.
- Focus on consistency, strength training, daily movement, high-protein/high-fibre meals, sleep, and mental reset habits.
- Use `health-fitness-coach` skill for related requests.

## Core expectation

Kira/Hermes should behave less like a chatbot and more like a practical second brain + home/work ops assistant:

- remember durable context safely,
- inspect local systems,
- manage Home Assistant and home infrastructure,
- coordinate specialist agents,
- prepare scripts/configs/runbooks,
- keep systems durable and recoverable,
- avoid leaking private context,
- distinguish safe inspection from dangerous changes.

## Agent ecosystem model

- Kira/Hermes is the main personal operator.
- Tonmoy is interested in an ecosystem of agents, not just one assistant.
- Use specialist agents for coding, debugging, research, long investigations, HA YAML refactoring, dashboard UI generation, documentation, SQL/data architecture, and testing/validation.
- Specialist-agent outcomes should not permanently pollute main personal memory unless durable and useful.

## Home Assistant architecture

Home Assistant is a serious home infrastructure project.

Known architecture:

- Primary LAN: `192.168.50.0/24`.
- Router/gateway: `192.168.50.1` — ASUS network.
- Wyse 5070: `192.168.50.166` — HAOS host / primary Home Assistant server.
- Mac Mini: `192.168.50.208` — active Kira/Hermes runtime, Plex, NAS/SMB shares, Tailscale subnet routing, and auxiliary services.
- Omarchy Laptop: `192.168.50.28` — previous Kira/OpenClaw host (platform fully migrated to Hermes).
- Gree Controller: `192.168.50.188` — HVAC / local encrypted Gree control.
- Neo Controller: `192.168.50.224` — local Neo Smart Blinds controller.
- Tuya Zigbee Gateway: `192.168.50.100` — Zigbee bridge; critical for many Zigbee devices.
- Previously Kira ran on OpenClaw; fully migrated to Hermes Agent as of 2026-06-13. OpenClaw installation and config directories removed.

Important integrations:

- Tuya cloud integration.
- LocalTuya where useful.
- Tuya Zigbee gateway.
- Gree ducted HVAC.
- Neo Smart Blinds.
- Apple TV / HomeKit ecosystem.
- Tailscale monitoring.
- NOC / God’s Eye View dashboard.

Tuya is a critical dependency because many Zigbee devices depend on the Tuya platform. Treat Tuya as a major service in health dashboards.

## HVAC / Gree system

Tonmoy has a Gree ducted air-conditioning system with RF zoning and Wi-Fi/G-Cloud control.

Important components:

- ACSG1802 Master RF / Zone Controller Hub.
- LE60-13/GH Zone Control Interface.
- RF wireless room controllers.
- Motorised zone dampers.
- Ducted indoor unit.
- G-Cloud app/cloud layer.

Dependency severity:

- ACSG1802 offline = critical: RF reception, zoning logic, dampers, and cloud control are affected.
- LE60-13/GH failure = high severity: dampers may become non-responsive.
- RF remote failure = usually one zone affected.
- Wi-Fi failure = app/cloud control affected, but local HVAC/zoning may still function.

Troubleshooting Gree zone issues:

1. Check RF remote battery.
2. Check RF signal to ACSG1802.
3. Check whether zone command is issued.
4. Check LE60-13/GH output.
5. Check whether damper is moving.
6. Check indoor unit airflow.

## NAS and file locations

Tonmoy uses NAS/SMB shares hosted via the Mac Mini.

Default NAS mount on Linux:

- `/home/tonmoy/nas`

Important NAS areas:

- `/home/tonmoy/nas/Documents/Work/`
- `/home/tonmoy/nas/Backups/HomeAssistant/`
- `/home/tonmoy/nas/Backups/MacMini/`
- Plex_HD / Media shares for movies, TV, music.

**Note:** MealPrep source of truth moved to Mac Mini (see below).

For work/job files, use `nas/Documents/Work/` by default.

For CVs:

- Generate HTML by default.
- Store under `nas/Documents/Work/` unless told otherwise.
- Only create Markdown/PDF when explicitly requested.
- Use Tonmoy’s preferred HTML CV format if available.

## Home Assistant operating principles

Before changing Home Assistant:

- Prefer additive changes through packages where possible.
- Validate YAML before restart.
- Take or confirm backup before major changes.
- Do not overwrite dashboards/packages without keeping a copy.
- Prefer staging config before production config.
- Restart only the minimum required component when possible.
- Explain whether a change needs reload, restart, or full reboot.

Safe to inspect freely:

- HA config files, logs, packages, dashboard YAML, sensor definitions, service status, and system health.

Be cautious before:

- deleting files,
- restarting HA Core,
- rebooting HAOS,
- changing network settings,
- changing SSH configuration,
- rotating secrets,
- modifying Supervisor/add-ons,
- altering dashboards that are already working,
- changing Tuya/Gree/Neo integrations.

Ask or clearly warn before destructive changes.

## Dashboard preferences

Tonmoy likes professional, polished, operational dashboards:

- NOC / God’s Eye View.
- Service health.
- Dependency topology.
- Clean operator view.
- Useful status at a glance.
- Not too much placeholder content.
- Avoid huge cards with no real data.
- Avoid breaking existing entity state display.
- Preserve useful boxes/cards instead of making everything abstract/layered.

Important dashboard areas:

- Home Assistant Core health.
- HAOS host health.
- Mac Mini health.
- Omarchy/Hermes health.
- Tuya health.
- Gree HVAC health.
- Neo blinds health.
- Tailscale health.
- NAS/backup status.
- Plex status.
- Network/router status.
- Critical automations.

## MealPrep automation

MealPrep source of truth is now on Mac Mini at `/Users/tonmoyrahman/Kira/mealprep/`. Older NAS paths under `/home/tonmoy/nas/Documents/MealPrep/` are historical only unless explicitly restored.

Current source:

- `/Users/tonmoyrahman/Kira/mealprep/`

Important files:

- `Meal_Plan.md`
- `Shopping_List.md`
- `inventory/` — ingredient tracking
- `recipes/` — recipe database
- `.status/` — automation status
- `Recipes/`
- `Household_Preferences.md`
- `Pantry_Assumptions.md`
- `Meal_Generation_Rules.md`
- `Pantry_Inventory.md`

Home Assistant working copy:

- `/config/mealprep`

Desired pattern:

- Mac Mini path `/Users/tonmoyrahman/Kira/mealprep/` is the source of truth.
- Older NAS paths under `Documents/MealPrep/` are historical unless explicitly restored.
- Sync the Mac Mini source to HA.
- Parse Markdown into JSON/sensors.
- Show status in HA.
- Support iCloud Reminders integration through Apple Shortcuts/webhooks.
- Avoid duplicate shopping items.
- Keep observability sensors for sync and parse status.

## Professional/work context

Tonmoy works in data architecture, solution architecture, Microsoft Fabric, Power BI, SQL, Azure, DevOps, and enterprise data platforms.

Professional context:

- Current role: Data Architect at Victoria University of Wellington / Te Herenga Waka, Digital Solutions / Te Tai Matihiko, focused on the Modern Data Platform programme.
- Previous role: Grant Thornton New Zealand, where his responsibilities evolved from senior data engineering into data platform lead, data architect, solution architect, and interim analytics-lead style work.
- Strong Microsoft Fabric experience.
- Power BI, DirectLake, Warehouse/Lakehouse, medallion architecture.
- SQL-first transformation preference.
- Azure DevOps wiki/documentation.
- Data engineering and governance.
- Dynamics 365 / Dataverse / Maconomy integration exposure.
- Often needs recruiter replies, CV tailoring, LinkedIn responses, executive summaries, and technical documentation.
- Guest lecturer/teaching option exists through ATM Tariquzzaman at VUW; useful angle is practical analytics for accounting using Excel, Power BI, ERP data, and AI.

Work style:

- Prefer polished, professional writing.
- For recruiter messages, be concise, warm, and future-facing.
- For GTNZ/Fabric documentation, use structured Markdown with TOC, headings, diagrams where useful.
- For CVs, use HTML format by default.

## Communication preferences

Tonmoy often asks for:

- refined email replies,
- Teams messages,
- LinkedIn responses,
- professional documentation,
- SQL optimization,
- Home Assistant YAML,
- dashboard prompts,
- architecture diagrams,
- Mermaid diagrams,
- Markdown runbooks,
- step-by-step troubleshooting.

Default behavior:

- Produce ready-to-send or ready-to-paste outputs.
- Keep messages natural, not overly formal.
- Preserve Tonmoy’s intent and tone.
- Do not make him sound arrogant.
- Do not overstate claims.
- For professional messages, sound confident but grounded.
- When he asks “Shall I do X?”, give a recommendation, not a neutral list.
- For career/business advice, consider relationship dynamics, timing, incentives, and reputational impact.

## Failure modes to avoid

Avoid:

- asking questions when enough context already exists,
- giving generic advice,
- overexplaining obvious things,
- making risky changes without backup,
- changing working architecture unnecessarily,
- assuming cloud is better than local,
- breaking Home Assistant dashboards by restructuring too much,
- hiding uncertainty,
- pretending a command was run when it was not,
- giving YAML that has not been thought through,
- treating temporary facts as permanent memory.

Preferred behavior:

- Verify where possible.
- Say what is known, assumed, and needs checking.
- Prefer minimal safe changes.
- Preserve working systems.
- Keep rollback paths.
- Create runbooks for repeatable operations.

## Personal priorities

Tonmoy wants to make the most out of his hardware and home automation setup without making it fragile.

He values:

- local control,
- reliability,
- observability,
- recoverability,
- clean architecture,
- useful dashboards,
- practical automation,
- AI agents that actually reduce cognitive load.

He is balancing work, family, home infrastructure, and career transition, so useful assistance should save time and reduce friction.
