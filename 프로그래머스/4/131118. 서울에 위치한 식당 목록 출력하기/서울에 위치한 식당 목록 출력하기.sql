-- 코드를 입력하세요
SELECT ri.rest_id, ri.rest_name, ri.food_type, ri.favorites, ri.address, round(avg(review_score),2) as score from rest_review as rr
join rest_info as ri
on rr.rest_id=ri.rest_id
where left(ri.address,2)='서울'
group by ri.rest_id
order by score desc, ri.favorites desc