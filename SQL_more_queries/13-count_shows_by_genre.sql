-- the database dump from hbtn_0d_tvshows to your MySQL server
-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tvg.name AS genre, COUNT(tvsg.genre_id) AS number_of_shows
FROM tv_shows AS tvs
INNER JOIN tv_show_genres AS tvsg
ON tvsg.show_id = tvs.id
INNER JOIN tv_genres AS tvg
ON tvg.id = tvsg.genre_id
GROUP BY tvg.name
ORDER BY number_of_shows DESC;
