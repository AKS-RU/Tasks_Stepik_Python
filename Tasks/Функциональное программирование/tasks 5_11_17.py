#   Декоратор counting_calls - 2
# Усовершенствуем ранее созданный декоратор counting_calls, добавив отслеживание переданных аргументов при
#   каждом вызове.
#
# Для этого декоратор counting_calls должен добавить в декорируемой функции атрибут calls - список, в который
#   будут сохраняться все переданные аргументы в момент вызова в виде словаря. Каждый словарь должен иметь два
#   ключа: args и kwargs для сохранения соответствующих аргументов.
#
# Sample Input 1:
#
# @counting_calls
# def add(a: int, b: int) -> int:
#     '''Возвращает сумму двух чисел'''
#     return a + b
#
#
# print(add.__name__)
# print(add.__doc__)
#
# print(add(10, b=20))
# print('Количество вызовов =', add.call_count)
# print(add.calls)
#
# print(add(5, 6))
# print(add.calls[1])
# Sample Output 1:
#
# add
# Возвращает сумму двух чисел
# 30
# Количество вызовов = 1
# [{'args': (10,), 'kwargs': {'b': 20}}]
# 11
# {'args': (5, 6), 'kwargs': {}}
# Sample Input 2:
#
# @counting_calls
# def add(a: int, b: int) -> int:
#     '''Возвращает сумму двух чисел'''
#     return a + b
#
# print(add(10, b=20))
# print(add(7, 5))
# print(add(12, 45))
# print('Количество вызовов =', add.call_count)
# print(add.calls[2])
#
# print(add(b=11, a=22))
# print(add.calls[3])
# Sample Output 2:
#
# 30
# 12
# 57
# Количество вызовов = 3
# {'args': (12, 45), 'kwargs': {}}
# 33
# {'args': (), 'kwargs': {'b': 11, 'a': 22}}

from functools import wraps

def counting_calls(func):
    func.call_count = 0
    func.calls = []
    @wraps(func)
    def dec_counting_calls(*args, **kwargs):
        dec_counting_calls.call_count += 1
        dec_counting_calls.calls.append({'args': args, 'kwargs': kwargs})
        return func(*args, **kwargs)
    return dec_counting_calls


@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(10, b=20))
print(add(7, 5))
print(add(12, 45))
print('Количество вызовов =', add.call_count)
print(add.calls[2])

print(add(b=11, a=22))
print(add.calls[3])
