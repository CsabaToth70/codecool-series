from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

from data import queries

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
    ordered_by = request.args.get('aspect', "Rating")
    requested_ordered_by = ordered_by
    ordered_by = "Runtime (min)" if ordered_by == "Runtime" else ordered_by
    adjusted_ordered_by = ordered_by
    direction_string = request.args.get('direction')
    direction = False if direction_string == "false" else True
    page_title = 'Most rated shows'
    shows_to_display = []
    title_id_dict = {}
    length_of_page_list = 5
    starting_row_number = get_starting_row_number(page_number)
    most_rated_shows = queries.get_ordered_shows(str(starting_row_number), ordered_by, direction)
    page_number_list, all_page_number = get_page_number_list(page_number, length_of_page_list)

    column_heads = []
    query_heads = []
    for head in most_rated_shows[0].keys():
        if head != 'id':
            query_heads.append(head)
            if head == adjusted_ordered_by:
                if direction:
                    adjusted_head = head + " ⇧"
                    column_heads.append(adjusted_head)
                else:
                    adjusted_head = head + " ⇩"
                    column_heads.append(adjusted_head)
            else:
                column_heads.append(head)

    for row in most_rated_shows:
        data_dict = {}
        for headline in query_heads:
            if row[headline] is not None:
                data_dict[headline] = row[headline]
            else:
                data_dict[headline] = 'No URL'
        shows_to_display.append(data_dict)

    for row in most_rated_shows:
        title_id_dict[row['Title']] = row['id']

    return render_template('design.html', selection=False, delete=False, is_one_show=False, page_title=page_title,
                           shows_to_display=shows_to_display, column_heads=column_heads, title_id_dict=title_id_dict,
                           detailed_view={}, edit_data={}, page_number_list=page_number_list, page_number=page_number,
                           all_page_number=all_page_number, aspect=requested_ordered_by, direction=direction_string)


@app.route('/show/')
def get_detailed_show():
    show_id = request.args.get('show-id')
    detailed_show = queries.get_one_show_data(show_id)
    detail_dict = {}
    detailTypes = []
    for whatDetail in detailed_show[0].keys():
        detailTypes.append(whatDetail)
    for detail in detailTypes:
        if detail == 'Runtime':
            minutes = int(detailed_show[0][detail])
            hours = str(int(minutes / 60)) + 'h ' if minutes >= 60 else ''
            rest_minutes = str(int(minutes % 60)) + 'min' if (minutes % 60) > 0 else ''
            detail_dict[detail] = hours + rest_minutes
        elif detail == 'Year':
            detail_dict[detail] = str(detailed_show[0][detail])[:4]
        else:
            detail_dict[detail] = detailed_show[0][detail]
    season_headers = ["Season", "Title", "Overview"]
    season_data = queries.get_season_data(show_id)
    return render_template('design.html', is_one_show=True, detailed_view=True, detailDict=detail_dict,
                           season_headers=season_headers, season_data=season_data)


@app.route('/search')
def get_searching_page():
    return render_template('search.html')


@app.route('/search-input', methods=['GET'])
def get_searching_result():
    searching_text = request.args.get('input-text')
    word_list = searching_text.split(' ')
    result_list = []
    for word in word_list:
        findings = queries.get_result('%' + word + '%')
        for i, row in enumerate(findings):
            result_list.append(findings[i])
    return jsonify(result_list)


def get_starting_row_number(page_number):
    return (page_number * 15) - 14


def get_page_number_list(page_number, length_of_page_list: int):
    rows_number = 15
    pagination_list = []
    page_number_list = [[i + 1, 0] for i in range(length_of_page_list)]
    all_row_number = get_all_row_number()
    all_page_number = get_all_page_number(all_row_number, rows_number)
    if page_number > all_page_number - length_of_page_list:
        for i in range((all_page_number - length_of_page_list) + 1, all_page_number + 1):
            pagination_list.append(i)
    elif page_number <= length_of_page_list:
        for i in range(length_of_page_list):
            pagination_list.append(i + 1)
    else:
        if length_of_page_list % 2 == 0:
            for i in range(page_number - int((length_of_page_list / 2)),
                           1 + page_number + int(((length_of_page_list / 2) - 1))):
                pagination_list.append(i)
        else:
            for i in range(page_number - int((length_of_page_list / 2)),
                           1 + page_number + int((length_of_page_list / 2))):
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
