CREATE DATABASE IT_Servicedesk;

USE IT_Servicedesk;
CREATE TABLE Department (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    email VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);
CREATE TABLE Tickets (
    ticket_id INT PRIMARY KEY,
    issue VARCHAR(100),
    status VARCHAR(20),
    priority VARCHAR(20),
    emp_id INT,
    created_date DATE,
    FOREIGN KEY (emp_id) REFERENCES Employee(emp_id)
);

INSERT INTO Department VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance');

INSERT INTO Employee VALUES
(101, 'Rahul', 'rahul@gmail.com', 1),
(102, 'Priya', 'priya@gmail.com', 2),
(103, 'Arjun', 'arjun@gmail.com', 1),
(104, 'Sneha', 'sneha@gmail.com', 3);

INSERT INTO Tickets VALUES
(1001, 'Network Issue', 'Open', 'High', 101, '2026-11-10'),
(1002, 'Login Problem', 'Closed', 'Medium', 102, '2026-11-11'),
(1003, 'System Error', 'Open', 'High', 103, '2026-11-12'),
(1004, 'Software Installation', 'Pending', 'Low', 104, '2026-11-13');

SELECT * FROM Tickets;
SELECT * FROM Employee;

SELECT * FROM Tickets
WHERE status = 'Open';

SELECT * FROM Tickets
WHERE priority = 'High';

UPDATE Tickets
SET status = 'Closed'
WHERE ticket_id = 1001;

UPDATE Tickets
SET priority = 'Medium'
WHERE ticket_id = 1003;

SELECT Tickets.ticket_id,
       Tickets.issue,
       Tickets.status,
       Employee.emp_name
FROM Tickets
INNER JOIN Employee
ON Tickets.emp_id = Employee.emp_id;

SELECT status, COUNT(*) AS total_tickets
FROM Tickets
GROUP BY status;

ALTER TABLE Employee
MODIFY emp_name VARCHAR(50) NOT NULL;

ALTER TABLE Tickets
ADD CONSTRAINT chk_ticket_status
CHECK (status IN ('Open', 'Closed', 'Pending'));