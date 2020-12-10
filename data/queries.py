from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_age(start_date, end_date):
    query = '''SELECT a.id, 
    CASE
     WHEN a.death is not null
        THEN CONCAT ('+', a.name)
        ELSE a.name
    END AS name, 
    CASE
     WHEN a.death is null
        THEN EXTRACT(year FROM CURRENT_DATE) - EXTRACT(year FROM a.birthday)
     ELSE 
        EXTRACT(year FROM a.death) - EXTRACT(year FROM a.birthday)
    END AS age,
    COUNT(s.id) 
    FROM actors a
    LEFT JOIN show_characters s 
    ON a.id = s.actor_id
    WHERE a.birthday between %(s_e)s and %(e_e)s
    GROUP BY a.id
    ORDER BY a.name DESC
    '''
    return data_manager.execute_select(query, {'s_e': start_date, 'e_e': end_date})
