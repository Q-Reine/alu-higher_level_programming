-- Import the database dump of hbtn_0d_tvshows to your MySQL server
SELECT tvs.title, tvsg.genre_id
FROM tv_shows AS tvs
INNER JOIN tv_show_genres AS tvsg
ON tvsg.show_id = tvs.id
ORDER BY tvs.title, tvsg.genre_id;