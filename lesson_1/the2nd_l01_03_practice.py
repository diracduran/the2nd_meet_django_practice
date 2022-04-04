# -*- coding: utf-8 -*-
# the2nd_l01_03_practice.py
"""
Используя библиотеку requests и метод get необходимо программу для получения изображений, используя pixabay API

1) Программа должна запросить у пользователя категорию изображения - <category> (обязательно учесть отказ от использования категории для получения случайной категории изображения)
2) Далее программа должна запросить у пользователя условие поиска - <q> (также учесть отказ от поиска - случайное изображение)
3) Сам запрос реализовать в виде функции с двумя обязательными аргументами category и q - get_image(category, q)
4) Программа должна работать до тех пор пока пользователь не захочет ее прервать (использовать цикл while) и логику также реализовать в виде функции - collect_images()
P.S. if __name__ == '__main__' - информацию можно узнать перейдя по ссылке:

https://zen.yandex.ru/media/id/5bbcd4ab48032300ab7460a6/chto-delaet-if-name--main-v-python-5eb5731aa19aea5aa92fdcf5
"""
import random
from tkinter.messagebox import QUESTION
from pip._vendor import requests


KEY = '26315914-cd93893e23695d073e1b908cf' # получите ключ после регистрации
BASE_URL = 'https://pixabay.com/api/'

CATEGORIES = ['fashion', 'nature', 'backgrounds', 'science', 'education', 'people', 'feelings', 'religion', 'health', 'places', 'animals', 'industry', 'food', 'computer', 'sports', 'transportation', 'travel', 'buildings', 'music']

def get_image(category, q):
    params = {
        "orientation": "horizontal",
        "image_type": "photo",
        "min_width": 1920,
        "min_height": 1080,
        "category": category,
        "q": q
    }
    res = requests.get(BASE_URL, params=params)
    data = res.json()
    # if (params['category'] in CATEGORIES and params['q'] == '') or (params['category'] == '' and params['q'] != ''): # ?????
    response = [d['largeImageURL'] for d in data['hits'] if params['category'] in CATEGORIES and params['q'] == q]
    return response

def collect_images():

    category = input("Choose category: 'fashion', 'nature', 'backgrounds', 'science', 'education', 'people', 'feelings', 'religion', 'health', 'places', 'animals', 'industry', 'food', 'computer', 'sports', 'transportation', 'travel', 'buildings', 'music'. Or enter \"random\". ")
    query = input('Any query? ')
        # flag = False

    while True:
        if query != '':
            if category in CATEGORIES:
                get_image(category, q=query)
            elif category == 'random':
                get_image(category=CATEGORIES[random.randint(1, len(CATEGORIES))], q=query)
        else: print('Query in necessary')
        break


if __name__ == '__main__':
    collect_images()
