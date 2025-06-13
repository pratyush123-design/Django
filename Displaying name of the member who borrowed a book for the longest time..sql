SELECT name, (return_data - borrowed_date) AS days_borrowed 
FROM Members
INNER JOIN Borrowings ON Members.member_id = Borrowings.member_id 
ORDER BY days_borrowed DESC 
LIMIT 1;