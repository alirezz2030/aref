# Project 2 — E-commerce Funnel and A/B Test

## Business problem
A product team is considering a checkout change. Measure where users drop off and evaluate whether variant B improves conversion compared with variant A.

## Business questions
1. What share of eligible users reach each funnel step?
2. Does conversion differ between A and B?
3. What are the absolute and relative lifts, and how uncertain are they?
4. Do results differ by device? Treat subgroup results as exploratory.
5. What checks are needed before a rollout decision?

## Core KPIs
Stage-to-stage conversion, overall conversion, revenue per user, absolute percentage-point lift, relative lift, confidence interval, p-value.

## Files
`data/experiment_users.csv` (one row per assigned user); `notebooks/ecommerce_funnel_ab_test.ipynb`; `sql/analysis_queries.sql`.

## Recommended workflow
1. Read the data and data-grain note before aggregating.
2. Profile key fields, missing values, duplicate keys, and date coverage.
3. Answer the business questions with SQL and Python.
4. Build a Power BI report with a clear overview page and focused drill-downs.
5. Write an executive summary: finding → evidence → implication → recommendation → success metric.
6. Publish only truthful findings, definitions, limitations, and the synthetic-data disclosure.

## Portfolio deliverables
Funnel chart; experiment result table; test-design checks; recommendation to launch, reject, or run a planned follow-up.

## Limitations and caveats
Synthetic randomized experiment. Statistical significance does not establish business value; confirm sample-ratio, randomization, guardrails, duration, and metric definitions.

## How to run
Open Jupyter from this project folder, then open the notebook under `notebooks/`. If necessary, install packages using:

```python
%pip install pandas numpy scipy matplotlib
```

The SQL examples in `sql/analysis_queries.sql` are written for SQLite. Import the CSV data into tables using the table names shown in the comments.
