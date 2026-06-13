# Master Personal Context - Tonmoy Rahman

## Purpose

This document is the primary personal context file for Kira, Hermes, specialist agents, and future AI assistants operating on behalf of Tonmoy Rahman.

It should be treated as the top-level context entry point. Other files under the NAS can be loaded as supporting context depending on the task.

Recommended NAS location:

```text
/nas/Documents/Kira/Context/Master_Personal_Context.md
```

Recommended companion location for finance-specific context:

```text
/nas/Documents/Kira/Context/Household_Financial_Context.md
```

---

# Context Loading Rules For Kira

When starting a new session, Kira should load this file first.

Depending on the task, Kira should then load supporting files from:

```text
/nas/Documents/Work/Master_Profile.md
/nas/Documents/Work/CV/Current/Tonmoy_Rahman_CV_Master.md
/nas/Documents/Work/LinkedIn/LinkedIn_Profile_Master.md
/nas/Documents/MealPrep/README.md
/nas/Documents/MealPrep/config/Household_Preferences.md
/nas/Documents/Kira/
```

Kira should avoid modifying source-of-truth documents unless explicitly instructed.

For professional writing, CVs, recruiter responses, and career documents, Kira should use:

```text
/nas/Documents/Work/
```

For household automation, agent operations, migration notes, and AI operating context, Kira should use:

```text
/nas/Documents/Kira/
```

For meal planning and shopping list workflows, Kira should use:

```text
/nas/Documents/MealPrep/
```

For Home Assistant dashboard/project files, Kira should use:

```text
/nas/Documents/Projects/
```

For house plans, landscaping, and design context, Kira should use:

```text
/nas/Documents/Sketchup/
```

---

# Personal Profile

Name: Tonmoy Rahman

Location: Wellington, New Zealand

Family:

- Wife: Esha Rahman
- Daughter: Sophie
- Son: Kian Rahman
- Kian was born on 25 March 2026 at 8:10am at Kenepuru Hospital in Porirua, Wellington.

Core priorities:

1. Family stability and wellbeing
2. Financial security
3. Career growth
4. Long-term financial independence
5. Home automation and technology
6. Continuous learning
7. Building useful AI-assisted systems

Decision style:

- Data-driven
- Strategic
- Long-term thinker
- Prefers measurable outcomes
- Prefers practical implementation over theory
- Willing to invest upfront for long-term gains
- Prefers automation over repetitive manual effort
- Likes systems that are documented, recoverable, and easy to hand over

---

# Professional Context

Tonmoy works in data architecture, analytics, Microsoft Fabric, Power BI, Azure, and enterprise data platforms.

Current career transition:

- Leaving Grant Thornton New Zealand.
- Starting a Data Architect role at Victoria University of Wellington.
- Intends to be stable in the VUW role until approximately December 2027.
- Open to future strategic or fractional consulting opportunities if they fit around primary commitments.

Previous role context:

- Data Architect / Solution Architect / interim Analytics Lead at Grant Thornton New Zealand.
- Sole or primary data person in a lean IT team.
- Responsible for Microsoft Fabric modernisation, Power BI, Azure SQL, DevOps, and enterprise analytics patterns.

Professional specialisations:

- Microsoft Fabric
- Power BI
- Data architecture
- Data engineering
- Azure SQL
- SQL Server
- Azure DevOps
- Enterprise analytics
- Data governance
- Semantic modelling
- DirectLake
- Medallion architecture
- CI/CD for analytics platforms
- Dynamics 365 / Dataverse integration patterns
- Data quality and deduplication

Preferred technical principles:

- SQL-first transformations where practical
- ELT over ETL
- Medallion architecture
- Bronze/Silver in Lakehouse
- Gold/serving layer in Warehouse or curated semantic layer
- DirectLake where appropriate
- Semantic models should consume curated/gold data only
- Avoid duplicated business logic
- Keep Power BI transformations minimal
- Use Azure DevOps and CI/CD where practical
- Document architecture and operational handover clearly
- Prefer simple, supportable designs over unnecessarily complex architecture

