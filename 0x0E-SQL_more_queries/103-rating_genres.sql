-- lists all genres by their rating
SELECT name, SUM(rate) AS rating
FROM tv_genres AS ge
INNER JOIN tv_show_genres AS sg
ON sg.genre_id = ge.id
INNER JOIN tv_show_ratings AS sr
ON sr.show_id = sg.show_id
GROUP BY ge.name
ORDER BY rating DESC;