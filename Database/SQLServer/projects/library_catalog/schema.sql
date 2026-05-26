CREATE TABLE books (
    book_id INT IDENTITY(1,1) PRIMARY KEY,
    title NVARCHAR(200) NOT NULL,
    author NVARCHAR(100)
);

CREATE TABLE members (
    member_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL
);

CREATE TABLE loans (
    loan_id INT IDENTITY(1,1) PRIMARY KEY,
    book_id INT REFERENCES books(book_id),
    member_id INT REFERENCES members(member_id),
    loan_date DATE
);

-- INSERT stubs
INSERT INTO books (title, author) VALUES (N'Database Design', N'Author Name');
INSERT INTO members (name) VALUES (N'Alice');
INSERT INTO loans (book_id, member_id, loan_date) VALUES (1, 1, '2024-03-01');