---

# Career Preferences

Minimum preferred contract rate:

```text
NZD $140/hr + GST
```

Permanent salary target:

```text
NZD $170,000+
```

Career preferences:

- Prefer senior architecture, Fabric, analytics leadership, and modern data platform roles.
- Less interested in pure SQL developer roles unless the role has strong strategic or architectural elements.
- Open to recruiter relationships, but currently prioritising VUW stability.
- Future consulting or fractional work may be considered if it does not create conflict with primary employment.

Recruiter communication style:

- Concise
- Warm
- Professional
- Relationship-preserving
- Avoid sounding desperate or overly available
- Mention stability at VUW when relevant
- Keep future opportunities open

---

# Financial Context

Primary financial goals:

1. Pay down mortgage aggressively.
2. Build long-term wealth.
3. Work toward financial independence.
4. Maintain family security.
5. Buy a Tesla in the future when financially sensible.

Current philosophy:

- Avoid consumer debt.
- Avoid unnecessary vehicle finance.
- Prioritise mortgage reduction while debt is high.
- Keep an emergency fund.
- Maintain investment exposure.
- Prefer long-term net worth over lifestyle inflation.
- Tesla is a goal, but not at the expense of financial stability.

Current cash and investments:

```text
Joint savings: approximately $20,000
Sharesies portfolio: approximately $100,000
Tonmoy KiwiSaver: approximately $80,000
Esha KiwiSaver: approximately $35,000
Credit card balance: $0
Credit card limit: $5,000
Other consumer debt: none
```

Expected future mortgage position:

```text
Estimated total lending after rental sale: approximately $1,000,000
```

The household is financially solid, but still property-leveraged. The key financial milestone is selling the rental property and applying sale proceeds to reduce total lending.

---

# Household Budget Context

Fortnightly income while Esha is on parental leave:

```text
Tonmoy after-tax income: $4,400
Esha parental leave income: $1,700
Airbnb income: approximately $1,000
Total: approximately $7,100
```

Fortnightly income when Esha returns to work:

```text
Tonmoy after-tax income: $4,400
Esha after-tax income estimate: $2,100
Airbnb income: approximately $1,000
Total: approximately $7,500
```

Current fortnightly expenses:

```text
Mortgage: $2,740
Insurance: $500
Rates: $326
Utilities: $200
Internet + mobile: $75
Childcare: $1,000
Food: $300
Personal spending: $300
Fuel: $200
Entertainment: $150
Eating out: $100
Home maintenance: $100
Subscriptions: $100
Miscellaneous: $200
Total: approximately $6,291
```

Estimated surplus:

```text
Current surplus: approximately $809 per fortnight
Future surplus: approximately $1,209 per fortnight
```

Budget interpretation:

- Household is positive cashflow.
- Childcare is a major temporary expense.
- Airbnb income materially improves affordability.
- Mortgage reduction should be prioritised after the rental property sale.
- Avoid taking on an $80,000 vehicle loan while the mortgage remains high.

---

# Property Context

Current property situation:

- Primary residence is retained.
- Airbnb property is retained.
- Another rental property is currently on the market for sale.

Expected rental sale outcome:

```text
Expected sale proceeds: approximately $600,000
Use of proceeds: pay down home loan debt
Expected remaining total mortgage debt: approximately $1,000,000
```

Property strategy:

1. Reduce leverage.
2. Improve cashflow resilience.
3. Retain useful income-generating assets where sensible.
4. Avoid overextending.
5. Prioritise family stability.

---

# Home Automation And Technical Home Context

Primary smart home platform:

```text
Home Assistant OS
```

Current architecture:

```text
HAOS ARM64 running as a VM on Wyse 5070
HAOS IP: 192.168.50.166
Mac Mini IP: 192.168.50.208
Omarchy laptop IP: 192.168.50.28
Primary LAN: 192.168.50.0/24
Gateway: 192.168.50.1
Tailscale subnet routing via Mac Mini
```

Mac Mini roles:

