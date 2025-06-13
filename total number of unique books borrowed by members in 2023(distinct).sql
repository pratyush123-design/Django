SELECT COUNT(DISTINCT book_id) 
FROM Borrowings 
WHERE EXTRACT(YEAR FROM borrowed_date) = 2023;