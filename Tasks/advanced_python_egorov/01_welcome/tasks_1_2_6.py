# Считаем статистику
# Файл data_workers.json содержит строку в формате JSON, в которой вы можете получить
# персональные данные о 10 000 человек.
#
# Каждый человек представлен объектом (словарем) с пятью ключами:
#
# {
#     "forename": "Camilla",
#     "surname": "Björk",
#     "female": True,
#     "age": 39,
#     "occupation": "firefighter"
# }
# Создайте программу, которая может вычислять статистику по возрасту и полу для различных
# профессий на основе файла data_workers.json.
#
#
#
# В редакторе кода на степике вы можете обращаться к файлу data_workers.json, он будет находиться
# в той же папке, где и запускается сам модуль
#
#
#
#
#
# Программа должна принимать на вход название профессии и выводить статическую информацию по ней
# в следующем виде:
#
# ---------------------
# | 20-29  | {количество между 20 и 29 годами}
# | 30-39  | {количество между 30 и 39 годами}
# | 40-49  | {количество между 40 и 49 годами}
# | 50-59  | {количество между 50 и 59 годами}
# | 60-69  | {количество между 60 и 69 годами}
# ---------------------
# | FEMALE | {общее количество женщин данной профессии}
# | MALE   | {общее количество мужчин данной профессии}
# ---------------------


import json

with open('data_workers.json') as fp:
    file = json.load(fp)

occupation_in = input()


def get_statistics(start: int, end: int, occupation: str) -> int:
    count = 0
    for i in file:
        if start <= i['age'] <= end and i['occupation'] == occupation:
            count += 1
    return count


def get_gender(gender: bool, occupation: str) -> int:
    count = 0
    for i in file:
        if i["female"] == gender and i['occupation'] == occupation:
            count += 1
    return count


print('-' * 21)
print(f'| 20-29  | {get_statistics(20, 29, occupation_in)}')
print(f'| 30-39  | {get_statistics(30, 39, occupation_in)}')
print(f'| 40-49  | {get_statistics(40, 49, occupation_in)}')
print(f'| 50-59  | {get_statistics(50, 59, occupation_in)}')
print(f'| 60-69  | {get_statistics(60, 69, occupation_in)}')
print('-' * 21)
print(f'| FEMALE | {get_gender(True, occupation_in)}')
print(f'| MALE   | {get_gender(False, occupation_in)}')
print('-' * 21)
