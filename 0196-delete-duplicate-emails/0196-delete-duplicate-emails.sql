/* Write your T-SQL query statement below */
with cte as (
    select p1.id, p1.email,
    row_number() over (partition by p1.email order by p1.id asc) as row_num
    from Person p1
)
delete from cte
where row_num > 1