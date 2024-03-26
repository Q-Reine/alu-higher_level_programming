-- -- the database dump from hbtn_0d_tvshows to your MySQL server
SELECT tvs.title, tvsg.genre_id
FROM tv_shows AS tvs
LEFT JOIN tv_show_genres AS tvsg
ON tvsg.show_id = tvs.id
WHERE tvsg.genre_id IS NULL
ORDER BY tvs.title, tvsg.genre_id;