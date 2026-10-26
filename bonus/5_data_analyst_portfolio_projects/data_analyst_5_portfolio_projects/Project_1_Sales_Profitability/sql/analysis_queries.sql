-- Project 1: Sales and Profitability (SQLite)
-- Load sales_lines.csv into a table named sales_lines.
-- Revenue and gross_profit are transaction-line values; order_id can repeat.
SELECT strftime('%Y-%m', order_date) AS month,
       ROUND(SUM(revenue), 2) AS revenue,
       ROUND(SUM(gross_profit), 2) AS gross_profit,
       ROUND(SUM(gross_profit) / NULLIF(SUM(revenue), 0), 4) AS gross_margin
FROM sales_lines
GROUP BY strftime('%Y-%m', order_date)
ORDER BY month;

SELECT category, channel,
       ROUND(SUM(revenue), 2) AS revenue,
       ROUND(SUM(gross_profit), 2) AS gross_profit,
       ROUND(SUM(gross_profit) / NULLIF(SUM(revenue), 0), 4) AS gross_margin,
       ROUND(AVG(discount_pct), 3) AS avg_discount
FROM sales_lines
GROUP BY category, channel
ORDER BY gross_profit DESC;

SELECT product_id, category, SUM(gross_profit) AS gross_profit
FROM sales_lines
GROUP BY product_id, category
ORDER BY gross_profit ASC
LIMIT 10;
