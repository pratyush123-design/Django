SELECT name FROM Members 
WHERE member_id IN 
(SELECT member_id FROM Borrowings 
 GROUP BY member_id 
 HAVING COUNT(book_id) = (SELECT COUNT(*) FROM Books));