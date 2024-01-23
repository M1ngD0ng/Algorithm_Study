-- 코드를 입력하세요
SELECT extract(hour from datetime) as 'hour',
count(*) as 'count'
from animal_outs
where extract(hour from datetime)>=9 and extract(hour from datetime)<20
group by extract(hour from datetime)
order by 1