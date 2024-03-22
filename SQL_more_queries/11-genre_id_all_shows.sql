-- Import the database dump of hbtn_0d_tvshows to your MySQL server
SELECT s.title AS title, g.genre_id AS genre_id
FROM tv_shows s LEFT OUTER JOIN tv_show_genres g
  ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
