-- 코드를 입력하세요
SELECT a.apnt_no, p.pt_name, p.pt_no, d.mcdp_cd, d.dr_name, a.apnt_ymd from appointment as a
join patient as p on a.pt_no=p.pt_no
join doctor as d on a.mddr_id=d.dr_id
where a.apnt_cncl_yn='N'
and left(a.apnt_ymd,10)='2022-04-13'
and d.mcdp_cd='CS'
order by a.apnt_ymd