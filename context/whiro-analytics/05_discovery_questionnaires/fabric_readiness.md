# Fabric Readiness Assessment — Discovery Questionnaire

*Purpose: Pre-engagement questionnaire to scope a Fabric readiness assessment. Use alongside an environment walkthrough.*

---

## Organisation Profile

1. Organisation name:
2. Industry/sector:
3. Approximate number of employees:
4. Data team size (data engineers, analysts, architects):
5. Primary contact name and role:

---

## Current Technology Stack

6. Which of the following do you currently use? (select all that apply)
   - [ ] Power BI (Pro / PPU / Premium)
   - [ ] Azure SQL Database
   - [ ] SQL Server on-premises
   - [ ] Azure Synapse Analytics
   - [ ] Azure Data Factory
   - [ ] Azure Data Lake Storage
   - [ ] Databricks
   - [ ] Snowflake
   - [ ] Microsoft Dynamics 365 / Dataverse
   - [ ] Microsoft 365 / SharePoint / Teams
   - [ ] SAP / Oracle / other ERP
   - [ ] Other (please list):
7. What is your primary data warehouse / analytics platform?
8. Do you have a data lake today?
   - [ ] Yes — what technology?
   - [ ] No
9. What ETL/ELT tools do you use?
10. Do you use any open-source or non-Microsoft tools in your data stack?

---

## Current Challenges & Motivation

11. What is driving your interest in Microsoft Fabric? (select all that apply)
    - [ ] Reduce tool sprawl / simplify the data stack
    - [ ] Replace legacy on-premises SQL / SSIS / SSRS
    - [ ] Enable self-service analytics
    - [ ] Improve data governance and lineage
    - [ ] Move to medallion architecture
    - [ ] Consolidate data sources
    - [ ] Licensing/cost optimisation
    - [ ] Vendor consolidation (fewer vendors, single platform)
    - [ ] Others are doing it / management interest
    - [ ] Unsure — exploring options
12. What are your top 3 data platform pain points today? (free text)
13. Have you evaluated other platforms (Databricks, Snowflake, Google BigQuery, AWS)?
    - [ ] No
    - [ ] Yes — what was the outcome?
14. Do you have a specific business problem or data workload you want to solve with Fabric?

---

## Data Landscape

15. Approximate data volume today (total TB across sources):
16. Number of data sources (distinct systems/feeds):
17. What types of data do you work with? (select all that apply)
    - [ ] Transactional / operational
    - [ ] Customer / CRM
    - [ ] Financial / ERP
    - [ ] IoT / sensor / real-time
    - [ ] Unstructured (documents, images, logs)
    - [ ] External / third-party data
    - [ ] Other:
18. How frequently do you need data to be available?
    - [ ] Real-time / near real-time
    - [ ] Hourly
    - [ ] Daily
    - [ ] Weekly / monthly
19. Do you have existing data pipelines and how are they built?
20. What is your current data architecture pattern?
    - [ ] Single data warehouse
    - [ ] Data lake + warehouse
    - [ ] Data mesh / data domains
    - [ ] Lakehouse (Databricks, Apache Iceberg, Delta Lake)
    - [ ] No formal architecture
    - [ ] Other:

---

## Analytics & Reporting

21. What tools are used for reporting and analytics today?
    - [ ] Power BI
    - [ ] Excel
    - [ ] Tableau
    - [ ] Looker
    - [ ] Custom dashboards (web apps)
    - [ ] SSRS / paginated reports
    - [ ] Other:
22. How many published reports/dashboards exist?
23. Who builds reports?
    - [ ] Central BI / data team only
    - [ ] Distributed — business analysts in departments
    - [ ] Both
24. Do you have data governance practices in place?
    - [ ] No formal governance
    - [ ] Basic — some naming conventions and ownership
    - [ ] Moderate — catalog, lineage, ownership defined
    - [ ] Advanced — data catalog, stewardship, certification, data contracts

---

## Microsoft Licensing & Capacity

25. What Microsoft licensing do you have today?
    - [ ] Microsoft 365 E3/E5
    - [ ] Power BI Pro / PPU / Premium
    - [ ] Azure subscription (free / pay-as-you-go / Enterprise Agreement)
    - [ ] Microsoft 365 + Dynamics 365
    - [ ] Microsoft EA / CSP agreement
26. Do you have an existing Azure consumption commitment?
27. Are there budget constraints or a preferred procurement model?
    - [ ] Upfront / annual commitment preferred
    - [ ] Monthly / pay-as-you-go preferred
28. What timeframe are you considering for a Fabric adoption decision?

---

## Team & Capability

29. How many people work in data / analytics / BI today?
    - [ ] 0
    - [ ] 1–2
    - [ ] 3–5
    - [ ] 6+
30. Do you have dedicated data engineering capability?
31. Do you have SQL capability?
32. Do you have Power BI / Fabric capability?
33. Would your team need training/skilling as part of a Fabric adoption?
34. Do you prefer to build internal capability or rely on external partners for ongoing data platform management?

---

## Governance & Compliance

35. Are there regulatory or compliance requirements relevant to your data platform?
    - [ ] Privacy Act 2020
    - [ ] Industry-specific regulations (health, financial services, etc.)
    - [ ] Internal data classification / retention policies
    - [ ] Other:
36. Do you need data residency in New Zealand?
37. Do you have data sovereignty or cross-border data requirements?

---

## Decision Timeline & Budget

38. What is your decision timeline for a Fabric investment?
    - [ ] Already decided — need implementation support
    - [ ] Within the next 3 months
    - [ ] 3–6 months
    - [ ] 6–12 months
    - [ ] Exploring — no fixed timeline
39. Do you have a budget range for a Fabric adoption assessment?
40. Who needs to be involved in the decision?
    - [ ] CIO / CTO / IT Director
    - [ ] Head of Data / Analytics
    - [ ] Finance / CFO
    - [ ] Business stakeholders
    - [ ] External advisor / board

---

## Notes for Kira

- For complex environments, request a 60-min architecture walkthrough and a diagram of current data flows.
- Fabric readiness is often a multi-stakeholder engagement — identify the champion and the decision-maker separately.
- Include a Fabric capacity calculator exercise if the prospect is serious (T-SQL, CU cost estimation, or Power BI usage metrics).
- If the prospect is already on Fabric Free or has started a Fabric trial, the scope shifts to optimisation + governance review.
