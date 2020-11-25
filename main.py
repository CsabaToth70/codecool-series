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


@app.route('/shows/most-rated')
def display_most_rated():
    page_title = 'Most rated shows'
    shows_to_display = []
    title_id_dict = {}
    most_rated_shows = queries.get_most_rated(1)
    column_heads = []

    for head in most_rated_shows[0].keys():
        if head != 'id':
            column_heads.append(head)

    for row in most_rated_shows:
        data_dict = {}
        for headline in column_heads:
            if row[headline] is not None:
                data_dict[headline] = row[headline]
            else:
                data_dict[headline] = 'No URL'
        shows_to_display.append(data_dict)

    for row in most_rated_shows:
        title_id_dict[row['Title']] = row['id']
    return render_template('design.html', page_title=page_title, shows_to_display=shows_to_display,
                           column_heads=column_heads, title_id_dict=title_id_dict, selection=False, delete=False,
                           is_one_show=False, detailed_view={}, edit_data={})


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
