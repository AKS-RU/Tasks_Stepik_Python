# Валидация args - 2
# Помните декоратор validate_all_args_str, который проверял, что все переданные позиционные значения являются
# строками? А если вдруг нам потребуется создать декоратор, который будет проверять аргументы не на принадлежность
# к строке, а, скажем, к списку или числу? Тогда нам понадобится создавать отдельный декоратор на каждый тип данных.
# Или сделать параметризированный декоратор validate_all_args, который будет принимать тип данных в качестве аргумента
# и проверять, что все значения в args относятся к переданному типу данных.
#
# Ваша задача написать такой декоратор validate_all_args, который имеет параметр type_. Если все позиционные аргументы
# принадлежат типу type_, то запускается оригинальная функция; в противном случае необходимо отменить ее запуск и
# вывести сообщение
#
# Все аргументы должны принадлежать типу {type_}
#
# Sample Input 1:
#
# @validate_all_args(str)
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
# Все аргументы должны принадлежать типу <class 'str'>
# Sample Input 2:
#
# @validate_all_args(int)
# def print_args_kwargs(*args, **kwargs):
#     for i, value in enumerate(args):
#         print(i, value)
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
#
#
# print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)
# Sample Output 2:
#
# 0 1
# 1 2
# 2 3
# 3 4
# a = 100
# b = 300
# t = 50
# w = 40
# Sample Input 3:
#
# @validate_all_args(set)
# def print_args_kwargs(*args, **kwargs):
#     for i, value in enumerate(args):
#         print(i, value)
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
#
#
# print_args_kwargs([], [1], [1, 2], b=set(), w=set())
# Sample Output 3:
#
# Все аргументы должны принадлежать типу <class 'set'>
# Sample Input 4:
#
# @validate_all_args(list)
# def print_args_kwargs(*args, **kwargs):
#     for i, value in enumerate(args):
#         print(i, value)
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
#
#
# print_args_kwargs([], [1], [1, 2], b=set(), w=set())
# Sample Output 4:
#
# 0 []
# 1 [1]
# 2 [1, 2]
# b = set()
# w = set()


from functools import wraps


def validate_all_args(type_: str):


    def decorator(func):
        @wraps(func)
        def dec_inner(*args, **kwargs):
            if all(isinstance(i, type_) for i in args):
                return func(*args, **kwargs)
            else:
                print(f"Все аргументы должны принадлежать типу {type_}")

        return dec_inner
    return decorator




@validate_all_args(list)
def print_args_kwargs(*args, **kwargs):
    for i, value in enumerate(args):
        print(i, value)
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')


print_args_kwargs([], [1], [1, 2], b=set(), w=set())