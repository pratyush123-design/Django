SELECT Authors.name, COUNT(Books.book_id) AS book_count 
FROM Authors 
INNER JOIN Books ON Authors.author_id = Books.author_id 
GROUP BY Authors.name 
ORDER BY book_count ASC 
LIMIT 1;