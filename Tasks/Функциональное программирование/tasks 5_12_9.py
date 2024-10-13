# Ваша задача переписать декоратор monkey_patching. Ранее он заменял значения всех переданных аргументов при
# вызове оригинальной функции следующим образом:
#
#     ➕   значение каждого позиционного аргумента заменяется на строку «Monkey»
#
#     ➕   значение каждого именованного аргумента заменяется на строку «patching»
#
# Теперь необходимо завести параметры arg и kwarg, при помощи которых можно влиять на значения, которые будут
# проставляться в позиционные и именованные аргументы. Параметры arg и kwarg являются необязательными для передачи,
# их значения по умолчанию «Monkey» и «patching» соответственно.
#
# Sample Input 1:
#
# @monkey_patching(arg='Super')
# def print_args_kwargs(*args, **kwargs):
#     for i, value in enumerate(args):
#         print(i, value)
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
#
#
# print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)
# Sample Output 1:
#
# 0 Super
# 1 Super
# 2 Super
# 3 Super
# a = patching
# b = patching
# t = patching
# w = patching
# Sample Input 2:
#
# @monkey_patching(kwarg='Duper')
# def print_args_kwargs(*args, **kwargs):
#     for i, value in enumerate(args):
#         print(i, value)
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
#
# print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)
# Sample Output 2:
#
# 0 Monkey
# 1 Monkey
# 2 Monkey
# 3 Monkey
# a = Duper
# b = Duper
# t = Duper
# w = Duper
# Sample Input 3:
#
# @monkey_patching(kwarg='Duper', arg='Super')
# def print_args_kwargs(*args, **kwargs):
#     for i, value in enumerate(args):
#         print(i, value)
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
#
# print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)
# Sample Output 3:
#
# 0 Super
# 1 Super
# 2 Super
# 3 Super
# a = Duper
# b = Duper
# t = Duper
# w = Duper


from functools import wraps


def monkey_patching(arg='Monkey', kwarg='patching'):
    def decorator(func):

        @wraps(func)
        def dec_decorator(*args, **kwargs):
            args = [arg] * len(args)
            kwargs = {k: kwarg for k in kwargs}
            return func(*args, **kwargs)
        return dec_decorator
    return decorator


@monkey_patching(kwarg='Duper', arg='Super')
def print_args_kwargs(*args, **kwargs):
    for i, value in enumerate(args):
        print(i, value)
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')

print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)