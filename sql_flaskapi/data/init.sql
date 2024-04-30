CREATE DATABASE student_flask;
USE student_flask;

CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    school VARCHAR(255) NOT NULL
);

INSERT INTO student (name, age, school) VALUES ('John Doe', 20, 'ABC High School');

INSERT INTO student (name, age, school) VALUES 
('Jane Smith', 22, 'XYZ College'),
('Alice Johnson', 21, 'DEF Academy'),
('Bob Brown', 19, 'GHI School');
