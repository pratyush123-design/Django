SELECT member_id, COUNT(book_id) AS total_borrowed 
FROM Borrowings 
WHERE EXTRACT(MONTH FROM borrowed_date) = 1 
  AND EXTRACT(YEAR FROM borrowed_date) = 2023
GROUP BY member_id 
HAVING COUNT(book_id) > 2 
  AND member_id NOT IN 
    (SELECT member_id 
     FROM Borrowings 
     WHERE EXTRACT(MONTH FROM borrowed_date) > 1 
       AND EXTRACT(YEAR FROM borrowed_date) = 2023);