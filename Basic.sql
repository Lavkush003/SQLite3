-- Create table
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks INTEGER
);

-- Insert records
INSERT INTO students (name, marks) VALUES ('Rahul', 85);
INSERT INTO students (name, marks) VALUES ('Anita', 92);
INSERT INTO students (name, marks) VALUES ('Vikas', 78);

-- Fetch all records
SELECT * FROM students;
