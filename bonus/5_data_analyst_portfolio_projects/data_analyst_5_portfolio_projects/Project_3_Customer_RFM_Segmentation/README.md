# Project 3 — Customer RFM Segmentation

## Business problem
Marketing needs a transparent way to identify loyal customers, promising new buyers, and customers who may be at risk of lapsing.

## Business questions
1. How recent, frequent, and high-value are customers?
2. How large is each segment and what share of revenue does it represent?
3. Which acquisition channels bring valuable customers?
4. What actions fit each segment?
5. How would you test whether a campaign causes incremental purchases?

## Core KPIs
Recency days, distinct orders, total order value, RFM score, customers per segment, revenue share, revenue per customer.

## Files
`data/customers.csv`; `data/transactions.csv`; `notebooks/customer_rfm_segmentation.ipynb`; `sql/analysis_queries.sql`.

## Recommended workflow
1. Read the data and data-grain note before aggregating.
2. Profile key fields, missing values, duplicate keys, and date coverage.
3. Answer the business questions with SQL and Python.
4. Build a Power BI report with a clear overview page and focused drill-downs.
5. Write an executive summary: finding → evidence → implication → recommendation → success metric.
6. Publish only truthful findings, definitions, limitations, and the synthetic-data disclosure.

## Portfolio deliverables
RFM table; segment summary; customer strategy matrix; experiment proposal; Power BI page with segment filters.

## Limitations and caveats
RFM score bins and segment rules are heuristics that depend on the reference date and observation window. Validate retention and contribution margin before investing in campaigns.

## How to run
Open Jupyter from this project folder, then open the notebook under `notebooks/`. If necessary, install packages using:

```python
%pip install pandas numpy scipy matplotlib
```

The SQL examples in `sql/analysis_queries.sql` are written for SQLite. Import the CSV data into tables using the table names shown in the comments.
