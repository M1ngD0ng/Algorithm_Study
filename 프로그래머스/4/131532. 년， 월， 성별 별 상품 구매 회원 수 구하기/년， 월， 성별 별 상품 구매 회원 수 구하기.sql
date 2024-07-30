-- 코드를 입력하세요
SELECT DATE_FORMAT(os.sales_date,"%Y") as YEAR, 
    DATE_FORMAT(os.sales_date,"%m") as MONTH, 
    ui.GENDER, 
    count(distinct os.user_id) as USERS 
from user_info as ui
join online_sale as os on ui.user_id=os.user_id
where ui.gender is not null
GROUP BY YEAR, MONTH, ui.gender
ORDER BY YEAR, MONTH, ui.gender
