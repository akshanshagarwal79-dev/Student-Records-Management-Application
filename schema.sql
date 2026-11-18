CREATE DATABASE IF NOT EXISTS student;
USE student;

CREATE TABLE IF NOT EXISTS admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS student (
    rollno INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    fname VARCHAR(100),
    gender VARCHAR(20),
    dob DATE,
    address TEXT,
    phone VARCHAR(20),
    course VARCHAR(100),
    section VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS marks (
    rollno INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    father_name VARCHAR(100),
    class VARCHAR(100),
    section VARCHAR(20),
    subject1 VARCHAR(100), marks1 INT NOT NULL,
    subject2 VARCHAR(100), marks2 INT NOT NULL,
    subject3 VARCHAR(100), marks3 INT NOT NULL,
    subject4 VARCHAR(100), marks4 INT NOT NULL,
    subject5 VARCHAR(100), marks5 INT NOT NULL,
    total_marks INT NOT NULL,
    percentage DECIMAL(5,2) NOT NULL,
    grade VARCHAR(2) NOT NULL,
    CONSTRAINT fk_marks_student FOREIGN KEY (rollno) REFERENCES student(rollno)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create the initial administrator record only if one does not already exist.
-- Change this temporary password immediately after first login.
INSERT INTO admin (password)
SELECT 'admin123' WHERE NOT EXISTS (SELECT 1 FROM admin);
