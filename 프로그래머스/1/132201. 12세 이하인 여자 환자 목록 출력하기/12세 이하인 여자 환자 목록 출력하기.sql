-- 코드를 입력하세요
SELECT pt_name, pt_no, gend_cd, age, if(tlno is null, 'NONE', tlno) as tlno
from patient
where age<13 and gend_cd='W'
order by 4 desc, 1 asc