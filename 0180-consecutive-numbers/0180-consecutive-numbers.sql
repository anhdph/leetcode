# Write your MySQL query statement below
with cte as (
    select
        num,
        lag(num, 1) over (order by id) as num_2,
        lag(num, 2) over (order by id) as num_3
    from Logs
)
select distinct num as ConsecutiveNums
from cte
where (num = num_2) and (num_2 = num_3)