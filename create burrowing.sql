CREATE TABLE Borrowings (
    borrowing_id SERIAL PRIMARY KEY,
    book_id INT REFERENCES Books(book_id),
    member_id INT REFERENCES Members(member_id),
    borrowed_date DATE,
    return_date DATE
);