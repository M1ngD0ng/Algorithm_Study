-- 코드를 입력하세요
SELECT b.ingredient_type, sum(a.total_order) as total_order from first_half as a
join icecream_info as b
on a.flavor=b.flavor
group by 1
order by 2 
