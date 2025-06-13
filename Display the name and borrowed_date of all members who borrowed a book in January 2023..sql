SELECT name, borrowed_date FROM Members 
INNER JOIN Borrowings ON Members.member_id = Borrowings.member_id 
WHERE EXTRACT(MONTH FROM borrowed_date) = 6 AND EXTRACT(YEAR FROM borrowed_date) = 2023;