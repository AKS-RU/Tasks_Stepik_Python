# К нам обратились работники одного известного ресторана с просьбой написать приложение, которое позволяет автоматизировать процесс резервации столов. Одним из этапов процесса является определение свободных столов, чтобы затем можно было их предложить забронировать клиентам.
#
# Всего в ресторане имеется 9 столиков. Информация о брони хранится в глобальной переменной tables в словаре следующего формата
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
# Ключи здесь - номера столов, значения - имена клиентов, если бронь имеется, иначе None.
#
# По текущему состоянию бронирования видно, что только столик под номером 1 занят Андреем, все остальные столики
# свободны. Значение None является признаком того, что столик никем не занят.
#
# Ваша задача написать две функции, которые помогут определять какие столы сейчас свободны:
#
#     ✔  функцию is_table_free, которая принимает номер стола и возвращает ответ на вопрос: «Свободен ли данный
# стол?» в виде булева значения
#
#     ✔ функцию get_free_tables, которая вернет список всех свободных столов.
#
# Sample Input 1:
#
# tables = {
#   1: 'Andrey',
#   2: None,
#   3: None,
#   4: None,
#   5: 'Vasiliy',
#   6: None,
#   7: None,
#   8: 'Stas',
#   9: None,
# }
#
# print(is_table_free(1))
# print(is_table_free(2))
# print(get_free_tables())
# Sample Output 1:
#
# False
# True
# [2, 3, 4, 6, 7, 9]
# Sample Input 2:
#
# tables = {
#   1: 'Andrey',
#   2: None,
#   3: 'Gena',
#   4: None,
#   5: 'Vasiliy',
#   6: 'Chubaka',
#   7: None,
#   8: 'Stas',
#   9: None,
# }
#
# print(is_table_free(5))
# print(is_table_free(6))
# print(get_free_tables())
# Sample Output 2:
#
# False
# False
# [2, 4, 7, 9]

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


def get_free_tables():
    return [i for i in tables if tables.get(i) == None]


print(bool(is_table_free(1)))
print(get_free_tables())
