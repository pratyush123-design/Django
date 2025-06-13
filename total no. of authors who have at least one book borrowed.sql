SELECT COUNT(DISTINCT Authors.author_id) AS total_authors FROM Authors 
INNER JOIN Books ON Authors.author_id = Books.author_id 
INNER JOIN Borrowings ON Books.book_id = Borrowings.book_id 
WHERE EXTRACT(YEAR FROM borrowed_date) = 2023;