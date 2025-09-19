CREATE DATABASE studentdb;
USE studentdb;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    marks INT
);

INSERT INTO students (name, age, marks) VALUES
('Rahul', 18, 85),
('Priya', 19, 92),
('Aman', 18, 76),
('Simran', 20, 89),
('Arjun', 19, 95);

SELECT * FROM students;
