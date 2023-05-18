-- a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
-- rows without a name value are not listed and the result set is mainly score and name attributes in display in descending order of score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
