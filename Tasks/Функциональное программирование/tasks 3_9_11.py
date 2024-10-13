# Делаем заказ в ресторане - часть 2
# Вам потребуется код из следующих задач
#
#     ✔  «Делаем заказ в ресторане»
#
#     ✔  «Удаляем заказ»
#
# Проблема предыдущей версии функции make_order заключается в том, что она перезатирала ранее заказанные блюда.
# И она также не давала в рамках одного вызова заказать несколько блюд из одной категории.
#
# Ваша задача переписать функцию  make_order так, чтобы она сохраняла блюда из одной категории в виде списка,
# а в случае нового заказа с блюдами из той же категории, эти блюда добавлялись бы в тот же список..
#
# Давайте разберем примеры, имеется такая структура данных
#
# tables = {
#     1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
#     2: None,
#     3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
# }
# Далее Андрей делает два заказа make_order
#
# make_order(1, soup='Borsh')
# make_order(1, soup='Лапша')
# Оба заказанных блюда из категории суп, значит в итоге нужно сложить их в один список и получить следующее
#
# {
#  1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': ['Borsh', 'Лапша']}},
#  2: None,
#  3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}
# }
# Также новая реализация функции make_order   должна позволять передать несколько блюд через запятую в рамках
# одной категории
#
# make_order(1, soup='Borsh,Лапша', desert='Медовик', drink='Cola')
# make_order(1, soup='Гаспачо', desert='Печенье,Наполеон')
#
#
#
#
# Для успешного решения задания вам необходимо переписать функцию make_order и продублировать ранее созданные
# reserve_table и delete_order со всеми их зависимостями.
#
# Не забывайте про кнопку «Запустить код» для проверки работоспособности программы перед отправкой.
#
# Sample Input 1:
#
# tables = {
#     1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
#     2: None,
#     3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
# }
# make_order(1, soup='Borsh')
# make_order(1, soup='Лапша')
# print(tables)
# Sample Output 1:
#
# {1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': ['Borsh', 'Лапша']}}, 2: None,
#  3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}}
#
# Sample Input 2:
#
# tables = {
#     1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
#     2: None,
#     3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
# }
# make_order(1, soup='Borsh,Лапша', desert='Медовик', drink='Cola')
# make_order(1, soup='Гаспачо', desert='Печенье,Наполеон')
# print(tables)
# Sample Output 2:
#
# {1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': ['Borsh', 'Лапша', 'Гаспачо'],
#                                                  'desert': ['Медовик', 'Печенье', 'Наполеон'],
#                                                  'drink': ['Cola']}}, 2: None,
#  3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}}
# Sample Input 3:
#
# tables = {
#     1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
#     2: None,
#     3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
# }
#
# make_order(1, soup='Borsh,Лапша', desert='Медовик', drink='Cola')
# make_order(1, soup='Гаспачо', desert='Печенье,Наполеон')
#
# reserve_table(2, 'Vlad')
#
# make_order(2, soup='Чечевичный', salad='Цезарь,Мимоза', breakfast='Яичница,Бекон')
# make_order(2, drink='Raf,Coffee,Juice', main_dish='Утка по-пекински,Отбивная')
# make_order(2, desert='Трюфель', call='такси')
#
# make_order(1, desert='Наполеон', drink='Чай', meal='Манка,Овсянка')
# make_order(1, desert='Вишня', drink='Кофе')
# print(tables)
# delete_order(number_table=2, drink=True, desert=True, call=True, шаурма=True, cheesecake=True)
# delete_order(number_table=1, soup=True, desert=True, call=True)
# print(tables)
# Sample Output 3:
#
# {1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': ['Borsh', 'Лапша', 'Гаспачо'],
#                                                  'desert': ['Медовик', 'Печенье', 'Наполеон', 'Наполеон', 'Вишня'],
#                                                  'drink': ['Cola', 'Чай', 'Кофе']}},
#  2: {'name': 'Vlad', 'is_vip': False, 'order': {'soup': ['Чечевичный'], 'salad': ['Цезарь', 'Мимоза'],
#                                                 'drink': ['Raf', 'Coffee', 'Juice'],
#                                                 'main_dish': ['Утка по-пекински', 'Отбивная'],
#                                                 'desert': ['Трюфель']}},
#  3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}}
# {1: {'name': 'Andrey', 'is_vip': True, 'order': {'drink': ['Cola', 'Чай', 'Кофе']}},
#  2: {'name': 'Vlad', 'is_vip': False, 'order': {'soup': ['Чечевичный'], 'salad': ['Цезарь', 'Мимоза'],
#                                                 'main_dish': ['Утка по-пекински', 'Отбивная']}},
#  3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}}


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
                if key in tables[n]['order']:
                    tables[n]['order'][key] += val.split(',')
                else:
                    tables[n]['order'][key] = val.split(',')


def delete_order(*,number_table, delete_all=False, **kwargs):
    if delete_all:
        tables[number_table]['order'] = {}
    else:
        for key, val in kwargs.items():
            if key in menu and val and key in tables[number_table]['order']:
                tables[number_table]['order'].pop(key)



tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
    2: None,
    3: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}
make_order(1, soup='Borsh,Лапша', desert='Медовик', drink='Cola')
make_order(1, soup='Гаспачо', desert='Печенье,Наполеон')
print(tables)

