-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT c.name, c.id FROM states s, cities c WHERE s.name = 'California' AND s.id = c.state_id ORDER BY c.id;
