CREATE VIEW BookAuthors AS
SELECT Books.title, Authors.name AS author_name
FROM Books
INNER JOIN Authors ON Books.author_id = Authors.author_id;