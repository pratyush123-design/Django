SELECT EXTRACT(MONTH FROM borrowed_date) AS month, COUNT(book_id) AS books_borrowed 
FROM Borrowings WHERE EXTRACT(YEAR FROM borrowed_date) = 2023 
GROUP BY month ORDER BY month;