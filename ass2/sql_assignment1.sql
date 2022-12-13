CREATE TABLE dept (
	dept_no INT PRIMARY KEY,
    d_name VARCHAR (21),
    loc VARCHAR (21)
);

CREATE TABLE emp (
	emp_no INT PRIMARY KEY NOT NULL,
    e_name VARCHAR (25),
    sal INT,
    hire_date DATE,
    commission INT,
    mrg INT,
    dept_no INT, 
    FOREIGN KEY (dept_no) REFERENCES dept(dept_no) ON DELETE SET NULL
    
    
);

INSERT INTO dept VALUES(10,'Accounts','Bangalore');
INSERT INTO dept VALUES(20,'IT','Delhi');
INSERT INTO dept VALUES(30,'Production','Chennai');
INSERT INTO dept VALUES(40,'Sales','Hyd');
INSERT INTO dept VALUES(50,'Admn','London');
SELECT * FROM dept;

INSERT INTO emp VALUES(1001, 'Sachin',19000,'1980-1-1',2100,1003,20);
INSERT INTO emp VALUES(1002, 'Kapil',15000,'1970-1-1',2300,1003,10);
INSERT INTO emp VALUES(1003, 'Stefen',12000,'1990-1-1',500,1007,20);
INSERT INTO emp VALUES(1004, 'Williams',9000,'2001-1-1',null,1007,30);
INSERT INTO emp VALUES(1005, 'John',5000,'2005-1-1',null,1006,30);
INSERT INTO emp VALUES(1006, 'Dravid',19000,'1985-1-1',2400,1007,10);
INSERT INTO emp VALUES(1007, 'Martin',21000,'2000-1-1',1040,null,null);
SELECT * FROM emp;

-- 1: select employee details of dept number 10 or 30
	SELECT *
    FROM emp
    WHERE dept_no = 10 OR dept_no = 30;
    
-- 2: Write a query to fetch all the dept details with more than 1 Employee
	SELECT  d.*
    FROM emp AS e, dept AS d
    WHERE e.dept_no = d.dept_no AND (e.dept_no)>1
    GROUP BY d.dept_no;
    
-- 3: Write a query to fetch employee details whose name starts with the letter “S”
	SELECT *
    FROM emp
    WHERE e_name LIKE 'S%';

-- 4: Select Emp Details Whose experience is more than 2 years
	SELECT *
    FROM emp
    WHERE hire_date > 2020-1-1;

-- 5: Write a SELECT statement to replace the char “a” with “#” in Employee Name ( Ex:  Sachin as S#chin)
	UPDATE emp
    SET e_name =  REPLACE(e_name,'a','#');
    select e_name from emp;
	
-- 6: Write a query to fetch employee name and his/her manager name. 
	SELECT e.e_name, m.e_name
    FROM emp AS e, emp AS m
    WHERE e.emp_no = m.mrg;
    
-- 7: Fetch Dept Name , Total Salry of the Dept
	SELECT SUM(e.sal), d.d_name
    FROM emp AS e, dept As d
	WHERE d.dept_no = e.dept_no
    GROUP BY d.d_name;

-- 8: Write a query to fetch ALL the  employee details along with department name, department location, irrespective of employee existance in the department.
	SELECT emp.*, d_name, loc
    FROM emp
    JOIN dept
    ON emp.dept_no = dept.dept_no;

-- 9: Write an update statement to increase the employee salary by 10 %
	UPDATE emp
    SET sal = ((sal * 0.1) + sal);

-- 10: Write a statement to delete employees belong to Chennai location.
	DELETE 
    FROM emp
    WHERE dept_no = 30;

-- 11: Get Employee Name and gross salary (sal + comission) .
	SELECT e_name, (sal + commission) AS gross_salary
    FROM emp;
    

-- 12: Increase the data length of the column Ename of Emp table from  100 to 250 using ALTER statement
	ALTER TABLE emp
	MODIFY e_name
	varchar(225);

-- 13: Write query to get current datetime
	SELECT CURRENT_DATE(), CURRENT_TIME();

-- 14: Write a statement to create STUDENT table, with related 5 columns
	CREATE TABLE student(
		s_id INT PRIMARY KEY,
        s_name VARCHAR(50),
        s_add VARCHAR(101),
        s_phone_no INT,
        s_percentage INT
    );

-- 15:  Write a query to fetch number of employees in who is getting salary more than 10000
	SELECT COUNT(e_name)
    FROM emp
    WHERE sal > 10000;

-- 16: Write a query to fetch minimum salary, maximum salary and average salary from emp table.
	SELECT AVG(sal), MIN(sal), MAX(sal)
    FROM emp;

-- 17: Write a query to fetch number of employees in each location
	SELECT COUNT(e.emp_no), d.loc
    FROM emp AS e, dept AS d
    WHERE e.dept_no = d.dept_no
    GROUP BY d.loc;

-- 18: Write a query to display emplyee names in descending order
	SELECT e_name
    FROM emp
    ORDER BY e_name DESC;

-- 19: Write a statement to create a new table(EMP_BKP) from the existing EMP table
	CREATE TABLE EMP_BKP LIKE emp;

-- 20: Write a query to fetch first 3 characters from employee name appended with salary.
	SELECT LEFT(e_name, 3)
    FROM emp;

-- 21: Get the details of the employees whose name starts with S
	SELECT *
    FROM emp
    WHERE e_name LIKE 's%';

-- 22: Get the details of the employees who works in Bangalore location
	SELECT *
	FROM emp
	WHERE dept_no = 10;

-- 23:  Write the query to get the employee details whose name started within  any letter between  A and K
	SELECT *
    FROM emp
    WHERE e_name BETWEEN 'a%' AND 'k%';

-- 24: Write a query in SQL to display the employees whose manager name is Stefen
	SELECT *
    FROM emp
    WHERE mrg = 1003;

-- 25:  Write a query in SQL to list the name of the managers who is having maximum number of employees working under him
	SELECT e.e_name, COUNT(e.emp_no)
    FROM emp AS e
   -- WHERE e.emp_no = e.mrg
    GROUP BY e.mrg
    ORDER BY COUNT(e.emp_no) DESC;

-- 26: Write a query to display the employee details, department details and the manager details of the employee who has second highest salary
	SELECT emp.*, dept.*
	FROM emp 
	JOIN dept
	ON emp.dept_no = dept.dept_no
	WHERE sal < (SELECT MAX(sal) FROM emp) 
    ORDER BY sal DESC
    LIMIT 1;
   
-- 27: Write a query to list all details of all the managers
	SELECT e.*
    FROM emp AS e
    WHERE e.emp_no IN (SELECT mrg FROM emp);

-- 28: Write a query to list the details and total experience of all the managers
   SELECT (EXTRACT(YEAR FROM hire_date) - 2022)*(-1) AS tot_experience, e.*
   FROM emp AS e
   WHERE emp_no IN (SELECT mrg FROM emp); 
    
-- 29:  Write a query to list the employees who is manager and  takes commission less than 1000 and works in Delhi
	SELECT e.e_name
    FROM emp AS e, dept AS d
    WHERE e.emp_no IN (SELECT mrg FROM emp) AND commission < 1000 AND d.dept_no = 20;

-- 30: Write a query to display the details of employees who are senior to Martin
	SELECT *
    FROM emp
    WHERE hire_date > '2000-01-01';

