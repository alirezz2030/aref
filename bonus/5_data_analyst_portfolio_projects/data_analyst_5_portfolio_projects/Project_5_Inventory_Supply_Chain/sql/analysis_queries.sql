-- Project 5: Inventory and Supply Chain (SQLite)
-- Load inventory_monthly.csv into inventory_monthly.
-- Load products.csv into products.
SELECT month,
       SUM(demand_units) AS demand_units,
       SUM(fulfilled_units) AS fulfilled_units,
       SUM(stockout_units) AS stockout_units,
       ROUND(1.0 * SUM(fulfilled_units) / NULLIF(SUM(demand_units), 0), 4) AS unit_fill_rate,
       ROUND(SUM(estimated_stockout_value), 2) AS estimated_stockout_value
FROM inventory_monthly
GROUP BY month
ORDER BY month;

SELECT p.category,
       SUM(i.demand_units) AS demand_units,
       SUM(i.stockout_units) AS stockout_units,
       ROUND(SUM(i.estimated_stockout_value), 2) AS estimated_stockout_value
FROM inventory_monthly i
JOIN products p ON p.product_id = i.product_id
GROUP BY p.category
ORDER BY estimated_stockout_value DESC;

SELECT warehouse,
       SUM(stockout_units) AS stockout_units,
       ROUND(1.0 * SUM(stockout_units) / NULLIF(SUM(demand_units), 0), 4) AS unmet_demand_share
FROM inventory_monthly
GROUP BY warehouse
ORDER BY unmet_demand_share DESC;
