from data import data_manager
from psycopg2.extras import RealDictCursor
from psycopg2 import sql
import datetime

def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


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


def get_ordered_shows(starting_row, ordered_by='Rating', order_direction=True):
    if order_direction:
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
        ORDER BY {asp} DESC
        LIMIT 15 OFFSET %(s_w)s;'''
    else:
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
        ORDER BY {asp} ASC
        LIMIT 15 OFFSET %(s_w)s;'''
    return data_manager.execute_select(sql.SQL(query).format(asp=sql.Identifier(ordered_by)),
                                       variables={'s_w': starting_row})


def get_one_show_data(show_id):
    query = '''SELECT s.id AS "id",
       title AS "Title",
       year AS "Year",
       runtime AS "Runtime",
       ROUND(rating, 1) AS "Rating",
       STRING_AGG(DISTINCT g.name::text, ', ' ) AS "Genres",
       trailer AS "Trailer",
       homepage AS "Homepage",
       ARRAY_TO_STRING((ARRAY_AGG(DISTINCT a.name))[1:3], ', ') AS "Actors"
    FROM shows s
    INNER JOIN show_genres sg
        ON s.id=sg.show_id
    INNER JOIN genres g
        ON sg.genre_id = g.id
    INNER JOIN show_characters sc
        ON s.id = sc.show_id
    INNER JOIN actors a
        ON sc.actor_id = a.id
    WHERE s.id = %(s_d)s
    GROUP BY s.id, s.title, s.year, s.runtime, s.rating, s.trailer, s.homepage;'''
    return data_manager.execute_select(query, variables={'s_d': show_id})

