from flask import Flask, render_template, url_for, request, redirect
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


@app.route('/shows/most-rated/')
def display_most_rated():
    page_number = int(request.args.get('page', 1))
    page_title = 'Most rated shows'
    shows_to_display = []
    title_id_dict = {}
    length_of_list = 8
    starting_row_number = get_starting_row_number(page_number)
    most_rated_shows = queries.get_most_rated(starting_row_number)
    page_number_list, all_page_number = get_page_number_list(page_number, length_of_list)

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
                           is_one_show=False, detailed_view={}, edit_data={}, page_number_list=page_number_list,
                           page_number=page_number, all_page_number=all_page_number)


def get_starting_row_number(page_number):
    return (page_number * 15) - 14


def get_page_number_list(page_number, length_of_list: int):
    rows_number = 15
    pagination_list = []
    page_number_list = [[i + 1, 0] for i in range(length_of_list)]
    all_row_number = get_all_row_number()
    all_page_number = get_all_page_number(all_row_number, rows_number)
    if page_number > all_page_number - length_of_list:
        for i in range((all_page_number - length_of_list) + 1, all_page_number + 1):
            pagination_list.append(i)
    elif page_number <= length_of_list:
        for i in range(length_of_list):
            pagination_list.append(i + 1)
    else:
        if length_of_list % 2 == 0:
            for i in range(page_number - int((length_of_list / 2)), 1 + page_number + int(((length_of_list / 2) - 1))):
                pagination_list.append(i)
        else:
            for i in range(page_number - int((length_of_list / 2)), 1 + page_number + int((length_of_list / 2))):
                pagination_list.append(i)
    for n, p in enumerate(pagination_list):
        page_number_list[n][1] = p
    return page_number_list, all_page_number


def get_all_row_number():
    all_row_number = queries.get_number_of_all()
    all_row_number = all_row_number[0]['count']
    return int(all_row_number)


def get_all_page_number(all_row_number, rows_number):
    all_page_number = (all_row_number / rows_number) + (all_row_number % rows_number > 0)
    return int(all_page_number)


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
