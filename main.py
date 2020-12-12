from flask import Flask, render_template, url_for, request, jsonify
from data import queries
import math
from dotenv import load_dotenv
from datetime import date

load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/input-year')
def get_year():
    return render_template('year.html')


@app.route('/year')
def get_actor_data():
    year = request.args.get('year-input')
    actor_data = queries.get_actor_data(year)
    actor_data = get_completed_data(actor_data)
    return jsonify(actor_data)


def get_completed_data(actor_data):
    current_date = date.today()
    for i, row in enumerate(actor_data):
        actor_data[i]['is_older_actor'] = False
        if actor_data[i]['actor_age'] is None:
            actor_data[i]['age_of_show'] = get_age_from_dates(current_date, row['released_year'])
            actor_data[i]['age_actor_at_release'] = None
        else:
            age_of_show = get_age_from_dates(current_date, row['released_year'])
            birthday = get_birth_year_by(row['actor_age'])
            age_actor_at_release = get_age_from_dates(row['released_year'], birthday)
            if int(age_actor_at_release) > int(age_of_show):
                row['is_older_actor'] = True
            actor_data[i]['age_of_show'] = age_of_show
            actor_data[i]['age_actor_at_release'] = age_actor_at_release
    return actor_data


def get_age_from_dates(later_date, earlier_date):
    earlier_date = int(str(earlier_date)[:4])
    later_date = int(str(later_date)[:4])
    return later_date - earlier_date


def get_birth_year_by(age):
    current_year = int(str(date.today())[:4])
    year_int = current_year - int(age)
    year_string = str(year_int) + "-01-01"
    return year_string


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
