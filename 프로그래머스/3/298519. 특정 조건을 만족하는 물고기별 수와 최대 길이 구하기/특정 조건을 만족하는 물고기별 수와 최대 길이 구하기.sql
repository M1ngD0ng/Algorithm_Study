-- 코드를 작성해주세요
select cnt as FISH_COUNT, MAX_LENGTH, FISH_TYPE
from (select fish_type, count(*) as cnt, avg(ifnull(length,10)) as avg_length, max(length) as max_length 
      from fish_info
     group by fish_type) as a
where avg_length>=33
order by fish_type