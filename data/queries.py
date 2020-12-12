from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_actor_data(year):
    query = '''SELECT
    a.id,
    a.name,
    EXTRACT(years FROM AGE(CURRENT_DATE ,a.birthday)) AS actor_age,
    s.year AS released_year
    FROM actors a
    LEFT JOIN show_characters sc
    ON a.id = sc.actor_id
    LEFT JOIN shows s
    ON sc.show_id = s.id
    WHERE s.year = %(y_r)s
    GROUP BY a.id, a.name, s.year
    ORDER BY actor_age DESC;'''
    return data_manager.execute_select(query, {'y_r': year})
