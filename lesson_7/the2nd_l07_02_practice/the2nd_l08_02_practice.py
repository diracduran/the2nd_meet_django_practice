# -*- coding: utf-8 -*-
# the2nd_l08_02_practice.py

"""
В папке LESSON_08 создать папку the2nd_l08_02_practice. Перейти в папку the2nd_l08_02_practice. И сохранить в ней скрипт the2nd_l08_02_practice.py

ЗАДАНИЕ.

1) Ниже написан код, который позволяет получить информацию о 10 героях Фантастической саги "Звездные Войны". 

2) Необходимо сохранить полученные данные в БД star_wars.db используя библиотеку sqlite3

3) Название таблицы: star_wars_people

4) Заголовки таблицы сохранены в переменной TABLE_HEADERS

5)  Полученные данные о героях сохранены в переменной sw_people (индексация элементов в sw_people полностью совпадает с индексами в TABLE_HEADERS)

6) Выведите на экран собержимое базы данных (сохраните в переменную short_info) для всего содержимого по столбцам name, height, mass, birth_year, homeworld.

7) Выведите на экран собержимое базы данных для героев, чей рост <= 100 (сохраните в переменную height_less_100). Для вывода используйте столбцы: name, height, mass, birth_year. 
"""
import sqlite3
from pip._vendor import requests

BASE_URL = "https://swapi.dev/api"
PEOPLE_PATH = "/people/"
TABLE_HEADERS = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'url']

response = requests.get(BASE_URL + PEOPLE_PATH)
data = response.json()['results']



sw_people = [(p['name'], p['height'], p['mass'], p['hair_color'], p['skin_color'], p['eye_color'], p['birth_year'], p['gender'], p['homeworld'], p['url']) for p in data]

print(sw_people)

db_name = "path/to/star_wars.db"
connect = sqlite3.connect(db_name)
with connect:
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS star_wars_people (name TEXT, height INTEGER, mass INTEGER, hair_color TEXT, skin_color TEXT, eye_color TEXT, birth_year TEXT, gender TEXT, homeworld TEXT, url TEXT)""")

    cursor.executemany("""INSERT INTO star_wars_people VALUES (?,?,?,?,?,?,?,?,?,?)""", sw_people)

       
    short_info = [tuple(row) for row in cursor.execute("""SELECT height, mass, birth_year, homeworld FROM star_wars_people""")]
    print("СОДЕРЖИМОЕ БД (short_info)")
    print(*short_info, sep='\n')
    """
    СОДЕРЖИМОЕ БД (short_info)
    (172, 77, '19BBY', 'https://swapi.dev/api/planets/1/')
    (167, 75, '112BBY', 'https://swapi.dev/api/planets/1/')
    (96, 32, '33BBY', 'https://swapi.dev/api/planets/8/')
    (202, 136, '41.9BBY', 'https://swapi.dev/api/planets/1/')
    (150, 49, '19BBY', 'https://swapi.dev/api/planets/2/')
    (178, 120, '52BBY', 'https://swapi.dev/api/planets/1/')
    (165, 75, '47BBY', 'https://swapi.dev/api/planets/1/')
    (97, 32, 'unknown', 'https://swapi.dev/api/planets/1/')
    (183, 84, '24BBY', 'https://swapi.dev/api/planets/1/')
    (182, 77, '57BBY', 'https://swapi.dev/api/planets/20/')
    """

    height_less_100 = [tuple(row) for row in cursor.execute("""SELECT name, height, mass, birth_year FROM star_wars_people WHERE height <= 100""")]
    print("СОДЕРЖИМОЕ БД (height_less_100)")
    print(*height_less_100, sep='\n')
    """
    СОДЕРЖИМОЕ БД (height_less_100)
    ('R2-D2', 96, 32, '33BBY')
    ('R5-D4', 97, 32, 'unknown')
    """

    connect.commit()