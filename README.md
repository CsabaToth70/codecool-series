# Codecool series

## About the project

My objective was to build up a dynamic website about movies and TV series. The task was to find and rank films by some preselected parameters, to serve background information of them, and ensure watch trailers from the page directly.
<br>

## Applied technologies

Front end: HTML, CSS, Javascript, IFrame Player API
Back end: server: Python, Flask server, postgres-based database

(For further information see the reqiurements.txt file content)
<br>

## Technical information for building up database of the project 

The runabble version can be found on the development brach of the repository.

1. After cloning the project to the local machine, the next step is the creation of an SQL database within the local repository:
sudo -u <user_name> createdb <name_of_database>
and then stepping into the psql: psql

2. Initiating connection to the created database: \connect <name_of_database>

The runningorder of the SQL files should be as below:
3. From data/db_schema/ folder 01_create_schema.sql -> psql -q <name_of_database> < 01_create_schema.sql

4. From dump_1000_shows: 
    Run all of them in the below order, with command: psql -q <name_of_database> < <name_of_sql_file>

    codecool_public_genres.sql
    codecool_public_shows.sql 
    codecool_public_actors.sql
    codecool_public_show_genres.sql
    codecool_public_seasons.sql
    codecool_public_episodes.sql(95000 lines! It can take 15-20 minutes)
    codecool_public_show_characters
<br>

## User information about main functionalities of the codecool series webpage

The list of titles displayed on the starting screen. 
We can step into the detailed page of concerned movies with click on any title or 
move to the whole database by clicking on "bd model" button at the right top corner. 
The trailers can be watched from the detailed page of the films.
After we stepped into the database, data is displayed in a table where 15 films
are displayed on one page. The user can scroll through the data by clicking
on the page numbers or arrows next to them.

The user can change the order of the films in the table by clicking these headlines:
title, year, runtime, genre. 
<br>

## Story

Codecool is famous about its great community and one of the reasons for this is
the time spent well together - for instance with watching TV shows! That's why
there is a need for a great website where all Codecoolers can find his/her
favorite series.

