-- 코드를 입력하세요
SELECT order_id, product_id, left(out_date,10) as out_date,
case
when out_date > '2022-05-02' then '출고대기'
when out_date is null then '출고미정'
else '출고완료'
end as '출고여부'
from food_order
order by 1