-- 코드를 입력하세요
SELECT a.user_id, a.nickname, sum(b.price) as total_sales from used_goods_user as a, used_goods_board as b
where a.user_id=b.writer_id and b.status='DONE'
group by 1
having sum(b.price) >=700000
order by 3