/* Write your T-SQL query statement below */
with top_user as (
    select top 1 u.name, count(*) as count_rating
    from movierating mr
    join users u on u.user_id = mr.user_id
    group by u.name
    order by count_rating desc, u.name asc
),
top_movie as (
    select top 1 m.title, avg(mr.rating * 1.0) as avg_rating
    from movierating mr
    join movies m on m.movie_id = mr.movie_id
    where mr.created_at >= '2020-02-01' and mr.created_at < '2020-03-01'
    group by m.title
    order by avg_rating desc, m.title asc
)

select name as results from top_user

union all

select title as results from top_movie;