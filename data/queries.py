from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

# Title, Year, Runtime (min), Rating, Genres, Trailer, Homepage

def get_most_rated(starting_row: int):
    query = '''SELECT s.id AS "id",
       title AS "Title",
       year AS "Year",
       runtime AS "Runtime (min)",
       ROUND(rating, 1) AS "Rating",
       STRING_AGG( name::text, ', ' ORDER BY name) AS "Genres",
       trailer AS "Trailer",
       homepage AS "Homepage"
    FROM shows s
    INNER JOIN show_genres sg
        ON s.id=sg.show_id
    INNER JOIN genres g
        ON sg.genre_id = g.id
    GROUP BY s.id, s.title, s.year, s.runtime, s.rating, s.trailer, s.homepage
    ORDER BY Rating DESC
    LIMIT 15 OFFSET %(s_w)s;'''
    return data_manager.execute_select(query, variables={'s_w': starting_row})


def get_number_of_all():
    query = '''SELECT COUNT(*) FROM (SELECT s.id AS "id",
       title AS "Title",
       year AS "Year",
       runtime AS "Runtime (min)",
       ROUND(rating, 1) AS "Rating",
       STRING_AGG( name::text, ', ' ORDER BY name) AS "Genres",
       trailer AS "Trailer",
       homepage AS "Homepage"
    FROM shows s
    INNER JOIN show_genres sg
        ON s.id=sg.show_id
    INNER JOIN genres g
        ON sg.genre_id = g.id
    GROUP BY s.id, s.title, s.year, s.runtime, s.rating, s.trailer, s.homepage
    ORDER BY Rating DESC) AS foo;'''
    return data_manager.execute_select(query)


def get_all_by_rating():
    query = '''SELECT s.id AS "id",
       title AS "Title",
       year AS "Year",
       runtime AS "Runtime (min)",
       ROUND(rating, 1) AS "Rating",
       STRING_AGG( name::text, ', ' ORDER BY name) AS "Genres",
       trailer AS "Trailer",
       homepage AS "Homepage"
    FROM shows s
    INNER JOIN show_genres sg
        ON s.id=sg.show_id
    INNER JOIN genres g
        ON sg.genre_id = g.id
    GROUP BY s.id, s.title, s.year, s.runtime, s.rating, s.trailer, s.homepage
    ORDER BY Rating DESC;'''
    return data_manager.execute_select(query)

