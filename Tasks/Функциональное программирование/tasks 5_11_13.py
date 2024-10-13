# Декоратор monkey_patching
# Monkey patch -  это прием в программировании, который используется для динамического изменения поведения
# фрагмента кода во время выполнения.
#
# Ваша задача написать декоратор monkey_patching, который заменяет значения всех переданных аргументов при
# вызове оригинальной функции следующим образом:
#
#     ➕   значение каждого позиционного аргумента заменяется на строку «Monkey»
#
#     ➕   значение каждого именованного аргумента заменяется на строку «patching»
#
# Sample Input 1:
#
# @monkey_patching
# def concatenate(*args):
#     """
#     Возвращает конкатенацию переданных строк
#     """
#     return ', '.join(args)
#
#
# print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
# print(concatenate('my', 'name is', 'Artem'))
# print(concatenate.__name__)
# print(concatenate.__doc__.strip())
# Sample Output 1:
#
# Monkey, Monkey, Monkey, Monkey, Monkey
# Monkey, Monkey, Monkey
# concatenate
# Возвращает конкатенацию переданных строк
# Sample Input 2:
#
# @monkey_patching
# def info_kwargs(**kwargs):
#     """Выводит информацию о переданных kwargs"""
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
#
# info_kwargs(first_name="John", last_name="Doe", age=33)
# info_kwargs(c=43, b= 32, a=32)
# print(info_kwargs.__name__)
# print(info_kwargs.__doc__.strip())
# Sample Output 2:
#
# age = patching
# first_name = patching
# last_name = patching
# a = patching
# b = patching
# c = patching
# info_kwargs
# Выводит информацию о переданных kwargs
# Sample Input 3:
#
# @monkey_patching
# def print_args_kwargs(*args, **kwargs):
#     for i, value in enumerate(args):
#         print(i, value)
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
#
#
# print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)
# Sample Output 3:
#
# 0 Monkey
# 1 Monkey
# 2 Monkey
# 3 Monkey
# a = patching
# b = patching
# t = patching
# w = patching


from functools import wraps


def monkey_patching(func):
    @wraps(func)
    def dec_monkey_patching(*args,**kwargs):
        args = ['Monkey']*len(args)
        kwargs = {k:'patching' for k in kwargs}
        return func(*args, **kwargs)
    return dec_monkey_patching



@monkey_patching
def info_kwargs(**kwargs):
    """Выводит информацию о переданных kwargs"""
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')

info_kwargs(first_name="John", last_name="Doe", age=33)
info_kwargs(c=43, b= 32, a=32)
print(info_kwargs.__name__)
print(info_kwargs.__doc__.strip())