-- the database dump from hbtn_0d_tvshows to your MySQL server
-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT s.title
FROM tv_genres g INNER JOIN tv_show_genres sg
  ON g.id = sg.genre_id
  INNER JOIN tv_shows s
  ON sg.show_id = s.id
WHERE g.name = 'Comedy'
ORDER BY s.title;
