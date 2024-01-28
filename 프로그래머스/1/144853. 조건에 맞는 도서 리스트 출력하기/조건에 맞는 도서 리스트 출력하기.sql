-- 코드를 입력하세요
SELECT book_id, left(published_date,10) from book
where published_date like '2021-%'
    and category='인문'
order by 2