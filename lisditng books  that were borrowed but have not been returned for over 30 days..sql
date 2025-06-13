SELECT title FROM Books 
INNER JOIN Borrowings ON Books.book_id = Borrowings.book_id 
WHERE return_data IS NULL 
AND (CURRENT_DATE - borrowed_date) > 30;