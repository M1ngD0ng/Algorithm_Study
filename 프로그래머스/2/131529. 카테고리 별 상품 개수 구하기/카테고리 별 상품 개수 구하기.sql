-- 코드를 입력하세
SELECT left(product_code,2) as category, count(product_id) as products from product group by left(product_code,2)