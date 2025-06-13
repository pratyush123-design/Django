SELECT member_id, COUNT(DISTINCT book_id) AS unique_books 
FROM Borrowings 
GROUP BY member_id 
ORDER BY unique_books DESC 
LIMIT 1;