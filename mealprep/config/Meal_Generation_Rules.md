# Meal Generation Rules

This folder is the canonical source of truth for household meal planning.
Do not change folder structure without updating the automation pipeline.

_Last Updated: 2026-03-11_

This file defines the required input model and workflow for generating weekly meal plans.

## Required Input Files (Read First)
1. `config/Household_Preferences.md`
2. `config/Pantry_Assumptions.md`
3. `inventory/Pantry_Inventory.md`
4. Existing recipe files under `Recipes/`
5. Current `Meal_Plan.md` and `Shopping_List.md` (for continuity)

## Input Model (Source of Truth)
`config + inventory -> meal generator -> outputs`

Where:
- `config` = household constraints, style, and baseline pantry assumptions
- `inventory` = current meaningful stock and use-soon priorities
- `outputs` = `Meal_Plan.md`, `Shopping_List.md`, and `Recipes/*`

## Weekly Generation Workflow
0. Read all required input files above.
1. Propose 5-7 dinner options aligned with household preferences.
2. Select a balanced weekly set (cuisine variety + ingredient reuse).
3. Prioritise meals that consume `Use Soon` and other stocked inventory items.
4. Enforce pregnancy-safe and child-friendly rules.
5. Prefer meals that are practical for weeknights and generally under 60 minutes.
6. Generate/update recipe files in `Recipes/` as needed.
7. Update `Meal_Plan.md` with schedule, timing, and lunchbox reuse notes.
8. Update `Shopping_List.md` with only needed purchases, grouped by section.
9. Add short waste-reduction notes explaining reuse across meals.

## Shopping List Rules

Always include sections:
- NEED TO BUY
- PANTRY ASSUMED
- Waste Reduction Notes

## Change Management Rules
- Keep implementation additive and reversible.
- Do not remove or relocate `inventory/Pantry_Inventory.md`.
- Do not change existing automation paths for sync, HA dashboard, webhooks, or reminders.
- Preserve existing top-level files unless explicitly migrating in a separate planned step.
