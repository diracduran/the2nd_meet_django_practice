# the2nd_l09_04_practice.py
"""
Создать папку LESSON_09. Перейти в папку LESSON_09 и создать в ней папку the2nd_l09_04_practice. Перейти в папку the2nd_l09_04_practice. Скопировать в нее файл the2nd_l09_04_practice.py.

ПАРСИНГ ДАТЫ
Напишите функцию parse_date, которая принимает в качестве аргумента строку. Функция должна проверить, соответствует ли строка формату даты.
Допустимы форматы даты: "dd/mm/yyyy"; "dd.mm.yyyy"; "dd,mm,yyyy".
Однако, вместо того, чтобы просто возвращать True или False, если строка совпадает, Вы должны вернуть словарь, содержащий три части даты с ключами "d", "m", "y":
    parse_date("11/12/2016") --> {"d" : "11", "m" : "12", "y" : "2016"}
    
Строка должна иметь ПОЛНОЕ совпадение, то есть ничего кроме даты быть не должно. Если совпадений нет, то return None
    
Пример:
    parse_date("07/06/1967") --> {"d" : "07", "m" : "06", "y" : "1967"}
    parse_date("01.09.2018") --> {"d" : "01", "m" : "09", "y" : "2018"}
    parse_date("27,03,2001") --> {"d" : "27", "m" : "03", "y" : "2001"}
    parse_date("01/01/1900 start date") --> None
    parse_date("22-11-2012") --> None
"""
import re

# ВАШ КОД НИЖЕ
def parse_date(check_date):
    # pattern = re.compile(r'[01]?[0-9]|[20-29]|[30-31]/|.|,[1-12]/|.|,[0-9]{4}')
    match = re.findall(r'^([0]?[1-9]|[1|2][0-9]|[3][0|1])[./,]([0]?[1-9]|[1][0-2])[./,]([0-9]{4}|[0-9]{2})$', check_date)
    
            if m == None: return None
            return {"d" : m[0], "m" : m[1], "y" : m[2]}
            

check_list = [
        "07/06/1967",
        "01.09.2018",
        "27,03,2001",
        "01/01/1900 start date",
        "22-11-2012"
        ]

for check in check_list: print(parse_date(check))
"""
{'d': '07', 'm': '06', 'y': '1967'}
{'d': '01', 'm': '09', 'y': '2018'}
{'d': '27', 'm': '03', 'y': '2001'}
None
None
"""