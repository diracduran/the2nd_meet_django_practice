# the2nd_l09_01_homework.py
"""
Создать папку LESSON_09. Перейти в папку LESSON_09 и создать в ней папку the2nd_l09_01_homework. Перейти в папку the2nd_l09_01_homework. Скопировать в нее файл the2nd_l09_01_homework.py.

-=*** GIVE ME AN IMAGE FROM NATIONAL GEOGRAPHY ***=-

Напишите функцию get_img_url, которая будет находить ссылки на все изображения сохраненные в переменной data (данные хранятся в виде строки).
Данные в переменной data - это результат запроса GET на сайт https://www.instagram.com/natgeo/

Ссылки на изображения, к которым необходимо написать регулярное выражение представлены в формате:

"src":"https://scontent-arn2-1.cdninstagram.com/vp/d1bd5ef62357946d3e602e318a2ba0c1/5D3D3A74/t51.2885-15/sh0.08/e35/c0.135.1080.1080/s640x640/56347818_439423140135260_222436944865078914_n.jpg?_nc_ht=scontent-arn2-1.cdninstagram.com","config_width":640

"src":"https://scontent-arn2-1.cdninstagram.com/vp/822a0ba89496db753a0cd1ec55d5a556/5D3F5191/t51.2885-15/sh0.08/e35/c0.75.1080.1080/s640x640/54513868_2499920290078880_6085694610039206455_n.jpg?_nc_ht=scontent-arn2-1.cdninstagram.com","config_width":640

"src":"https://scontent-arn2-1.cdninstagram.com/vp/bf0671c779e473fe8312c62674bef6e4/5D3E631A/t51.2885-15/e15/c180.0.720.720/s640x640/54463866_560472434444154_2512477850949351202_n.jpg?_nc_ht=scontent-arn2-1.cdninstagram.com","config_width":640

ОБЯЗАТЕЛЬНО ПРИ ПОИСКЕ УЧЕСТЬ ,"config_width":640 - ТАК КАК ЭТО ВЛИЯЕТ НА РАЗМЕР СОХРАНЯЕМОГО ИЗОБРАЖЕНИЯ

Данные необходимо вернуть в виде списка:

["https://scontent-arn2-1.cdninstagram.com/vp/d1bd5ef62357946d3e602e318a2ba0c1/5D3D3A74/t51.2885-15/sh0.08/e35/c0.135.1080.1080/s640x640/56347818_439423140135260_222436944865078914_n.jpg?_nc_ht=scontent-arn2-1.cdninstagram.com", ..., ..., ..., "https://scontent-arn2-1.cdninstagram.com/vp/bf0671c779e473fe8312c62674bef6e4/5D3E631A/t51.2885-15/e15/c180.0.720.720/s640x640/54463866_560472434444154_2512477850949351202_n.jpg?_nc_ht=scontent-arn2-1.cdninstagram.com"]

"""
import random
from pip._vendor import requests
import re
BASE_URL = "https://www.instagram.com/natgeo/"
response = requests.get(BASE_URL)
data = response.text
img_prefix = "nat_geo_"

def save_10_img(image_url):
    if image_url:
        for i in range(10):
            try:
                filename = img_prefix + str(i) + ".jpg"
                img_url = random.choice(image_url)
                image_url.remove(img_url)
                img_resp = requests.get(img_url)
                with open(filename, 'wb') as f:
                    f.write(img_resp.content)
            except Exception as err:
                print(err)
            else:
                print(filename + " is done")
    else:
        print("Your images url list is empty")


# ВАШ КОД НИЖЕ
def get_img_url(http_page):
    match = re.findall(r'\"src\":\"https\:\/+[a-z]+\-[a-z0-9]+\-\d\.[a-z]+\.[a-zA-Z0-9]+/\w{2}/[a-z0-9]+/[0-9A-Z]+/t\d{2}\.\d{4}-\d{2}/([a-z]+(\d{2}|[0-9]\.\d{2})/[a-z]+(\d{2}|\d{3}\.\d\.\d{3}\.\d{3})/[a-z]\d\.(\d{3}|\d{2})\.\d{4}\.\d{4}/\w640x640/\d{8,}_\d{15,}_\d{18,}_\w\.\w{3}\?_\w{2}_\w{2}\=[a-z]+\-[a-z0-9]+\-\d\.[a-z]+\.[a-zA-Z0-9]+\"\,\"config_width\"\:640|\w\d{2}/\w\d{3}.\d.\d{3}.\d{3}/s\d{3}x\d{3}/\d{8,}_\d{15,}_\d{18,}_\w\.\w{3}\?_\w{2}_\w{2}\=[a-z]+\-[a-z0-9]+\-\d\.[a-z]+\.[a-zA-Z0-9]+\"\,\"config_width\"\:640)', http_page)
    links = []
    if match:
        for m in match:
            links_match = re.findall(r'\"https\:\/+[a-z]+\-[a-z0-9]+\-\d\.[a-z]+\.[a-zA-Z0-9]+/\w{2}/[a-z0-9]+/[0-9A-Z]+/t\d{2}\.\d{4}-\d{2}/([a-z]+(\d{2}|[0-9]\.\d{2})/[a-z]+(\d{2}|\d{3}\.\d\.\d{3}\.\d{3})/[a-z]\d\.(\d{3}|\d{2})\.\d{4}\.\d{4}/\w640x640/\d{8,}_\d{15,}_\d{18,}_\w\.\w{3}\?_\w{2}_\w{2}\=[a-z]+\-[a-z0-9]+\-\d\.[a-z]+\.[a-zA-Z0-9]+\"|\w\d{2}/\w\d{3}.\d.\d{3}.\d{3}/s\d{3}x\d{3}/\d{8,}_\d{15,}_\d{18,}_\w\.\w{3}\?_\w{2}_\w{2}\=[a-z]+\-[a-z0-9]+\-\d\.[a-z]+\.[a-zA-Z0-9]+\")', m)
            links.append(links_match)
    return links



nat_geo_img = get_img_url(data)
print(nat_geo_img) # возвращает [] :<
save_10_img(nat_geo_img) # возвращает 'Your images url list is empty' :<