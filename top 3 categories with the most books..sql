SELECT category, COUNT(*) AS book_count 
FROM Books 
GROUP BY category 
ORDER BY book_count DESC 
LIMIT 3;