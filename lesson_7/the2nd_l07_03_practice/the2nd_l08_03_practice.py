# -*- coding: utf-8 -*-
# the2nd_l08_03_practice.py

"""
В папке LESSON_08 создать папку the2nd_l08_03_practice. Перейти в папку the2nd_l08_03_practice. И сохранить в ней скрипт the2nd_l08_03_practice.py

ЗАДАНИЕ.

1) Ниже написан код, который позволяет получить информацию о всех фильмах Фантастической саги "Звездные Войны". 

2) Необходимо сохранить полученные данные в БД star_wars_films используя библиотеку psycopg2 (Для этого необходимо создать БД в приложении PostgreSQL):
    CREATE DATABASE star_wars_films;
    ALTER USER postgres PASSWORD 'postgres';
    \q
для создания соединения:
    conn = psycopg2.connect("host='localhost' dbname='star_wars_films' user='postgres' password='postgres'") 

3) Название таблицы: sw_films_table

4) Заголовки таблицы сохранены в переменной TABLE_HEADERS

5)  Полученные данные о героях сохранены в переменной sw_films (индексация элементов в sw_films полностью совпадает с индексами в TABLE_HEADERS)

6) Выведите на экран содержимое базы данных таблицы sw_films_table (сохраните в переменную all_films) для всего содержимого отсортированных по Эпизодам (episode_id).

7) Выведите на экран собержимое базы данных таблицы sw_films_table (сохраните в переменную george_lucas_films) для всего содержимого, где режиссером был George Lucas (director). 
"""

import psycopg2
from pip._vendor import requests

BASE_URL = "https://swapi.dev/api"
FILMS_PATH = "/films/"
TABLE_HEADERS = ['release_date', 'title', 'episode_id', 'director', 'producer']

response = requests.get(BASE_URL + FILMS_PATH)
data = response.json()['results']
sw_films = [(p['release_date'], p['title'], p['episode_id'], p['director'], p['producer']) for p in data]

print(sw_films)

db_name = "path/to/db"
connect = psycopg2.connect("host='localhost' dbname='star_wars_films' user='your_username' password='your_password'")
with connect:

    cursor = connect.cursor()

    # cursor.execute("""CREATE TABLE IF NOT EXISTS sw_films_table (release_date TEXT, title TEXT, episode_id INTEGER, director TEXT, producer TEXT);""")

    # for sw in sw_films:
    #     cursor.execute(f"INSERT INTO sw_films_table VALUES {sw};")


    

    # вот тут у меня не получается :'<

    # episodes = cursor.execute("""SELECT * FROM sw_films_table ORDER BY episode_id;""")
    # all_films = [tuple(row) for row in episodes]
    # print("СОДЕРЖИМОЕ БД (all_films)")
    # print(*all_films, sep='\n')

    # director = cursor.execute("""SELECT * FROM sw_films_table WHERE director = 'George Lucas';""")
    # george_lucas_films = [tuple(row) for row in director]
    # print("СОДЕРЖИМОЕ БД (george_lucas_films)")
    # print(*george_lucas_films, sep='\n')

    # connect.commit()