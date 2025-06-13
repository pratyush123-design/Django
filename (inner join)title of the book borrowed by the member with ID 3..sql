SELECT title FROM Books 
INNER JOIN Borrowings ON Books.book_id = Borrowings.book_id 
WHERE member_id =4 ;