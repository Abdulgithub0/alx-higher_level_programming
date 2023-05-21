-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa
USE hbtn_0d_usa;
SELECT id, name FROM states, cities ON states.id = cities.state_id;