- Plex
- SMB/NAS shares
- Tailscale subnet router
- Auxiliary services
- Kira/Hermes runtime

Important smart home integrations:

- Home Assistant
- Apple HomeKit / Apple TV Home Hub
- Tuya
- LocalTuya
- Tuya Zigbee Gateway
- Gree HVAC local controller
- Neo Smart Blinds
- Plex
- Tailscale

Known device IPs:

```text
Gree controller: 192.168.50.188:7000
Neo Smart Blinds controller: 192.168.50.224:8839
Tuya Zigbee LAN Gateway: 192.168.50.100
```

Automation philosophy:

- Local-first where practical
- Cloud acceptable where unavoidable
- Reliability over novelty
- Self-healing where possible
- Document configuration changes
- Preserve rollback paths
- Avoid fragile automations

---

# Kira / Hermes Context

Kira is Tonmoy’s personal AI operator.

Current platform note:

- Kira was previously associated with OpenClaw / Omarchy laptop.
- Kira has now moved toward Hermes / Mac Mini.
- Any old assumption that Kira primarily runs on the Omarchy laptop should be treated as outdated unless specifically confirmed.

Kira’s purpose:

- Household automation
- Documentation
- Technical research
- Home Assistant support
- Operational monitoring
- Planning
- Coding assistance through specialist agents
- Long-running investigation support
- Context management

Preferred Kira behaviour:

- Be proactive, but not reckless.
- Document actions.
- Ask before making risky changes.
- Use specialist agents for coding, debugging, and research when useful.
- Keep the main personal context clean.
- Do not pollute long-term memory with every temporary detail.
- Maintain clear distinction between source-of-truth files, generated drafts, and experiments.

Current Kira folder structure under NAS:

```text
/nas/Documents/Kira/
├── Context/
│   ├── Master_Personal_Context.md
│   ├── Household_Financial_Context.md
│   ├── Home_Assistant_Context.md
│   ├── Career_Context.md
│   └── Decision_Principles.md
├── Runbooks/
│   ├── Smart_Home_Runbook_v8.md
│   └── Tuya_IR_Remote_Runbook.md
├── Reference/
│   ├── Gree_Ducted_Zoning_Architecture.md
│   └── Smart_Home_Technical_Documentation_v5_Professional.md
├── Agent_Notes/
│   ├── Kira_Control_Plane_Handover.md
│   └── Kira_Persistence_Setup.md
├── Logs/
└── Archive/
```

All directories exist. Context, Runbooks, Reference, and Agent_Notes are populated. Logs and Archive are ready for future use.

Known permanently lost documents:
- `docs/README.md` (documentation hub)
- `docs/system-map.md` (detailed system architecture map)
- `Smart_Home_Technical_Documentation_v7_Enterprise.md` (only v5 exists)

---

# NAS Structure Awareness

Current important NAS document areas:

```text
/nas/Documents/Kira/
```

Used for Kira migration plans, audits, and agent-related documentation.

```text
/nas/Documents/MealPrep/
```

Used for meal planning, recipes, shopping list, household food preferences, and pantry assumptions.

```text
/nas/Documents/Projects/
```

Used for Home Assistant dashboards, command centre YAML files, NOC dashboard experiments, Tuya service files, and related smart home projects.

```text
/nas/Documents/Sketchup/
```

Used for house floor plans, landscaping plans, and SketchUp models.

```text
/nas/Documents/Work/
```

Used for CVs, job applications, LinkedIn content, recruiter templates, offers, onboarding, VUW documents, and professional master profile.

Important existing work files:

```text
/nas/Documents/Work/Master_Profile.md
/nas/Documents/Work/Master_Profile_Update_Template.md
/nas/Documents/Work/CV/Current/Tonmoy_Rahman_CV_Master.md
/nas/Documents/Work/CV/Current/Tonmoy_Rahman_CV_Master.docx
/nas/Documents/Work/CV/Current/Tonmoy_Rahman_CV_Short.md
/nas/Documents/Work/LinkedIn/LinkedIn_Profile_Master.md
/nas/Documents/Work/LinkedIn/Recruiter_Response_Templates.md
/nas/Documents/Work/VUW/VUW_Final Blueprint_Overview v1.3.pdf
```

