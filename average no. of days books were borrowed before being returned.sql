SELECT AVG(return_data - borrowed_date) AS avg_days_borrowed FROM Borrowings 
WHERE EXTRACT(YEAR FROM borrowed_date) = 2022;