SELECT category, AVG(copies_available) 
FROM Books 
GROUP BY category;