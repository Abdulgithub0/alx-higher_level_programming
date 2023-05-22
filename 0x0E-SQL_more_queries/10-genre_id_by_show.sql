-- import the database dump from hbtn_0d_tvshows to your MySQL server:
-- 	This script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- 	Each record  display: tv_shows.title - tv_show_genres.genre_id
-- 	Results set are sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- 	The database name will be passed as an argument of the mysql command
SELECT s.title, t.genre_id FROM tv_show_genres t, tv_shows s WHERE s.id = t.show_id ORDER BY s.title, t.genre_id;
