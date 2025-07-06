SELECT 
    MONTH(date) AS Month, 
    SUM(price) AS Total_Revenue
FROM 
    customers c
JOIN 
    plans p ON c.customer_id = p.plan_id
JOIN 
    date d ON c.customer_id = d.date_id
WHERE 
    YEAR(date) = 2008
GROUP BY 
    MONTH(date);