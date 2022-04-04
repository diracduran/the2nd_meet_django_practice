# -*- coding: utf-8 -*-
# the2nd_l01_01_practice.py
"""
Используя библиотеку requests и метод get получить список из 7 шуток с сайта https://icanhazdadjoke.com
Данные необходимо получить используя 1 запрос, то есть нужно изучить документацию API в разделе Search for dad jokes
Данные сохранить в список jokes и вывести все шутки на экран. 
"""
from pip._vendor import requests

URL = 'https://icanhazdadjoke.com/'

HEADERS = {'Accept': 'application/json'}

search_url = 'search'
params = {
	'limit': 7
}

res = requests.get(URL + search_url, headers=HEADERS, params=params)

json_res = res.json()

jokes = [joke['joke'] for joke in json_res['results']]

print("Задание 1:\n" + "\n".join(jokes))
"""
I'm tired of following my dreams. I'm just going to ask them where they are going and meet up with them later.
Did you hear about the guy whose whole left side was cut off? He's all right now.
Why didn’t the skeleton cross the road? Because he had no guts.
What did one nut say as he chased another nut?  I'm a cashew!
I knew I shouldn't steal a mixer from work, but it was a whisk I was willing to take.
How come the stadium got hot after the game? Because all of the fans left.
"""