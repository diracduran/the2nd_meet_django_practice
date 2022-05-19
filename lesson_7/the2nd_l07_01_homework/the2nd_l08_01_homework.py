# -*- coding: utf-8 -*-
# the2nd_l08_01_homework.py

"""
В папке LESSON_08 создать папку the2nd_l08_01_homework. Перейти в папку the2nd_l08_01_homework. И сохранить в ней скрипт the2nd_l08_01_homework.py и два файла .csv: dc-wikia-data.csv, marvel-wikia-data.csv

ЗАДАНИЕ.

1. В сохраненных файлах .csv содержится вся инфорация о героях DC (dc-wikia-data.csv) и MARVEL (marvel-wikia-data.csv)

2. Вам необходимо создать БД (на ваш выбор sqlite3 или postgreSQL) c названием comics.db (или comics для postgreSQL)

3. Создать с помощью кода python и используемого модуля sqlite3 (или psycopg2) внутри БД comics.db две таблицы dc_comics и marvel_comics

4. Напишите python скрипт который сохранит все данные из файлов .csv в таблицы dc_comics и marvel_comics в созданной БД comics

5. Название столбцов заголовка таблиц соответствует заголовкам в .csv файлах 
"""

import sqlite3
import csv

conn = sqlite3.connect('C:\\Users\\Dirac\\Desktop\\the2nd_meet_django_practice\lesson_7\\the2nd_l07_01_homework\\comics.db')

with open('C:\\Users\\Dirac\\Desktop\\the2nd_meet_django_practice\lesson_7\\the2nd_l07_01_homework\\dc-wikia-data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',') 
    dc_data = [] # пустой список для сохранения прочитанных данных
    for row in reader:
        dc_data.append(tuple(row)) # добавление в список
dc = dc_data[0:]

with open('C:\\Users\\Dirac\\Desktop\\the2nd_meet_django_practice\lesson_7\\the2nd_l07_01_homework\\marvel-wikia-data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',') 
    marvel_data = [] # пустой список для сохранения прочитанных данных
    for row in reader:
        marvel_data.append(tuple(row)) # добавление в список
marvel = marvel_data[0:]

with conn:
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS dc_comics (page_id INTEGER,name TEXT,urlslug TEXT,ID TEXT,ALIGN TEXT,EYE TEXT TEXT,HAIR TEXT,SEX TEXT,GSM TEXT,ALIVE TEXT,APPEARANCES INTEGER,FIRST APPEARANCE TEXT,YEAR INTEGER)""")
    cur.executemany("""INSERT INTO dc_comics VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""", dc)

    cur.execute("""CREATE TABLE IF NOT EXISTS marvel_comics (page_id INTEGER,name TEXT,urlslug TEXT,ID TEXT,ALIGN TEXT,EYE TEXT TEXT,HAIR TEXT,SEX TEXT,GSM TEXT,ALIVE TEXT,APPEARANCES INTEGER,FIRST APPEARANCE TEXT,YEAR INTEGER)""")
    cur.executemany("""INSERT INTO marvel_comics VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""", marvel)

    conn.commit()