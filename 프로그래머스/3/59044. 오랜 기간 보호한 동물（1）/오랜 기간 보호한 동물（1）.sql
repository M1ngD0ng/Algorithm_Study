-- 코드를 입력하세요
SELECT a.name, a.datetime from animal_ins as a
where animal_id not in (select animal_id from animal_outs)
order by 2
limit 3
