# Напишите функция create_info, которая имеет следующие параметры
#
#     —  employees содержит имена работников в виде списка  (можете переименовать параметр по своему усмотрению)
#
#     —  identifiers содержит уникальные идентификаторы работников  (можете переименовать параметр по своему усмотрению)
#
# Функция create_info на основании параметров employees и identifiers должна создать словарь, ключами которого являются
# идентификаторы, а значениями - имена сотрудников. Соединение идентификатора и имени сотрудника должно выполняться
# по следующей логике:
#
# Выбирается самый маленький идентификатор из списка identifiers
# Выбирается первое имя по алфавиту из списка employees
# Создается пара ключ-значение.
# Процесс повторяется со следующими значениями. Берется второй по старшинству идентификатор и второе имя по алфавиту,
# создается пара в словаре и вновь повторяем процесс
# Итоговый словарь функция create_info должна вернуть в качестве результата.
#
# Sample Input 1:
#
# names = [
#     'Pankratiy', 'Lidochka', 'Svetka', 'Maks', 'Yura', 'Sergei'
# ]
#
# ids = [77, 4, 20, 37, 32, 96]
# print(create_info(names, ids))
# Sample Output 1:
#
# {4: 'Lidochka', 20: 'Maks', 32: 'Pankratiy', 37: 'Sergei', 77: 'Svetka', 96: 'Yura'}
# Sample Input 2:
#
# names = [
#     'Pankratiy', 'Lidochka', 'Innokentiy', 'Anfisa', 'Yaroslava',
#     'Svetka', 'Maks', 'Yura', 'Sergei'
# ]
#
# ids = [77, 4, 20, 5, 56, 17, 20, 32, 96]
# print(create_info(names, ids))
# Sample Output 2:
#
# {4: 'Anfisa', 5: 'Innokentiy', 17: 'Lidochka', 20: 'Pankratiy', 32: 'Sergei', 56: 'Svetka', 77: 'Yaroslava',
# 96: 'Yura'}


def create_info(name: list[str], id_n: list[int]) -> dict[int:str]:
    return dict(zip(sorted(id_n), sorted(name)))


names = [
    'Pankratiy', 'Lidochka', 'Svetka', 'Maks', 'Yura', 'Sergei'
]

ids = [77, 4, 20, 37, 32, 96]
print(create_info(names, ids))