-- Lists all cities contained in the database hbtn_0d_usa
SELECT * cities.id, cities.name
FROM cities
WHERE cities.state_id
ORDER BY cities.id;
