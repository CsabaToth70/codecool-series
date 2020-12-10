from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_episode_numbers():
    query = '''SELECT s.title, 
    COUNT(e.id) AS number_of_episodes
    FROM shows s
    INNER JOIN seasons ss 
        ON s.id=ss.show_id
    INNER JOIN episodes e
        ON s.id=e.season_id
    GROUP BY s.title;
    '''
    return data_manager.execute_select(query)

