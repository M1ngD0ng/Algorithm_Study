select count(*) as FISH_COUNT, a.fish_name as FISH_NAME from fish_name_info as a
join fish_info as b
on a.fish_type=b.fish_type
group by 2
order by 1 desc
