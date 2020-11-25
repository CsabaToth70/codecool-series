from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')



def get_most_rated():
    query = '''SELECT s.id,
       title,
       year AS "release year",
       runtime,
       ROUND(rating, 1) AS rated,
       STRING_AGG( name::text, ', ' ORDER BY name) AS genres,
       trailer AS "link to trailer",
       homepage
    FROM shows s
    INNER JOIN show_genres sg
        ON s.id=sg.show_id
    INNER JOIN genres g
        ON sg.genre_id = g.id
    GROUP BY s.id, s.title, s.year, s.runtime, s.rating, s.trailer, s.homepage
    ORDER BY rated DESC
    LIMIT 15;'''
    return data_manager.execute_select(query)

