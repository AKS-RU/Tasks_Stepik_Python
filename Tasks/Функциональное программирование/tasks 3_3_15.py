# Через некоторое время менеджеры ресторана поняли, что помимо имени клиента, они бы еще хотели хранить его
# принадлежность к статусу VIP клиента. Соответственно, они бы хотели изменить структуру хранения резерваций
# на следующую:
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
#     9: None,
# }
# Здесь мы видим, что информация о клиенте хранится во вложенном словаре, у которого имеются два ключа name и is_vip.
#
# Исходя из новой структуры данных, ваша задача теперь сделать рефакторинг кода функции reserve_table. Теперь она
# должна принимать не два аргумента, а три: номер стола, имя клиента и статус VIP. Делать проверку свободен ли стол
# и если она пройдена, сохранять данные в описанной выше структуре
#
#
#
# Для успешного прохождения тестов скопируйте также реализацию функции delete_reservation  из задания «Резервация столов»
# и все ее зависимости от других функций, если они были

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


#
# tables[1] = {'name':tables.get(1), 'is_vip': True}
# print(tables)

def is_table_free(n: int):
    return not bool(tables.get(n))


def reserve_table(n: int, name: str, bool: bool):
    if is_table_free(n):
        tables[n] = {'name': name, 'is_vip': bool}


def delete_reservation(n: int):
    tables[n] = None

reserve_table(2,'hjhjh',True)
