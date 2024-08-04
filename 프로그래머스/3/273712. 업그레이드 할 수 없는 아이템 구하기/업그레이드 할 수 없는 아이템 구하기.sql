-- 코드를 작성해주세요
select ITEM_ID, ITEM_NAME, RARITY from item_info
where item_id not in (select ifnull(parent_item_id,-1) from item_tree
                     group by parent_item_id)
order by item_id desc
                     