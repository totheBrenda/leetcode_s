-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/

-- # Write your MySQL query statement below

select contest_id, round(count(distinct Register.user_id) / (select count(distinct user_id) from Users) * 100, 2) as percentage
from Register
group by contest_id
order by 2 desc, 1;