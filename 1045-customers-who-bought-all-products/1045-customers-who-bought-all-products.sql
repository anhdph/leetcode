/* Write your T-SQL query statement below */
select distinct customer_id
from Customer c
join Product p on p.product_key = c.product_key
group by customer_id
having count(distinct c.product_key) = (
    select count(*) from Product
)