-- Task 2.1
# Create Employee Table
CREATE TABLE Employee (
    ID INT,
    F_Name VARCHAR(60),
    L_Name VARCHAR(60),
    Email VARCHAR(60),
    P_Number VARCHAR(60),
    H_Date VARCHAR(60),
    J_ID VARCHAR(60),
    Salary FLOAT,
    C_PCT FLOAT,
    M_ID INT,
    D_ID INT
);


LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Employee.csv'
INTO TABLE Employee
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(
    @ID, @F_Name, @L_Name, @Email, @P_Number, @H_Date, @J_ID, @Salary, @C_PCT, @M_ID, @D_ID
)
SET
    ID = @ID,
    F_Name = @F_Name,
    L_Name = @L_Name,
    Email = @Email,
    P_Number = @P_Number,
    H_Date = @H_Date,
    J_ID = @J_ID,
    Salary = @Salary,
    C_PCT = IFNULL(NULLIF(@C_PCT, ' - '), 0),  
    M_ID = IFNULL(NULLIF(@M_ID, ' - '), 0), -- Convert ' - ' to NULL, then cast to INT
    D_ID = @D_ID;

SELECT *
FROM employee;


SELECT 
	AVG(Salary)
FROM 
	employee;

-- Task 2.4
SELECT
	MAX(salary)
FROM
	employee;
