-- https://leetcode.com/problems/game-play-analysis-i/

-- # Write your MySQL query statement below

select player_id, min(event_date) as first_login
from Activity
group by player_id
order by player_id;