# Продолжаем автоматизировать работу ресторана. Следующим этапом является резервация(закрепление) свободного столика
# за клиентом и отмена брони. Структура хранения резерваций все та же в виде словаря:
#
# tables = {
#   1: 'Andrey',
#   2: None,
#   3: None,
#   4: None,
#   5: None,
#   6: None,
#   7: None,
#   8: None,
#   9: None,
# }
# Ваша задача написать две функции, которые помогут создавать и удалять бронирование:
#
#     ✔  функцию reserve_table, которая принимает номер стола и имя клиента, проверяет свободен ли указанный столик и
# если за ним никто не прикреплен, вносятся данные клиента. Больше данная функция ничего не делает. Для реализации этой
# функции можете воспользоваться функцией is_table_free из задания «Автоматизируем ресторан: вакантные столы»
#
#     ✔ функцию delete_reservation, которая очищает запись о бронировании.
#
# Sample Input 1:
#
# tables = {
#     1: 'Andrey',
#     2: None,
#     3: 'Gena',
#     4: 'Artem',
#     5: 'Vasiliy',
#     6: None,
#     7: 'Artur',
#     8: None,
#     9: 'Misha',
# }
# print(tables)
# delete_reservation(1)
# delete_reservation(3)
# reserve_table(6, 'Chubaka')
# print(tables)
# Sample Output 1:
#
# {1: 'Andrey', 2: None, 3: 'Gena', 4: 'Artem', 5: 'Vasiliy', 6: None, 7: 'Artur', 8: None, 9: 'Misha'}
# {1: None, 2: None, 3: None, 4: 'Artem', 5: 'Vasiliy', 6: 'Chubaka', 7: 'Artur', 8: None, 9: 'Misha'}
#
# Sample Input 2:
#
# tables = {
#     1: 'Andrey',
#     2: None,
#     3: None,
#     4: None,
#     5: 'Vasiliy',
#     6: None,
#     7: None,
#     8: None,
#     9: 'Misha',
# }
#
# print(tables)
# reserve_table(3, 'Gena')
# reserve_table(4, 'Artem')
# reserve_table(5, 'Artur') # Артур не должен занять место Василия
# print(tables)
# Sample Output 2:
#
# {1: 'Andrey', 2: None, 3: None, 4: None, 5: 'Vasiliy', 6: None, 7: None, 8: None, 9: 'Misha'}
# {1: 'Andrey', 2: None, 3: 'Gena', 4: 'Artem', 5: 'Vasiliy', 6: None, 7: None, 8: None, 9: 'Misha'}

tables = {
    1: 'Andrey',
    2: None,
    3: None,
    4: None,
    5: 'Vasiliy',
    6: None,
    7: None,
    8: 'Stas',
    9: None,
}


def is_table_free(n: int):
    return not bool(tables.get(n))

def reserve_table(n: int, name: str):
    if is_table_free(n):
        tables[n]=name


def delete_reservation(n: int):
    tables[n]= None


reserve_table(9,'hjhjhj')
delete_reservation(9)