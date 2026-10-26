-- Project 3: Customer RFM (SQLite)
-- Load customers.csv as customers and transactions.csv as transactions.
WITH rfm AS (
    SELECT customer_id,
           CAST(julianday('2026-07-01') - julianday(MAX(order_date)) AS INTEGER) AS recency_days,
           COUNT(DISTINCT order_id) AS frequency,
           ROUND(SUM(order_value), 2) AS monetary
    FROM transactions
    GROUP BY customer_id
)
SELECT * FROM rfm ORDER BY monetary DESC LIMIT 25;

SELECT c.region, COUNT(DISTINCT t.customer_id) AS customers,
       ROUND(SUM(t.order_value), 2) AS revenue,
       COUNT(DISTINCT t.order_id) AS orders
FROM transactions t
JOIN customers c ON c.customer_id = t.customer_id
GROUP BY c.region
ORDER BY revenue DESC;

SELECT c.acquisition_channel,
       COUNT(DISTINCT t.customer_id) AS customers,
       ROUND(SUM(t.order_value), 2) AS revenue,
       ROUND(SUM(t.order_value) / COUNT(DISTINCT t.customer_id), 2) AS revenue_per_customer
FROM transactions t
JOIN customers c ON c.customer_id = t.customer_id
GROUP BY c.acquisition_channel
ORDER BY revenue_per_customer DESC;
