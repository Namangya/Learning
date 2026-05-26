CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100)
);

CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    member_id INT,
    loan_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

-- INSERT stubs
INSERT INTO books (title, author) VALUES ('Database Design', 'Author Name');
INSERT INTO members (name) VALUES ('Alice');
INSERT INTO loans (book_id, member_id, loan_date) VALUES (1, 1, '2024-03-01');
