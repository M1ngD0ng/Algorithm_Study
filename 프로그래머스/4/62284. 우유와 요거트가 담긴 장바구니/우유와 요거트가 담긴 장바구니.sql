-- 코드를 입력하세요
SELECT distinct a.cart_id  from cart_products as a
inner join cart_products as b
on a.cart_id=b.cart_id
where (a.name='Milk' and b.name='Yogurt') or (a.name='Yogurt' and b.name='Milk')
order by a.cart_id