-- 코드를 입력하세요
SELECT user_id, product_id  from online_sale
group by 1, 2
having count(product_id)>1
order by 1 asc, 2 desc