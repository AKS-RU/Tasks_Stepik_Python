# Декоратор check_count_args
# Напишите декоратор check_count_args, который проверяет количество переданных аргументов. Проверка заключается
# в следующем
#
# в оригинальную функцию должно быть передано только два аргумента и неважно позиционно или по ключу. Если это условие
# выполняется, возвращаем результат вызова оригинальной функции
#
# Если передано меньшее количество, декоратор должен вывести строку «Not enough arguments» и не должен запускать
# оригинальную функцию;
#
# Если передано более двух аргументов, то декоратор должен вывести строку «Too many arguments» и не должен запускать
# оригинальную функцию.
# Не забывайте сохранять имя функции и строку документации. Для решения необходимо написать только реализацию
# декоратора check_count_args
#
# Sample Input 1:
#
# @check_count_args
# def add_numbers(x, y):
#     """Return sum of x and y"""
#     return x + y
#
#
# print(add_numbers(4, 5))
# print(add_numbers.__name__)
# print(add_numbers.__doc__.strip())
# Sample Output 1:
#
# 9
# add_numbers
# Return sum of x and y
# Sample Input 2:
#
# @check_count_args
# def add_numbers(x, y):
#     """Return sum of x and y"""
#     return x + y
#
#
# print(add_numbers(6, y=7))
# print(add_numbers.__name__)
# print(add_numbers.__doc__.strip())
# Sample Output 2:
#
# 13
# add_numbers
# Return sum of x and y
# Sample Input 3:
#
# @check_count_args
# def add_numbers(x, y):
#     """Return sum of x and y"""
#     return x + y
#
# add_numbers(4)
# Sample Output 3:
#
# Not enough arguments
# Sample Input 4:
#
# @check_count_args
# def add_numbers(x, y):
#     """Return sum of x and y"""
#     return x + y
#
# add_numbers(3, 5, 6)
# Sample Output 4:
#
# Too many arguments


from functools import wraps


def check_count_args(func):
    @wraps(func)
    def dec_check_count_args(*args, **kwargs):
        if len(args)+len(kwargs) ==2:
            return func(*args, **kwargs)
        elif len(args)+len(kwargs) > 2:
            return print('Too many arguments')
        else:
            return print('Not enough arguments')

    return dec_check_count_args


@check_count_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y


print(add_numbers(6, y=7))
print(add_numbers.__name__)
print(add_numbers.__doc__.strip())