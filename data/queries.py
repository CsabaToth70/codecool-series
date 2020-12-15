from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_shows_by_genre(genre_id):
    query = '''
    SELECT s.id, s.title, 
    COUNT(DISTINCT s2.id) AS season_number, 
    COUNT(e.id) AS episode_number
    FROM shows s
    INNER JOIN seasons s2 ON s.id = s2.show_id
    INNER JOIN episodes e on s2.id = e.season_id
    INNER JOIN show_genres sg on s.id = sg.show_id
    INNER JOIN genres g on g.id = sg.genre_id
    WHERE g.id = %(g_d)s
    GROUP BY s.id
    HAVING COUNT(e.id) > 20
    ORDER BY COUNT(e.id) DESC
    LIMIT 50;'''
    return data_manager.execute_select(query, {'g_d': genre_id})


def get_genre_list():
    return data_manager.execute_select('SELECT * FROM genres;')