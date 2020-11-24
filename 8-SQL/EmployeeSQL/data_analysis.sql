-- 1. List the following details of each employee: employee number, last name, first name, sex, and salary.
SELECT employees.employee_number
	, employees.last_name
	, employees.first_name
	, employees.sex
	, salaries.salary
	FROM employees, salaries
	WHERE employees.employee_number = salaries.employee_number;

-- 2. List first name, last name, and hire date for employees who were hired in 1986.
SELECT first_name
	, last_name
	, hire_date
	FROM employees
	WHERE DATE(hire_date) BETWEEN DATE('1/1/1986') AND DATE('12/31/1986')	

-- 3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
SELECT departments.dept_number
	, dept_name
	, employees.employee_number
	, last_name
	, first_name
	FROM department_managers
	INNER JOIN departments ON departments.dept_number = department_managers.dept_number
	INNER JOIN employees ON employees.employee_number = department_managers.employee_number

-- 4. List the department of each employee with the following information: employee number, last name, first name, and department name.

-- 5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."

-- 6. List all employees in the Sales department, including their employee number, last name, first name, and department name.

-- 7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

-- 8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

	
	