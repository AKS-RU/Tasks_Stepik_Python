# Помните у нас была реализована функция reserve_table ? Она принимала три обязательных значения: номер стола,
# имя клиента и статус VIP.
#
# Как только менеджеры узнали про параметр со значением по умолчанию они сразу решили попросить вас переписать
# функцию reserve_table так, чтобы статус VIP клиента был по умолчанию равен False. Потому что большинство клиентов
# не так часто заходят в данное заведение и по статистике больше обычных клиентов, нежели вип-персон.
#
# Sample Input 1:
#
# tables = {
#     1: {'name': 'Andrey', 'is_vip': True},
#     2: None,
#     3: None,
#     4: None,
#     5: None,
#     6: None,
#     7: None,
#     8: None,
#     9: {'name': 'Misha', 'is_vip': False},
# }
# print(tables)
# reserve_table(2, 'Niko', True)
# reserve_table(6, 'Chubaka') # не передается вип-статус
# print(tables)
# Sample Output 1:
#
# {1: {'name': 'Andrey', 'is_vip': True}, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9:
#     {'name': 'Misha', 'is_vip': False}}
# {1: {'name': 'Andrey', 'is_vip': True}, 2: {'name': 'Niko', 'is_vip': True}, 3: None, 4: None, 5: None, 6:
#     {'name': 'Chubaka', 'is_vip': False}, 7: None, 8: None, 9: {'name': 'Misha', 'is_vip': False}}
# Sample Input 2:
#
# tables = {
#     1: {'name': 'Andrey', 'is_vip': True},
#     2: None,
#     3: None,
#     4: None,
#     5: {'name': 'Vasiliy', 'is_vip': False},
#     6: None,
#     7: None,
#     8: None,
#     9: {'name': 'Misha', 'is_vip': False},
# }
# print(tables)
# reserve_table(2, 'Zhora')
# reserve_table(3, 'Stasya')
# reserve_table(6, 'Chubaka', True)
# reserve_table(7, 'Luc', True)
# print(tables)
# Sample Output 2:
#
# {1: {'name': 'Andrey', 'is_vip': True}, 2: None, 3: None, 4: None, 5:
#     {'name': 'Vasiliy', 'is_vip': False}, 6: None, 7: None, 8: None, 9: {'name': 'Misha', 'is_vip': False}}
# {1: {'name': 'Andrey', 'is_vip': True}, 2: {'name': 'Zhora', 'is_vip': False},
#  3: {'name': 'Stasya', 'is_vip': False}, 4: None, 5: {'name': 'Vasiliy', 'is_vip': False},
#  6: {'name': 'Chubaka', 'is_vip': True}, 7: {'name': 'Luc', 'is_vip': True}, 8: None,
#  9: {'name': 'Misha', 'is_vip': False}}

tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False},
    6: None,
    7: None,
    8: None,
    9: {'name': 'Misha', 'is_vip': False},
}


def is_table_free(n: int):
    return not bool(tables.get(n))


def reserve_table(n: int, name: str, bool=False):
    if is_table_free(n):
        tables[n] = {'name': name, 'is_vip': bool}


def delete_reservation(n: int):
    tables[n] = None

print(tables)
reserve_table(2, 'Zhora')
reserve_table(3, 'Stasya')
reserve_table(6, 'Chubaka', True)
reserve_table(7, 'Luc', True)
print(tables)