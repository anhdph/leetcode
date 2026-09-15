# Write your MySQL query statement below
with cte as (
    select id, visit_date, people,
    id - row_number() over (order by id) as group_id
    from Stadium
    where people >= 100
)
select id, visit_date, people
from cte
where group_id in (
    select group_id
    from cte
    group by 1
    having count(group_id) >= 3
)