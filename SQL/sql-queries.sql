-- SELECT DISTINCT (e.first_name), e.last_name, t.title
-- FROM employees AS e 
-- INNER JOIN titles AS t 
-- ON e.emp_no = t.emp_no
-- INNER JOIN dept_emp AS d_emp
-- ON e.emp_no = d_emp.emp_no
-- INNER JOIN departments AS d
-- ON d.dept_no = d_emp.dept_no
-- LIMIT 10;

SELECT DISTINCT first_name, last_name, titles.title 
FROM employees
INNER JOIN titles
ON employees.emp_no = titles.emp_no
LIMIT 10;