SELECT member_id, COUNT(book_id) AS total_borrowed 
FROM Borrowings 
GROUP BY member_id;