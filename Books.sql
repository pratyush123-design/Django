CREATE TABLE Books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    author_id INT REFERENCES Authors(author_id),
    category VARCHAR(50),
    published_year INT,
    copies_available INT
);
