-- Project 2: E-commerce Funnel and A/B Test (SQLite)
-- Load experiment_users.csv into experiment_users.
SELECT variant, COUNT(*) AS users, SUM(purchase) AS conversions,
       ROUND(1.0 * SUM(purchase) / COUNT(*), 4) AS conversion_rate,
       ROUND(SUM(revenue) / COUNT(*), 2) AS revenue_per_user
FROM experiment_users
GROUP BY variant;

SELECT device, variant, COUNT(*) AS users, SUM(purchase) AS conversions,
       ROUND(1.0 * SUM(purchase) / COUNT(*), 4) AS conversion_rate
FROM experiment_users
GROUP BY device, variant
ORDER BY device, variant;

SELECT variant,
       SUM(product_view) AS product_viewers,
       SUM(add_to_cart) AS cart_users,
       SUM(checkout_started) AS checkout_users,
       SUM(purchase) AS buyers
FROM experiment_users
GROUP BY variant;
