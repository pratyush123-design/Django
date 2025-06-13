SELECT COUNT(*) 
FROM Borrowings 
WHERE EXTRACT(YEAR FROM borrowed_date) = 2023;