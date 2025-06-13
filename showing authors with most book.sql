SELECT name, COUNT(book_id) AS total_books 
FROM Authors 
INNER JOIN Books ON Authors.author_id = Books.author_id 
GROUP BY name 
ORDER BY total_books DESC LIMIT 1;