SELECT title FROM Books 
INNER JOIN Authors ON Books.author_id = Authors.author_id 
WHERE Authors.name = 'George Orwell';