Your job is to create such a site. The design has been already made by the
marketing team, there is also a database that is ready (thanks to
[trakt.tv](https://trakt.tv/)), you "only" have to connect the dots and present
the data in a digestable way.

## What are you going to learn?

You will learn and practice how to do the following things:
- `PostgreSQL` queries with `SELECT`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`, `LIMIT`,
  `OFFSET` and aggregate functions;
- `Flask` routes and variable rules;
- `Jinja2` templating;
- basic `HTML` tags;
- a little bit of `JavaScript`;
- and some basic algorhitmic and formatting topics.

## Tasks

1. Create a virtual environment in your project folder and install dependencies listed in `requirements.txt`. Make a copy of `.env.template` called `.env`, fill it out with **your** details. Finally, run `data/data_inserter.py` to insert data to work with.
    - Executing the command `source venv/bin/activate` in the shell in the project's folder followed by the command `which python3` shows the project folder path (e.g. /home/user/codecool/codecool-series/venv/bin/python3)
    - Executing the command `source venv/bin/activate` in the shell in the project's folder followed by the command `pip install -r requirements.txt` shows the `Requirement already satisfied` message for every package
    - Executing the command `psql -d codecool-series -c "SELECT relname, n_live_tup FROM pg_stat_user_tables;"`
in the shell shows the following table (numbers can be higher):
```
        relname     | n_live_tup
    -----------------+------------
    show_genres     |       2550
    episodes        |      95694
    genres          |         34
    actors          |       6015
    show_characters |       8178
    shows           |       1011
    seasons         |       5350
    (7 rows)
```
    - Executing the command `source venv/bin/activate` in the shell in the project's folder followed by the command `python3 main.py` and checking the website locally through a browser on the `http://127.0.0.1:5000/` path shows a Welcome page with a bullet point list of shows

2. Create a page accessible from the path `/shows/most-rated`, where you list the 15 most rated shows in a table showing the most rated show first. Show the title (make it a link to the `/show/<id>` URL), release year, average runtime length, rating (formatted as "9.2"), genres (in alphabetical order, separated by commas) and 1-1 link to the show's trailer and homepage (or the "No URL" string if there's no URL associated).
    - Checking the website locally through a browser on the `/shows/most-rated` URL shows a page with a Codecool logo and the "Codecool Series Database" title in the top left corner, a "Register" and "Login" button in the top right corner, a main heading centered on the top and a table on a *card* with white background
    - The page title (shown on the browser tab) and the main heading (centered on the top) is "Shows"
    - The table on the page has the following column headers: Title, Year, Runtime (min), Rating, Genres, Trailer, Homepage
    - The table on the page has 15 rows and each row contains valid data according to the column headers
    - Title column contents are links to the given show's page (`/show/<id>`)
    - Rating column contents are formatted as "9.2"
    - Genres column contents are separated by comma (e.g. "Action, Adventure, Drama, War")
    - Trailer column contents are links to the given show's YouTube trailer, or if there is no trailer for that show, the "No URL" string is shown (e.g. for the show Firefly)
    - Homepage column contents are links to the given show's homepage, or if there is no homepage for that show, the "No URL" string is shown (e.g. for the show Firefly)
    - Table contents are ordered by the shows rating in descending order (first one is the most rated)

3. Create a pagination to the table on the `/shows/most-rated` route to allow the user to see the lower rated shows.
    - Checking the website locally through a browser on the `/shows/most-rated` URL shows a page where there is an extra *card* at the bottom with page numbers and arrows (e.g. "« 1 2 3 4 5 6 7 8 »")
    - The page number that corresponds with the page the user is actually looking at (i.e. the active page) is highlighted
    - The page numbers work as links, clicking them changes the table contents to another 15 rows that corresponds with the given page number (so all shows in the database can be seen through if the user visits all pages)
    - Left («) and right (») arrows work as links, clicking them shows the previous and next page, respectively (except for the first and last pages where it does nothing)
    - Clicking page numbers / arrows keeps the order of shows in the table (just shows another 15 of them)

4. [OPTIONAL] In the pagination of the `/shows/most-rated` route show only 5 page numbers: the actual page and extra 2 in each direction, except for the beginning and the end, where the actual page number won't be the middle one. Arrows should work as well (shifting the shown page numbers.)
    - Checking the website locally through a browser on the `/shows/most-rated` URL shows a page where there is an extra *card* at the bottom with 5 page numbers and arrows (e.g. "« 1 2 3 4 5 »")
    - The active page number is in the middle and the previous and next 2 are shown as well (e.g. "« 5 6 (7) 8 9 »"); for the first and last two pages the active page number is on the side (e.g. "« (1) 2 3 4 5 »", "« 64 65 66 67 (68) »")
    - Clicking left («) and right (») arrows shifts the shown page numbers to the left or right, respectively (except for the first and last 2 pages)

5. Make the table on the page accessible on `/shows/most-rated` sortable according to the columns title, year, runtime and rating by clicking on the column header (it was sorted by the rating until now). If the user clicks on the already selected column, the way of sorting should be reversed. Indicate the sorting order next to the column header with arrows (e.g. ⇩, ⇧). Make this page accessible on the path `/shows` as well.
    - Checking the website locally through a browser on the `/shows` or `/shows/most-rated` URL shows a page with a table where clicking on the title, year, runtime or rating column header sorts the table according to the column clicked
    - Sort order is indicated by an arrow (e.g. ⇩, ⇧) next to the column header according to which the table is sorted
    - Clicking the header of a column that is already sorted reverses the sorting order

6. Create a new page, accessible from the path `/show/<id>` where the user can see the details of a TV show: title, average runtime length, rating, genres (in the same way as in the shows list), overview, and the name of the top 3 actors appearing in the show). Use the provided layout that can be seen on the `/design` page (detailed view)! Include the trailer (if there's any) as a Youtube embedded video.
    - Checking the website locally through a browser on the `/show/<id>` (where id is a valid show id) shows a page with a Codecool logo and the "Codecool Series Database" title in the top left corner, a "Register" and "Login" button in the top right corner and a *card* with white background containing the details of a the given show
    - The page title (shown on the browser tab) and card title is the title of the given show
    - The detailed layout is used that can be seen on the `/design` page
    - Average runtime is shown in the following format: "1h 42min" (if it's less than an hour, then the hour part is not shown, if it's a whole hour then the minute part is not shown)
    - Rating is formatted as "9.2" (and a little star, e.g. "☆")
    - Genres list is separated by comma (e.g. "Action, Adventure, Drama, War")
    - Actors list is separated by comma (e.g. "Bryan Cranston, Anna Gunn, Aaron Paul")
    - Trailer is shown as an embedded YouTube video if exists, if not, then nothing is shown (e.g. for Firefly)

7. Create a new *card* on the show's detailed view where you list the seasons of that show in table with columns number, title and overview ordered by the number of the season.
    - Checking the website locally through a browser on the `/show/<id>` (where id is a valid show id) shows a page with an extra *card* at the bottom with a table
    - The card title is "Seasons"
    - The table on the page has the following column headers: (Empty for the number of the season), Title, Overview
    - The table on the page has rows and each row contains valid data according to the column headers

