-- 코드를 작성해주세요
select a.emp_no, a.emp_name, b.grade, 
case when b.grade='S' then a.sal*0.2
    when b.grade='A' then a.sal*0.15
    when b.grade='B' then a.sal*0.1
    else 0
    end as BONUS
from hr_employees as a
join (select emp_no, case when avg(score)>=96 then 'S'
    when avg(score)>=90 then 'A'
    when avg(score)>=80 then 'B'
    else 'C'
    end as GRADE from hr_grade
     where year=2022
     group by emp_no) as b
on a.emp_no=b.emp_no
order by a.emp_no