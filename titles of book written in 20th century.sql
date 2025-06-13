SELECT title FROM Books 
INNER JOIN Authors ON Books.author_id = Authors.author_id 
WHERE Authors.birth_year BETWEEN 1901 AND 2000;