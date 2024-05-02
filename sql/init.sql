USE employeedb;

CREATE TABLE employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL
);

INSERT INTO employee (name, age) VALUES ('John Doe', 20);

INSERT INTO employee (name, age) VALUES 
('Jane Smith', 22),
('Alice Johnson', 21),
('Bob Brown', 19);
