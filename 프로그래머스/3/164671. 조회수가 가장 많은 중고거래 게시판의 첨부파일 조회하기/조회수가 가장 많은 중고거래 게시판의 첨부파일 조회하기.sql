-- 코드를 입력하세요
SELECT concat('/home/grep/src/',f.board_id,'/',f.file_id,f.file_name,f.file_ext) as file_path from used_goods_file as f
where f.board_id = (select b.board_id from used_goods_board as b
                    where b.views = (select max(views) from used_goods_board))
order by 1 desc