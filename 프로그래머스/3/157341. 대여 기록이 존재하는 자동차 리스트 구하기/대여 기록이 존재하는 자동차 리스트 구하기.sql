-- 코드를 입력하세요
SELECT distinct a.car_id from car_rental_company_car as a
join car_rental_company_rental_history as b
on a.car_id=b.car_id
where a.car_type='세단' and b.start_date >='2022-10-01'
order by 1 desc