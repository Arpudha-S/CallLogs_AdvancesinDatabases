SELECT 
    location,
    SUM(CASE WHEN YEAR(date) = 2023 THEN price ELSE 0 END) AS Revenue_2023,
    SUM(CASE WHEN YEAR(date) = 2022 THEN price ELSE 0 END) AS Revenue_2022
FROM 
    customers c
JOIN 
    plans p ON c.customer_id = p.plan_id
JOIN 
    date d ON c.customer_id = d.date_id
GROUP BY 
    location;
