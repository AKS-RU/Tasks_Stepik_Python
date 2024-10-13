# Вам потребуется код из задачи «Делаем заказ в ресторане»
#
# От менеджеров поступило требование написать функционал, который позволяет очищать заказ. Для этого нужно разработать
# функцию delete_order, которая имеет следующие параметры
#
# обязательный ключевой параметр number_table - номер стола, где будем очищать заказ
#
# необязательный ключевой параметр delete_all со значением по умолчанию False. Если передать в него True, должна
# очищаться полностью информация о заказе для указанного столика. При значении False удаление в заказе будет точечным по категориям
#
# произвольное количество ключевых параметров с булевым значением вида
# drink=True, desert=True, call=True, шаурма=True
# Среди этих значений вам нужно удалять из заказа только те, имена которых находятся в списке категорий и переданное
# значение равно True
#
#
#
# Для успешного решения задания вам необходимо определить новую функцию delete_order  и продублировать ранее созданные
# reserve_table и make_order со всеми их зависимостями.
#
# Не забывайте про кнопку «Запустить код» для проверки работоспособности программы перед отправкой.
#
# Sample Input 1:
#
# tables = {
#     1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
#     2: None,
#     3: None,
#     4: None,
#     5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
# }
#
# make_order(1, soup='Borsh')
# make_order(1, soup='Лапша', bring='Салфетку', meal='Манка')
#
# reserve_table(2, 'Vlad')
#
# make_order(2, soup='Чечевичный', salad='Цезарь', breakfast='Яичница')
# make_order(2, drink='Raf', main_dish='Утка по-пекински')
# make_order(2, desert='Трюфель', call='такси')
# print(tables)
#
# delete_order(number_table=2, delete_all=True)
# print(tables)
# Sample Output 1:
#
# {1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Лапша'}},
#  2: {'name': 'Vlad', 'is_vip': False, 'order': {'soup': 'Чечевичный', 'salad': 'Цезарь', 'drink': 'Raf',
#                                                 'main_dish': 'Утка по-пекински', 'desert': 'Трюфель'}},
#  3: None, 4: None, 5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}}
# {1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Лапша'}}, 2: {'name': 'Vlad', 'is_vip': False, 'order': {}},
#  3: None, 4: None, 5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}}
# Sample Input 2:
#
# tables = {
#     1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Borsh'}},
#     2: None,
#     3: None,
#     4: None,
#     5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
# }
#
# try:
#     delete_order(1, delete_all=True)
# except TypeError:
#     print('Вызов delete_order без передачи значения по ключу не должен проходить')
# else:
#     raise ValueError('Проверьте типы параметров функции delete_order')
# Sample Output 2:
#
# Вызов delete_order без передачи значения по ключу не должен проходить
# Sample Input 3:
#
# tables = {
#     1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Borsh'}},
#     2: None,
#     3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
# }
#
# make_order(1, soup='Borsh')
# make_order(1, soup='Лапша', bring='Салфетку', meal='Манка')
#
# reserve_table(2, 'Vlad')
#
# make_order(2, soup='Чечевичный', salad='Цезарь', breakfast='Яичница')
# make_order(2, drink='Raf', main_dish='Утка по-пекински')
# make_order(2, desert='Трюфель', call='такси')
# print(tables)
#
# delete_order(number_table=2, salad=True, main_dish=True, soup=False, desert=True)
# print(tables)
# Sample Output 3:
#
# {1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Лапша'}},
#  2: {'name': 'Vlad', 'is_vip': False, 'order': {'soup': 'Чечевичный', 'salad': 'Цезарь', 'drink': 'Raf',
#                                                 'main_dish': 'Утка по-пекински', 'desert': 'Трюфель'}},
#  3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}}
# {1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Лапша'}},
#  2: {'name': 'Vlad', 'is_vip': False, 'order': {'soup': 'Чечевичный', 'drink': 'Raf'}},
#  3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}}
# Sample Input 4:
#
# tables = {
#     1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Borsh'}},
#     2: None,
#     3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
# }
#
# make_order(1, soup='Borsh')
# make_order(1, soup='Лапша', bring='Салфетку', meal='Манка')
#
# reserve_table(2, 'Vlad')
#
# make_order(2, soup='Чечевичный', salad='Цезарь', breakfast='Яичница')
# make_order(2, drink='Raf', main_dish='Утка по-пекински')
# make_order(2, desert='Трюфель', call='такси')
# print(tables)
#
# delete_order(number_table=2, drink=True, desert=True, call=True, шаурма=True, cheesecake=True)
# delete_order(number_table=1, soup=True, desert=True, call=True)
# print(tables)
# Sample Output 4:
#
# {1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Лапша'}},
#  2: {'name': 'Vlad', 'is_vip': False, 'order': {'soup': 'Чечевичный', 'salad': 'Цезарь', 'drink': 'Raf',
#                                                 'main_dish': 'Утка по-пекински', 'desert': 'Трюфель'}},
#  3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}}
# {1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
#  2: {'name': 'Vlad', 'is_vip': False, 'order': {'soup': 'Чечевичный', 'salad': 'Цезарь', 'main_dish':
#      'Утка по-пекински'}}, 3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}}


tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}


menu = ('salad', 'soup', 'main_dish', 'drink', 'desert')


def is_table_free(n: int):
    return not bool(tables.get(n))


def reserve_table(n: int, name: str, bool=False):
    if is_table_free(n):
        tables[n] = {'name': name, 'is_vip': bool, 'order': {}}


def delete_reservation(n: int):
    tables[n] = None


def make_order(n, **kwargs):
    if not is_table_free(n):
        for key, val in kwargs.items():
            if key in menu:
                tables[n]['order'][key] = val

def delete_order(*,number_table, delete_all=False, **kwargs):
    if delete_all:
        tables[number_table]['order'] = {}
    else:
        for key, val in kwargs.items():
            if key in menu and val and key in tables[number_table]['order']:
                tables[number_table]['order'].pop(key)








tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Borsh'}},
    2: None,
    3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}

make_order(1, soup='Borsh')
make_order(1, soup='Лапша', bring='Салфетку', meal='Манка')

reserve_table(2, 'Vlad')

make_order(2, soup='Чечевичный', salad='Цезарь', breakfast='Яичница')
make_order(2, drink='Raf', main_dish='Утка по-пекински')
make_order(2, desert='Трюфель', call='такси')
print(tables)

delete_order(number_table=2, drink=True, desert=True, call=True, шаурма=True, cheesecake=True)
delete_order(number_table=1, soup=True, desert=True, call=True)
print(tables)