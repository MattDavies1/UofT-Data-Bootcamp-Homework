CREATE TABLE titles (
	title_id VARCHAR(255) PRIMARY KEY NOT NULL,
	title VARCHAR(255)
);

CREATE TABLE employees (
	employee_number INT PRIMARY KEY NOT NULL,
	title_id VARCHAR(255),
	FOREIGN KEY (title_id) REFERENCES titles(title_id),
	birth_date VARCHAR(255),
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	sex VARCHAR(255),
	hire_date VARCHAR(255)
);

CREATE TABLE salaries (
	id SERIAL NOT NULL,
	employee_number INT,
	FOREIGN KEY (employee_number) REFERENCES employees(employee_number),
	salary INT
);

CREATE TABLE departments(
	dept_number VARCHAR(255) PRIMARY KEY NOT NULL,
	dept_name VARCHAR(255)
);

CREATE TABLE department_managers(
	dept_number VARCHAR(255),
	FOREIGN KEY (dept_number) REFERENCES departments(dept_number),
	employee_number INT,
	FOREIGN KEY (employee_number) REFERENCES employees(employee_number)
);

CREATE TABLE dept_emp(
	employee_number INT,
	FOREIGN KEY (employee_number) REFERENCES employees(employee_number),
	dept_number VARCHAR(255),
	FOREIGN KEY (dept_number) REFERENCES departments(dept_number)
);
