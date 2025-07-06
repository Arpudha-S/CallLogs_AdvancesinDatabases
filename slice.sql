SELECT 
    location, 
    SUM(price) AS Total_Revenue
FROM 
    customers c
JOIN 
    plans p ON c.customer_id = p.plan_id
WHERE 
    location = 'Firozabad'
GROUP BY 
    location;
