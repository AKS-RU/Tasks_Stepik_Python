# Новая задача от создателей таких хитов как:
#
#     ✔  Автоматизируем ресторан: вакантные столы
#
#     ✔  Резервация столов: изменение требований - 2
#
# Настало время в нашем ресторане добавить возможность делать заказ посетителям ресторана. Они могут выбрать любую
# позицию из меню по следующим категориям:
#
# salad
# soup
# main_dish
# drink
# desert
#  Подумайте где и в каком виде можно хранить названия данных категорий
#
#
#
# Ваша задача переписать последнюю рабочую версию функции reserve_table (задача Резервация столов: изменение
# требований - 2) так, чтобы она создавала поле для хранения заказа (ключ «order» со значением пустой словарь).
# Вот такая структура должна получаться после резервации стола.
#
# tables = {
#     1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
#     2: None,
#     3: None,
#     4: None,
#     5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
#     6: None,
#     7: None,
#     8: None,
#     9: None,
# }
# В это поле мы далее будем складывать заказы при помощи функции make_order.
#
# Теперь самое интересное - функция make_order, которая принимает номер стола и далее перечисление желаемого.
#
# Вот примеры вызова функции make_order для стола номер 1
#
# make_order(1, soup='Borsh')
# make_order(1, desert='Наполеон', drink='Чай')
# Здесь мы видим, что человек сперва заказал борщ, а потом сделал повторный заказ, где  дозаказал десерт и напиток.
# итоге, в структуре данных по первому столу должна сохраниться следующая информация
#
# 1: {'is_vip': True,
#      'name': 'Andrey',
#      'order': {'desert': 'Наполеон', 'drink': 'Чай', 'soup': 'Borsh'}}
# Человек может сделать несколько заказов с одинаковыми категориями,
#
# make_order(1, soup='Borsh')
# make_order(1, desert='Наполеон', drink='Чай')
# make_order(1, desert='Медовик', drink='Кофе')
# в таком случае значения должны перезатираться и берется значение из последнего заказа
#
# 1: {'is_vip': True,
#      'name': 'Andrey',
#      'order': {'desert': 'Медовик', 'drink': 'Кофе', 'soup': 'Borsh'}
# Еще может быть такая ситуация, что человек заказывает еду не из перечисленных выше категорий или просит оказать
# услугу в рамках заказа. Тогда все имена ключей, которые не входят в перечисленные выше категории меню, не нужно
# записывать в итоговый заказ. Вот пример, где во втором заказе попросили принести салфетку и манную кашу.
#
# make_order(1, soup='Borsh')
# make_order(1, soup='Лапша', bring='Салфетку', meal='Манка')
# Имена bring и meal отсутствуют в категориях, поэтому структура заказа для стола 1 должна будет выглядеть так:
#
# 1: {'is_vip': True, 'name': 'Andrey', 'order': {'soup': 'Лапша'}}
#
#
# Для успешного решения задания вам необходимо определить функции reserve_table и make_order. Возможно понадобится
# продублировать функции, от которых зависела работа перечисленных ранее функций. Не забывайте про кнопку
# «Запустить код» для проверки работоспособности программы перед отправкой.
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
# make_order(1, desert='Наполеон', drink='Чай')
# print(tables)
# Sample Output 1:
#
# {1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Borsh', 'desert': 'Наполеон', 'drink': 'Чай'}},
#  2: None, 3: None, 4: None, 5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}}
# Sample Input 2:
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
# make_order(1, desert='Наполеон', drink='Чай')
# make_order(1, desert='Медовик', drink='Кофе')
# print(tables)
# Sample Output 2:
#
# {1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Borsh', 'desert': 'Медовик', 'drink': 'Кофе'}},
#  2: None, 3: None, 4: None, 5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}}}
# Sample Input 3:
#
# tables = {
#     1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
#     2: None,
#     3: None,
#     4: None,
#     5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
# }
# make_order(1, soup='Borsh')
# make_order(1, soup='Лапша', bring='Салфетку', meal='Манка')
#
# reserve_table(2, 'Vlad')
#
# make_order(2, soup='Чечевичный', salad='Цезарь', breakfast='Яичница')
# make_order(2, drink='Raf', main_dish='Утка по-пекински')
# make_order(2, desert='Трюфель', call='такси')
# print(tables)
# Sample Output 3:
#
# {1: {'name': 'Andrey', 'is_vip': True, 'order': {'soup': 'Лапша'}},
#  2: {'name': 'Vlad', 'is_vip': False, 'order': {'soup': 'Чечевичный', 'salad': 'Цезарь', 'drink': 'Raf', 'main_dish':
#      'Утка по-пекински', 'desert': 'Трюфель'}}, 3: None, 4: None, 5: {'name': 'Vasiliy', 'is_vip': False,
#                                                                       'order': {}}}




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


tables = {
    1: {'name': 'Andrey', 'is_vip': True, 'order': {}},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False, 'order': {}},
}
make_order(1, soup='Borsh')
make_order(1, soup='Лапша', bring='Салфетку', meal='Манка')

reserve_table(2, 'Vlad')

make_order(2, soup='Чечевичный', salad='Цезарь', breakfast='Яичница')
make_order(2, drink='Raf', main_dish='Утка по-пекински')
make_order(2, desert='Трюфель', call='такси')
print(tables)
