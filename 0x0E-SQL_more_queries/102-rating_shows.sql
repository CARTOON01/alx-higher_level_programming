-- This script lists all shows from "hbtn_0d_tvshows_rate" by their rating
SELECT sh.title, SUM(sr.rate) AS rating
FROM tv_shows AS sh
INNER JOIN tv_show_ratings AS sr
ON sh.id = sr.show_id
GROUP BY sh.title
ORDER BY rating DESC