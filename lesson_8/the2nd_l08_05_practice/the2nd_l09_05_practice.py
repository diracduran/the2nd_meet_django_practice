# the2nd_l09_05_practice.py
"""
Создать папку LESSON_09. Перейти в папку LESSON_09 и создать в ней папку the2nd_l09_05_practice. Перейти в папку the2nd_l09_05_practice. Скопировать в нее файл the2nd_l09_05_practice.py.

ЛЮДИ В ЧЕРНОМ
Напишите функцию top_secret, которая принимает в качестве аргумента строку. Функция должна заменять в строке "Люди в черном" на "СЕКРЕТ" и возвращать измененную стоку. При этом "люди в черном" могут изменять склонение и регистр букв:
Пример:
    top_secret("Люди в черном очень скрытные.") --> "СЕКРЕТ очень скрытные"
    top_secret("Всегда на помощь приходят люди в черном!") --> "Всегда на помощь приходят СЕКРЕТ!"
    top_secret("Людей в черном могут узнать только люди в черном.") --> "СЕКРЕТ могут узнать только СЕКРЕТ."
    
"""

import re

# ВАШ КОД НИЖЕ
def top_secret(check_mib):
    res = re.findall(r'[л|Л]юд\w{0,} в черном', check_mib)
    replaced_mib = check_mib.replace(res[0], 'СЕКРЕТ')
    return replaced_mib
    return

check_list = [
        "Люди в черном очень скрытные.",
        "Всегда на помощь приходят люди в черном!",
        "Людей в черном могут узнать только люди в черном."
        ]

for check in check_list: print(top_secret(check))
"""
СЕКРЕТ очень скрытные.
Всегда на помощь приходят СЕКРЕТ!
СЕКРЕТ могут узнать только люди в черном. :<
"""