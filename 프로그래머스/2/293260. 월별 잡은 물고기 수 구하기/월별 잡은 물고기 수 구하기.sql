select count(*) as FISH_COUNT, cast(date_format(time, '%c') as signed) as MONTH
from fish_info
group by 2
order by 2