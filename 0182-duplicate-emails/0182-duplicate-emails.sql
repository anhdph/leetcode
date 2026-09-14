/* Write your T-SQL query statement below */
select distinct p1.email as Email
from Person p1
join Person p2
on p1.email = p2.email
where p1.id <> p2.id