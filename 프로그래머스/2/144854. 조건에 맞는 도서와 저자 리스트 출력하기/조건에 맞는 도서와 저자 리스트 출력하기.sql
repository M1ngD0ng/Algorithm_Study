-- 코드를 입력하세요
SELECT a.book_id, b.author_name, left(a.published_date,10) as published_date from book as a
join author as b
on a.author_id=b.author_id
where a.category='경제'
order by 3