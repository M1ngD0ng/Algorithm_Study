-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME from ANIMAL_INS where ANIMAL_TYPE='Dog' and upper(NAME) like upper('%EL%') order by name asc;