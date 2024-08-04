-- 코드를 작성해주세요
select a.id, case when CHILD_COUNT is null then 0
      else CHILD_COUNT end as CHILD_COUNT
from ecoli_data as a
left join (select parent_id, 
      case when parent_id is null then 0
      else count(*) 
      end as CHILD_COUNT from ecoli_data
     group by parent_id) as b
on a.id=b.parent_id
order by a.id