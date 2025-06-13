SELECT Authors.name, SUM(Books.copies_available) AS total_copies 
FROM Authors
INNER JOIN Books ON Authors.author_id = Books.author_id
INNER JOIN Borrowings ON Books.book_id = Borrowings.book_id
GROUP BY Authors.name;