-- Project 4: HR Attrition (SQLite)
-- Load employees.csv into employees.
-- This dataset is synthetic; use aggregate, responsible analysis only.
SELECT department, COUNT(*) AS employees,
       SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) AS attrition_count,
       ROUND(1.0 * SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 4) AS attrition_share
FROM employees
GROUP BY department
ORDER BY attrition_share DESC;

SELECT overtime, COUNT(*) AS employees,
       ROUND(1.0 * SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 4) AS attrition_share
FROM employees
GROUP BY overtime;

SELECT job_satisfaction_1_to_4, COUNT(*) AS employees,
       ROUND(1.0 * SUM(CASE WHEN attrition = 'Yes' THEN 1 ELSE 0 END) / COUNT(*), 4) AS attrition_share
FROM employees
GROUP BY job_satisfaction_1_to_4
ORDER BY job_satisfaction_1_to_4;
