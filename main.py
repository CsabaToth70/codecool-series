from flask import Flask, render_template, url_for
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')

@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/length')
def get_number_of_episodes():
    shows_episode_data = queries.get_episode_numbers()
    table_heads = []
    for head in shows_episode_data[0].keys():
        table_heads.append(head)
    for i, row in enumerate(shows_episode_data):
        if row[table_heads[1]] >= 100:
            row['is_long'] = True
        else:
            row['is_long'] = False
    print(shows_episode_data)
    return render_template('length.html', table_heads=table_heads, shows_episode_data=shows_episode_data)


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
