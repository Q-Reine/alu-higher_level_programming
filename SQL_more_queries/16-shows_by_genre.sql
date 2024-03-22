-- the database dump from hbtn_0d_tvshows to your MySQL server
-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT s.title, g.name
FROM tv_shows s LEFT OUTER JOIN tv_show_genres sg
  ON s.id = sg.show_id
  LEFT OUTER JOIN tv_genres g
  ON sg.genre_id = g.id
ORDER BY s.title, g.name;