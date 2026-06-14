# Health Goal Meal Planning Rules

_Last updated: 2026-06-14_

Purpose: support Tonmoy’s 2026 health reset goal — lose about 12 kg over roughly 4 months while preserving family-friendly, pregnancy-safe, child-friendly meal planning.

This file supplements, not replaces:

- `config/Household_Preferences.md`
- `config/Meal_Generation_Rules.md`

## Nutrition priorities

When generating meal plans, bias meals toward:

1. Higher protein.
2. High fibre from vegetables, dal, beans, lentils, whole grains, fruit.
3. Moderate measured carbs, especially rice/roti/pasta/potato.
4. Lower oil and less deep-fried food.
5. Leftovers suitable for lunch to reduce reactive eating.
6. Practical weeknight cooking under 60 minutes where possible.

## Plate guidance

For Tonmoy’s portions, assume:

- Protein: generous palm-sized serving.
- Vegetables/salad/dal: 1–2 fists.
- Carbs: measured portion, not automatic seconds.
- Fats/oils/sauces: controlled, especially with curries and fried foods.

## Cuisine handling

Keep preferred cuisines, but use lighter defaults:

- Bangladeshi / Indian: grilled, baked, simmered, dal-heavy, vegetable-rich; watch oil and rice portions.
- Japanese: rice bowls with measured rice, lean protein, miso/soup/vegetables.
- Chinese / Thai: stir-fries with controlled oil, lean protein, vegetables; measured noodles/rice.
- Turkish / Mediterranean: grilled protein, salad, yoghurt-based sauces, controlled bread/rice.
- Italian: tomato-based sauces, lean protein, vegetables, measured pasta.

## Weekly meal plan structure

Aim for:

- 2 chicken/fish/seafood meals.
- 1 lean beef/lamb meal if desired.
- 1–2 dal/bean/lentil-heavy meals.
- 2 leftover-friendly lunches from dinners.
- At least 4 dinners with clear vegetable components.

## Avoid / limit

- Deep-fried snacks and sides.
- Heavy cream-based meals.
- Large rice/pasta portions without protein/vegetables.
- Sweets as default dessert.
- Takeaway-style meals more than once/week unless intentionally planned and portioned.

## Output requirements for health-mode meal plans

When Kira generates a weekly meal plan for this goal, include:

- Protein anchor for each dinner.
- Vegetable/fibre anchor for each dinner.
- Lunch leftover note where applicable.
- Tonmoy portion note if relevant, especially for rice/pasta/roti.
- Shopping list grouped by section.
