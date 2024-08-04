-- 코드를 입력하세요
SELECT a.author_id, a.author_name, b.category, sum(bs.sales*b.price) as TOTAL_SALES 
from book as b
join author as a on b.author_id=a.author_id
join book_sales as bs on b.book_id=bs.book_id
where left(bs.sales_date,7)='2022-01'
group by a.author_id, b.category
order by a.author_id asc, b.category desc