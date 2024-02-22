-- 코드를 입력하세요
SELECT * from places
where host_id in (select host_id from places 
                  group by 1
                  having count(*)>=2)
order by id