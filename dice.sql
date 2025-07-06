SELECT 
    c.location, 
    p.plan_name, 
    SUM(p.price) AS Total_Revenue
FROM 
    customers c
JOIN 
    plans p ON c.customer_id = p.plan_id
JOIN 
    date d ON c.customer_id = d.date_id  
WHERE 
    c.location IN ('Firozabad')  
    AND YEAR(d.date) = 2008
GROUP BY 
    c.location, p.plan_name;  
