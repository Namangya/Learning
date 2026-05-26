CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100)
);

CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE loans (
    loan_id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books(book_id),
    member_id INTEGER REFERENCES members(member_id),
    loan_date DATE
);

INSERT INTO books (title, author) VALUES ('Database Design', 'Author Name');
INSERT INTO members (name) VALUES ('Alice');
INSERT INTO loans (book_id, member_id, loan_date) VALUES (1, 1, '2024-03-01');
