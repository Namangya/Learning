CREATE TABLE books (
    book_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR2(200) NOT NULL,
    author VARCHAR2(100)
);

CREATE TABLE members (
    member_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR2(100) NOT NULL
);

CREATE TABLE loans (
    loan_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    book_id NUMBER REFERENCES books(book_id),
    member_id NUMBER REFERENCES members(member_id),
    loan_date DATE
);

-- INSERT stubs
INSERT INTO books (title, author) VALUES ('Database Design', 'Author Name');
INSERT INTO members (name) VALUES ('Alice');
INSERT INTO loans (book_id, member_id, loan_date) VALUES (1, 1, DATE '2024-03-01');
COMMIT;
