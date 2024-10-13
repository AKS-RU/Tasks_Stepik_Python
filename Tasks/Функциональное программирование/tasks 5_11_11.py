#                Декоратор explicit_args
# Реализуйте декоратор explicit_args, который не позволяет запускать оригинальную функцию, если были переданы
# позиционные аргументы. Декоратор explicit_args должен выводить фразу
#
# Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений
# и предотвращать запуск оригинальной функции
#
# Sample Input 1:
#
# @explicit_args
# def add(a: int, b: int) -> int:
#     '''Возвращает сумму двух чисел'''
#     return a + b
#
# print(add(10, 20))
# Sample Output 1:
#
# Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений
# None
# Sample Input 2:
#
# @explicit_args
# def add(a: int, b: int) -> int:
#     '''Возвращает сумму двух чисел'''
#     return a + b
#
# print(add(a=10, b=20))
# Sample Output 2:
#
# 30
# Sample Input 3:
#
# @explicit_args
# def add(a: int, b: int) -> int:
#     '''Возвращает сумму двух чисел'''
#     return a + b
#
# print(add(10, b=20))
# print(add.__name__)
# print(add.__doc__)
# Sample Output 3:
#
# Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений
# None
# add
# Возвращает сумму двух чисел


from functools import wraps


def explicit_args(func):
    @wraps(func)
    def dec_explicit_args(*args, **kwargs):
        if len(args):
            print('Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений')
        else:
            return func(*args, **kwargs)

    return dec_explicit_args


@explicit_args
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(10, b=20))
print(add.__name__)
print(add.__doc__)
