# Project 1 — Sales and Profitability Analysis

## Business problem
Management wants to understand which products, regions, and channels drive revenue and gross profit, and whether discounting or product mix is weakening margin.

## Business questions
1. How do revenue, gross profit, and gross margin change over time?
2. Which categories and channels lead on revenue versus profit?
3. Which products contribute the least gross profit?
4. Do high-discount lines have different margins?
5. Which two actions should management test first?

## Core KPIs
Revenue, gross profit, gross margin, unique orders, average order value, average discount, quantity sold.

## Files
`data/sales_lines.csv` (transaction-line grain); `notebooks/sales_profitability_analysis.ipynb`; `sql/analysis_queries.sql`.

## Recommended workflow
1. Read the data and data-grain note before aggregating.
2. Profile key fields, missing values, duplicate keys, and date coverage.
3. Answer the business questions with SQL and Python.
4. Build a Power BI report with a clear overview page and focused drill-downs.
5. Write an executive summary: finding → evidence → implication → recommendation → success metric.
6. Publish only truthful findings, definitions, limitations, and the synthetic-data disclosure.

## Portfolio deliverables
A sales-performance dashboard; SQL queries; a short executive summary; 3 evidence-backed findings; 2 recommendations with success metrics.

## Limitations and caveats
An order can contain multiple transaction lines. Do not count rows as orders. This dataset is synthetic, with simplified cost and discount rules.

## How to run
Open Jupyter from this project folder, then open the notebook under `notebooks/`. If necessary, install packages using:

```python
%pip install pandas numpy scipy matplotlib
```

The SQL examples in `sql/analysis_queries.sql` are written for SQLite. Import the CSV data into tables using the table names shown in the comments.
