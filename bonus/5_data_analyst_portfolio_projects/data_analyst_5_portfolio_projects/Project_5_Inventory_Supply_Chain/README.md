# Project 5 — Inventory and Supply Chain Analysis

## Business problem
Operations wants to understand where unmet demand and inventory pressure occur, then identify which products or warehouses should be investigated first.

## Business questions
1. What are unit fill rate and stockout indicators over time?
2. Which categories, products, and warehouses have the most unmet demand?
3. Are stockouts concentrated in certain months or long-lead suppliers?
4. What evidence should be checked before adjusting reorder points?
5. How can the business balance service levels against holding cost?

## Core KPIs
Demand units, fulfilled units, stockout units, unit fill rate, stockout-row rate, estimated stockout value, closing stock, replenishment received.

## Files
`data/inventory_monthly.csv`; `data/products.csv`; `notebooks/inventory_supply_chain_analysis.ipynb`; `sql/analysis_queries.sql`.

## Recommended workflow
1. Read the data and data-grain note before aggregating.
2. Profile key fields, missing values, duplicate keys, and date coverage.
3. Answer the business questions with SQL and Python.
4. Build a Power BI report with a clear overview page and focused drill-downs.
5. Write an executive summary: finding → evidence → implication → recommendation → success metric.
6. Publish only truthful findings, definitions, limitations, and the synthetic-data disclosure.

## Portfolio deliverables
Inventory dashboard; category/product/warehouse hotspot list; proposed replenishment-policy review; data limitations and operational next steps.

## Limitations and caveats
The monthly inventory data are synthetic and replenishment behavior is simplified. Validate lead time, backorders, safety stock, holding cost, and actual inventory timing before changing policy.

## How to run
Open Jupyter from this project folder, then open the notebook under `notebooks/`. If necessary, install packages using:

```python
%pip install pandas numpy scipy matplotlib
```

The SQL examples in `sql/analysis_queries.sql` are written for SQLite. Import the CSV data into tables using the table names shown in the comments.
