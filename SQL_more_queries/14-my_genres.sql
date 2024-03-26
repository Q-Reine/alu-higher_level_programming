-- the database dump from hbtn_0d_tvshows to your MySQL server
-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT g.name AS name
FROM tv_shows s INNER JOIN tv_show_genres sg
  ON s.id = sg.show_id
INNER JOIN tv_genres g
  ON sg.genre_id = g.id
WHERE s.title = 'Dexter'
ORDER BY g.name;
