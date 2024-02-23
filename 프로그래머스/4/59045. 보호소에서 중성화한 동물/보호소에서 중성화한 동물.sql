-- 코드를 입력하세요
SELECT a.animal_id, a.animal_type, a.name from animal_outs as a
join animal_ins as b
on a.animal_id=b.animal_id
where b.sex_upon_intake like 'intact%' and ( a.sex_upon_outcome like 'spayed%' or a.sex_upon_outcome like 'neutered%')
order by 1