# Декоратор pass_arguments
# Ваша задача написать параметризированный декоратор pass_arguments, который принимает произвольное количество
# именованных и позиционных аргументов и пробрасывает их дополнительно к аргументам, которые передаются при
# вызове оригинальной функции
#
# Sample Input 1:
#
# @pass_arguments(1, 2, 3)
# def add(*values):
#     return sum(values)
#
# print(add(5, 4, 6))
# Sample Output 1:
#
# 21
# Sample Input 2:
#
# @pass_arguments(s='Когда', w='-', r='нибудь!')
# def concatenate(**kwargs):
#     result = ""
#     for arg in kwargs.values():
#         result += str(arg)
#     return result
#
#
# print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))
# Sample Output 2:
#
# ЯВыучуЭтотПитон!Когда-нибудь!
# Sample Input 3:
#
# @pass_arguments(a=10, b=2, c=30)
# def calculate(a, b, c):
#     return a ** b + c
#
# print(calculate())
# Sample Output 3:
#
# 130
# Sample Input 4:
#
# @pass_arguments(one='Я', two='Точно', three='Говорю')
# def concatenate(**kwargs):
#     return ''.join([str(val) for val in kwargs.values()])
#
#
# print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))
# print(concatenate(q='Пенза-', w="лучший", we="город", s="Земли!"))
# Sample Output 4:
#
# ЯВыучуЭтотПитон!ЯТочноГоворю
# Пенза-лучшийгородЗемли!ЯТочноГоворю

from functools import wraps


def pass_arguments(*args_d, **kwargs_d):
    def decorator(func):
        @wraps(func)
        def dec_inner(*args, **kwargs):
            if len(args) == 0 and len(kwargs) == 0:
                return func(*args_d, **kwargs_d)
            return func(*args, **kwargs)+func(*args_d, **kwargs_d)
        return dec_inner
    return decorator


@pass_arguments(a=10, b=2, c=30)
def calculate(a, b, c):
    return a ** b + c

print(calculate())
