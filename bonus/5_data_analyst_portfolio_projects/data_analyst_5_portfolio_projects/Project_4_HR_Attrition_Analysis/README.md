# Project 4 — HR Attrition Analysis

## Business problem
People operations wants an aggregate view of recorded attrition patterns and a responsible plan for investigating work-process issues that may affect retention.

## Business questions
1. What is the overall recorded attrition share and how does it vary by department?
2. How do descriptive rates vary by overtime, satisfaction, and tenure?
3. Which group differences warrant validation with employee feedback and process data?
4. What aggregate interventions could be piloted and evaluated?
5. What fairness, privacy, and interpretation limits should be disclosed?

## Core KPIs
Employee count, attrition count, recorded attrition proportion by group, tenure-band summaries, group denominators.

## Files
`data/employees.csv`; `notebooks/hr_attrition_analysis.ipynb`; `sql/analysis_queries.sql`.

## Recommended workflow
1. Read the data and data-grain note before aggregating.
2. Profile key fields, missing values, duplicate keys, and date coverage.
3. Answer the business questions with SQL and Python.
4. Build a Power BI report with a clear overview page and focused drill-downs.
5. Write an executive summary: finding → evidence → implication → recommendation → success metric.
6. Publish only truthful findings, definitions, limitations, and the synthetic-data disclosure.

## Portfolio deliverables
Aggregate HR dashboard; data-quality notes; responsible follow-up plan; caveats about sample, causation, fairness, and privacy.

## Limitations and caveats
All data are synthetic. This project is for aggregate learning only, not to rank, score, hire, fire, or otherwise make individual employment decisions.

## How to run
Open Jupyter from this project folder, then open the notebook under `notebooks/`. If necessary, install packages using:

```python
%pip install pandas numpy scipy matplotlib
```

The SQL examples in `sql/analysis_queries.sql` are written for SQLite. Import the CSV data into tables using the table names shown in the comments.
