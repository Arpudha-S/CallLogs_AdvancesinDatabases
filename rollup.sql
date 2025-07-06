SELECT 
    YEAR(date) AS Year, 
    SUM(price) AS Total_Revenue
FROM 
    customers c
JOIN 
    plans p ON c.customer_id = p.plan_id
JOIN 
    date d ON c.customer_id = d.date_id
GROUP BY 
    YEAR(date);
