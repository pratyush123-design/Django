SELECT name FROM Members 
WHERE member_id NOT IN (SELECT member_id FROM Borrowings);