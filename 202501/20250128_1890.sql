-- https://leetcode.com/problems/the-latest-login-in-2020/

-- # Write your MySQL query statement below

select user_id, max(time_stamp) as last_stamp
from Logins
-- where time_stamp >= '20200101' and time_stamp < '20210101'
where year(time_stamp) = 2020
-- where time_stamp like '2020%'
group by user_id;