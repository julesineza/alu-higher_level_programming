-- A script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in my MySQL server.
-- Records should be ordered by score in descing order 
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;