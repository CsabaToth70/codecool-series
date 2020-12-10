from flask import Flask, render_template, url_for, request, jsonify
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask('codecool_series')

@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/input-age')
def input_age():
    return render_template('age.html')


@app.route('/age')
def age():
    start_date = request.args.get('start-date')
    end_date = request.args.get('end-date')
    actor_data_dicts = queries.get_age(start_date, end_date)
    return jsonify(actor_data_dicts)


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
