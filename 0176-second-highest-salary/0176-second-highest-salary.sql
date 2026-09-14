with highest_salary as (
    select max(salary) as salary
    from employee
)

select max(salary) as SecondHighestSalary
from employee
where salary < (select salary from highest_salary)