---

# MealPrep Context

MealPrep is a household automation workflow stored under:

```text
/nas/Documents/MealPrep/
```

Important files:

```text
Meal_Plan.md
Shopping_List.md
README.md
config/Household_Preferences.md
config/Meal_Generation_Rules.md
config/Pantry_Assumptions.md
inventory/Pantry_Inventory.md
Recipes/
```

MealPrep principles:

- NAS is the source of truth.
- Meal plans and shopping lists should remain human-readable Markdown.
- Automations may parse these files into Home Assistant sensors or dashboards.
- Avoid destructive edits unless explicitly requested.
- Maintain household preferences and pantry assumptions.

---

# Communication Preferences

General writing style:

- Professional
- Concise
- Warm
- Human sounding
- Direct, but not rude
- Avoid excessive corporate jargon
- Avoid overusing em dashes
- Avoid obvious AI phrasing
- Prefer practical, polished wording

Common communication tasks:

- Recruiter responses
- Professional emails
- LinkedIn replies
- Architecture feedback
- Executive summaries
- CV tailoring
- Business case wording
- Handover notes

Preferred deliverables:

- Markdown
- HTML for CVs and professional profile-style documents
- Mermaid diagrams for architecture
- SQL scripts for technical implementation
- Concise executive summaries where appropriate

CV preference:

- CVs and similar documents should be generated in the established plain HTML CV template unless explicitly requested otherwise.
- Markdown and PDF versions should only be created when specifically requested or useful.

---

# Family And Lifestyle Context

Primary family objective:

Create a stable, enjoyable, and financially secure life for the family.

Family values:

- Security
- Time with children
- Good education
- Family experiences
- Comfortable home
- Thoughtful spending
- Avoid unnecessary financial stress

Lifestyle notes:

- Tesla is a desired future purchase.
- Family experiences matter, but should not compromise debt reduction and financial independence.
- Backyard, landscaping, and child-friendly home improvements are important recurring themes.

---

# Decision Framework

When making recommendations for Tonmoy, agents should generally apply this order:

1. Protect family stability.
2. Avoid unnecessary financial or operational risk.
3. Prioritise long-term value.
4. Prefer clear, documented systems.
5. Prefer automation where it reduces future effort.
6. Keep solutions supportable.
7. Avoid overengineering unless the future value is clear.
8. Preserve optionality.
9. Be honest about trade-offs.
10. Leave systems better than they were found.

---

# Risk Preferences

Financial risk:

- Moderate.
- Comfortable with investments.
- Does not want high consumer debt.
- Wants to reduce mortgage pressure.

Technical risk:

- Comfortable experimenting.
- Production/home systems should remain stable.
- New automation should be testable and reversible.

Career risk:

- Will take strategic opportunities.
- Currently values stability due to family and VUW transition.
- Open to fractional consulting if it preserves relationships and does not overcommit.

---

# Future Success Vision

By 2030, success looks like:

- Lower mortgage burden.
- Stronger investment portfolio.
- High family stability.
- Well-established role as a senior data/Fabric architect.
- Mature Home Assistant and Kira/Hermes setup.
- Reliable NAS-based household knowledge system.
- Strong AI-assisted household operations.
- Tesla ownership if financially sensible.
- More optionality around consulting, entrepreneurship, or fractional work.

---

# Instructions For Future Agents

When using this document:

1. Treat it as directional context, not immutable truth.
2. Ask for confirmation before making major financial, professional, or technical decisions.
3. Prefer updating companion files rather than bloating this master file.
4. Keep dated decisions in logs or notes.
5. Keep this file focused on durable context.
6. If new facts conflict with this document, flag the conflict and ask Tonmoy whether to update the source of truth.
7. When generating new files, place them under the most appropriate existing NAS folder.
8. Do not assume old Kira/OpenClaw/Omarchy details are current unless confirmed.
