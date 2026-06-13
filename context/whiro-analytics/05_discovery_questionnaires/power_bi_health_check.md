# Power BI Health Check — Discovery Questionnaire

*Purpose: Pre-engagement questionnaire to scope the health check. Collect responses via Google Form, email, or discovery call notes.*

---

## Organisation Details

1. Organisation name:
2. Industry/sector:
3. Number of Power BI users (total):
4. Number of Power BI report consumers:
5. Number of Power BI pro/premium licenses:
6. Do you have a Power BI dedicated capacity (Premium Per User / Premium / Fabric)? If yes, which SKU?
7. Primary contact name and role:
8. How long has your organisation used Power BI?

---

## Reporting Environment

9. Approximate number of Power BI workspaces:
10. Approximate number of datasets/semantic models:
11. Approximate number of published reports:
12. How many reports are actively used (vs. stale/abandoned)?
13. Do you have a formal workspace structure or naming convention?
   - [ ] Yes
   - [ ] No
14. Do you use deployment pipelines (dev/test/prod)?
   - [ ] Yes
   - [ ] No
15. How do you manage report versioning and change?
   - [ ] No formal process
   - [ ] Manual / ad-hoc
   - [ ] Deployment pipelines
   - [ ] DevOps / CI-CD
   - [ ] Other:

---

## Data Sources

16. What types of data sources do your reports connect to? (select all that apply)
   - [ ] Excel / CSV files
   - [ ] SharePoint / OneDrive
   - [ ] SQL Server / Azure SQL
   - [ ] Azure Synapse / Fabric
   - [ ] Dataverse / Dynamics 365
   - [ ] Web APIs
   - [ ] Other databases (Oracle, PostgreSQL, etc.)
   - [ ] Power BI Dataflows
   - [ ] Other:
17. How are refreshes scheduled?
   - [ ] Manual only
   - [ ] Scheduled gateway refresh
   - [ ] DirectQuery / Direct Lake
   - [ ] Automated pipeline (Data Factory, etc.)
   - [ ] Mixed / varies by dataset
18. Do you use an on-premises data gateway?
   - [ ] Yes — how many gateways, and what mode (standard / personal)?
   - [ ] No
19. Do you experience refresh failures?
   - [ ] Occasionally
   - [ ] Frequently
   - [ ] Rarely

---

## Performance & Pain Points

20. Which best describes your Power BI experience?
   - [ ] Working well — occasional issues
   - [ ] Some reports are slow or unreliable
   - [ ] Multiple reports are slow or fail regularly
   - [ ] Significant trust or governance problems
21. Have users reported inconsistent numbers across different reports?
   - [ ] Yes
   - [ ] No
22. What are your top 3 pain points with Power BI? (free text)

---

## Security & Access

23. How is report access managed?
   - [ ] App workspace permissions only
   - [ ] Row-Level Security (RLS)
   - [ ] Object-Level Security (OLS)
   - [ ] No formal security model
   - [ ] Unsure
24. Do you have external/customer-facing reporting needs?
   - [ ] Yes
   - [ ] No

---

## Governance

25. Do you have documented standards for naming, model design, DAX, or report layout?
   - [ ] Yes
   - [ ] Partial
   - [ ] No
26. Is there a data catalog or data dictionary?
   - [ ] Yes
   - [ ] Partial
   - [ ] No
27. Who owns Power BI administration in your organisation?
28. Is Power BI usage being monitored (e.g. through Admin Portal, Log Analytics, or third-party tools)?
   - [ ] Yes
   - [ ] No

---

## Scope & Expectations

29. What would you like the health check to focus on most? (rank or select)
   - [ ] Performance / report speed
   - [ ] Governance and security
   - [ ] Data model quality
   - [ ] Refresh reliability
   - [ ] Duplicate or stale reports
   - [ ] General health assessment
30. Are there specific reports or datasets you would like included in scope?
31. What other initiatives or priorities should we be aware of?
32. What timeframe would you expect for this health check?
33. Who is the decision-maker for this engagement?

---

## Notes for Kira

- Keep this as a Google Form or Notion template for reuse.
- Use responses to scope effort estimate (small/medium/large).
- Follow up discovery call: ask for a 30-min screen share of their Power BI service + a walkthrough of 1–2 problem reports.
