-- a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in MySQL server.
-- Results set display both the score and the name in descending order of scores
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
