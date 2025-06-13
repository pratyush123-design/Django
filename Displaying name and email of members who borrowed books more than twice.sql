SELECT name, email FROM Members 
WHERE member_id IN 
(SELECT member_id FROM Borrowings 
 WHERE EXTRACT(YEAR FROM borrowed_date) = 2023 
 GROUP BY member_id HAVING COUNT(borrowing_id) > 2);