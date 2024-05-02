USE studentdb;

CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    school VARCHAR(255) NOT NULL
);

INSERT INTO student (name, age, school) VALUES ('Jessi', 20, 'SUTD');

INSERT INTO student (name, age, school) VALUES 
('Jane Smith', 22, 'NTU'),
('Alice Johnson', 21, 'NUS'),
('Bob Brown', 19, 'Temasek poly');
