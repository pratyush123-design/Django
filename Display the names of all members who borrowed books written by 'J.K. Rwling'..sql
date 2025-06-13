SELECT Members.name FROM Members
INNER JOIN Borrowings ON Members.member_id = Borrowings.member_id
INNER JOIN Books ON Borrowings.book_id = Books.book_id
INNER JOIN Authors ON Books.author_id = Authors.author_id
WHERE Authors.name = 'J.K. Rwling';