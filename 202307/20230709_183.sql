-- ## https://leetcode.com/problems/customers-who-never-order/

-- # Write your MySQL query statement below

select name as Customers
from Customers
left join Orders on Orders.customerId = Customers.id
where Orders.customerId is Null;