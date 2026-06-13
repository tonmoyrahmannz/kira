# Reporting Modernisation Sprint — Discovery Questionnaire

*Purpose: Pre-sprint scoping to define what gets modernised, what success looks like, and where the constraints are.*

---

## About the Report / Process

1. What is the report or reporting process you want to modernise? (name and brief description)
2. Who is the primary audience / consumer of this report?
3. How often is this report used?
   - [ ] Daily
   - [ ] Weekly
   - [ ] Monthly
   - [ ] Quarterly
   - [ ] Ad-hoc
4. How many users access or depend on this report?
5. What happens if this report breaks or is unavailable?
   - [ ] Minor inconvenience
   - [ ] Some operational impact
   - [ ] Significant business disruption
   - [ ] Regulatory / compliance risk
6. What would success look like for this modernisation? (free text — be specific)

---

## Current Pain Points

7. What is the main problem with this report today? (select top 3)
   - [ ] Too slow to load / refresh
   - [ ] Refresh fails regularly
   - [ ] Numbers don't match other reports / trust issues
   - [ ] Manual steps required (download files, run Excel macros, email)
   - [ ] Hard to maintain / modify
   - [ ] Poor documentation
   - [ ] Built by someone who is no longer available
   - [ ] Uses deprecated or fragile data sources
   - [ ] No security or access model
   - [ ] Other:
8. Which of these pains causes the most frustration or risk?
9. How long would you estimate is currently spent on manual data prep or report maintenance per week?

---

## Current Technical Details

10. Where does the source data come from? (select all that apply)
    - [ ] Excel / CSV files emailed or shared
    - [ ] SharePoint / OneDrive
    - [ ] SQL Server / Azure SQL
    - [ ] Dynamics 365 / Dataverse
    - [ ] Web service / API
    - [ ] Power BI Dataflow
    - [ ] Other database (please list):
11. How is the data currently transformed?
    - [ ] Manually in Excel
    - [ ] Power Query (in Power BI or dataflows)
    - [ ] SQL views / stored procedures
    - [ ] SSIS / Data Factory
    - [ ] Custom scripts (Python, R, etc.)
    - [ ] No transformation — raw data in report
12. What tool is the report built in?
    - [ ] Power BI
    - [ ] Excel
    - [ ] SSRS / paginated reports
    - [ ] Tableau
    - [ ] Other:
13. Is the data model documented?
14. Are there known data quality issues?
15. Does this report feed any downstream reports or processes?

---

## Desired Target State

16. What target platform should the modernised report use?
    - [ ] Power BI (Direct Lake mode)
    - [ ] Power BI (Import mode)
    - [ ] Power BI (DirectQuery)
    - [ ] Fabric Warehouse
    - [ ] Fabric Lakehouse
    - [ ] SQL Server / Azure SQL
    - [ ] Unsure — recommend the best approach
17. Should the data transformation layer move from Power Query/Excel to SQL or Fabric?
18. Should the report remain in its current tool, or move to Power BI?
19. Do you want self-service capability where business users can extend the report?
20. Do you need the modernised report to follow specific governance or security requirements?

---

## Scope & Constraints

21. Is there a specific deadline or business cycle driving the timeline?
22. Are there dependencies on other teams, systems, or external parties?
23. Do you have access to the source systems and credentials needed?
24. Can we access the existing Power BI workspace, data source, and current report file?
25. Are there any constraints on what we can change? (e.g. locked-down SQL server, no cloud, regulatory restrictions)
26. Is there a test environment available, or do we work directly in production?
27. Who will validate and accept the modernised report on completion?
28. Do you need documentation and handover support, or ongoing maintenance support?

---

## Measures of Success

29. What measurable improvements would make this sprint a success? (check all that apply)
    - [ ] Report load time under X seconds (specify):
    - [ ] Refresh completes under X minutes (specify):
    - [ ] Zero refresh failures over 1 month
    - [ ] Numbers match between this report and other trusted sources
    - [ ] Report is maintainable by someone other than the original author
    - [ ] Manual steps eliminated
    - [ ] Documentation exists and is understandable by a new team member
    - [ ] Other:
30. How would you like the before/after comparison presented?
    - [ ] Performance metrics (load times, refresh duration)
    - [ ] Visual comparison (side-by-side screenshots)
    - [ ] Technical assessment (complexity reduction, data model score)
31. What budget is available for this sprint?

---

## After the Sprint

32. Is there a likelihood of additional modernisation sprints after this one?
33. Would you consider a managed support arrangement after modernisation?
34. Who would own and maintain the modernised report going forward?

---

## Notes for Kira

- This questionnaire works best as a live discovery call guide rather than a send-ahead form — the nuances matter.
- The critical input for scoping is: **one specific report/process** + **measurable success criteria**.
- If they can't name one report, they're not ready for a sprint — redirect to the Health Check.
- Sprint pricing should use the complexity rubric: small / standard / complex based on data sources, transformations, and dependencies.
