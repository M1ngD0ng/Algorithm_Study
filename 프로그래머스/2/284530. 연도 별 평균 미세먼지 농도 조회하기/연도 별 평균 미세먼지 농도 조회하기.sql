select cast(left(YM, 4) as signed) as YEAR, round(avg(PM_VAL1),2) as 'PM10', round(avg(PM_VAL2),2) as 'PM2.5' from air_pollution
where LOCATION2='수원'
group by 1
order by 1