# Write your MySQL query statement below
/* Write your T-SQL query statement below */
select
    request_at as Day,
    round(
        sum(
            case
                when status != 'completed' then 1
                else 0
            end
        ) / count(request_at)
        , 2
     ) as 'Cancellation Rate'
from Trips T
where request_at between '2013-10-01' and '2013-10-03'
and client_id not in (
    select users_id from Users where banned = 'Yes'
)
and driver_id not in (
    select users_id from Users where banned = 'Yes'
)
group by 1