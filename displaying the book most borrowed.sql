SELECT title, name FROM Books 
INNER JOIN Authors ON Books.author_id = Authors.author_id
INNER JOIN Borrowings ON Books.book_id = Borrowings.book_id 
GROUP BY title, name 
ORDER BY COUNT(Borrowings.book_id) DESC LIMIT 1;