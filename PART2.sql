USE studentdb;

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    total_classes INT,
    attended_classes INT,
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Sample data
INSERT INTO attendance (student_id, total_classes, attended_classes) VALUES
(1, 40, 36),  -- Rahul
(2, 40, 38),  -- Priya
(3, 40, 28),  -- Aman
(4, 40, 34),  -- Simran
(5, 40, 39);  -- Arjun
