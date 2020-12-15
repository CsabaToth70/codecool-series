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


@app.route('/get_genres')
def get_genres():
    genre_list = queries.get_genre_list()
    return render_template('genre.html', genre_list=genre_list)


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
