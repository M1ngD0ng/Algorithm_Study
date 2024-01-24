-- 코드를 입력하세요
SELECT a.product_code, sum(a.price*b.sales_amount) as SALES from product as a
join offline_sale as b
on a.product_id = b.product_id
group by 1
order by 2 desc, 1
