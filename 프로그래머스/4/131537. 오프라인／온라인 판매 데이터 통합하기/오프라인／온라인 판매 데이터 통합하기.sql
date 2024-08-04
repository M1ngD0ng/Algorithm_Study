(select left(SALES_DATE,10) as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT from online_sale as a
where left(SALES_DATE,7)='2022-03'
union
select left(SALES_DATE,10) as SALES_DATE, PRODUCT_ID, null as USER_ID, SALES_AMOUNT from offline_sale as b
where left(SALES_DATE,7)='2022-03')
order by SALES_DATE, PRODUCT_ID, USER_ID
