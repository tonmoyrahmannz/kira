# MealPrep System README

This folder is the canonical source of truth for household meal planning.
Do not change folder structure without updating the automation pipeline.

_Last Updated: 2026-03-11_

This folder uses a **config + inventory -> generation outputs** model.

## Folder Structure

```text
MealPrep/
├── config/
│   ├── Household_Preferences.md
│   ├── Pantry_Assumptions.md
│   └── Meal_Generation_Rules.md
├── inventory/
│   └── Pantry_Inventory.md
├── Meal_Plan.md
├── Shopping_List.md
├── Recipes/
├── .status/
└── .backups/
```

---

## Quick Start (5-Min Weekly Routine)

1. Update `inventory/Pantry_Inventory.md` (especially **Use Soon**, fridge, freezer).
2. Check `config/*` and adjust only if household rules/preferences changed.
3. Run weekly meal generation using canonical inputs (`config/*` + `inventory/*`).
4. Review regenerated outputs:
   - `Meal_Plan.md`
   - `Shopping_List.md`
   - `Recipes/*` (new/updated)
5. Sync/verify automation outputs (HA dashboard, reminders, webhook flow) without changing paths.

---

## What Each Config File Controls

### `config/Household_Preferences.md`
Controls household-level planning constraints and preferences:
- family profile (adults + child)
- pregnancy-safe food rules
- child-friendly constraints
- cuisine preferences
- shopping/store preference
- practical cooking style (weeknight-friendly, time target)

Use this file when deciding **what kind of meals are acceptable**.

### `config/Pantry_Assumptions.md`
Controls baseline staples that are usually in stock.
- defines “normally available” pantry items
- prevents unnecessary re-buying of common staples
- clarifies when assumed items should still be purchased

Use this file to decide **what should usually not appear in NEED TO BUY**.

### `config/Meal_Generation_Rules.md`
Controls the generation pipeline and operating rules.
- required input files to read first
- weekly meal generation workflow
- shopping list structure requirements
- additive/reversible change policy
- path stability requirements

Use this as the **procedural runbook** for weekly generation.

---

## What the Inventory File Does

### `inventory/Pantry_Inventory.md`
Represents meaningful, current stock on hand.
- use-soon items
- fridge/freezer items
- notable pantry quantities worth planning around

This file is used to:
- prioritise meals that consume existing stock first
- reduce food waste
- reduce duplicate shopping

Important:
- this is a practical planning snapshot, **not** a strict stock ledger
- this file remains separate from pantry assumptions

---

## Which Files Are Generated / Updated by Weekly Planning

Primary generated outputs:
- `Meal_Plan.md` (weekly dinner plan + timing + reuse notes)
- `Shopping_List.md` (consolidated grouped list + waste reduction notes)
- `Recipes/*.md` (new or updated recipe documents)

Operational support files used by automation:
- `.status/*` (sync/import status)
- `.backups/*` (shopping list backups)

---

## What Remains Canonical

Canonical inputs for generation:
1. `config/Household_Preferences.md`
2. `config/Pantry_Assumptions.md`
3. `config/Meal_Generation_Rules.md`
4. `inventory/Pantry_Inventory.md`

Canonical generated outputs for execution:
- `Meal_Plan.md`
- `Shopping_List.md`
- `Recipes/*`

Design principle:
- **Config + inventory are the planning truth**
- outputs are regenerated from that truth and current week context

---

## Weekly Regeneration Workflow

1. Read all canonical input files in this order:
   - `config/Household_Preferences.md`
   - `config/Pantry_Assumptions.md`
   - `config/Meal_Generation_Rules.md`
   - `inventory/Pantry_Inventory.md`
2. Review existing `Recipes/*`, `Meal_Plan.md`, and `Shopping_List.md` for continuity.
3. Draft 5-7 meal candidates aligned with preferences and safety rules.
4. Select a weekly set optimised for:
   - ingredient reuse
   - use-soon inventory consumption
   - practical cook times
5. Generate/update recipe files in `Recipes/` where needed.
6. Regenerate `Meal_Plan.md` for the target week.
7. Regenerate `Shopping_List.md` with grouped sections and waste-reduction notes.
8. Leave paths stable so sync / HA dashboard / webhook / reminders pipelines continue working.

---

## Maintenance Notes

- Keep changes additive and reversible.
- Do not move or delete `inventory/Pantry_Inventory.md`.
- Avoid unnecessary path changes for automation compatibility.
- Update this README when architecture or generation rules change.
