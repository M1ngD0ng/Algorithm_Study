-- 코드를 입력하세요
SELECT user_id, nickname, concat(city, ' ',street_address1,' ',street_address2) as 전체주소,
concat(left(TLNO,3),'-',mid(TLNO,4,4),'-',right(TLNO,4)) as 전화번호
from used_goods_user
where user_id in 
(
    select writer_id from used_goods_board
    group by 1 
    having count(*)>=3
)
order by 1 desc