# Валидация kwargs
# Напишите декоратор validate_all_kwargs_int_pos, который проверяет на корректность переданные именованные аргументы.
# Корректным будет считаться именованный аргумент, значение которого является целым положительным числом. Позиционные
# аргументы игнорируются во время проверки декоратора validate_all_kwargs_int_pos.
#
# Если было передано хотя бы одно некорректное значение в именованный аргумент, функция-декоратор
# validate_all_kwargs_int_pos должна:
#
# вывести на экран фразу «Все именованные аргументы должны быть положительными числами»;
#
# вернуть None и не запускать оригинальную  функцию.
# Если же все аргументы корректны, validate_all_kwargs_int_pos запускает оригинальную функцию со всеми переданными
# значениями.
#
# Также для проверки вам необходимо скопировать из предыдущего шага реализацию декоратора validate_all_args_str,
# потому что в проверках будет использоваться валидация сразу и на *args, и на **kwargs.
#
# Sample Input 1:
#
# @validate_all_kwargs_int_pos
# def concatenate(*args, **kwargs):
#     result = ""
#     for arg in args + tuple(kwargs.values()):
#         result += str(arg)
#     return result
#
#
# print(concatenate(a="i", b='Love', c="Python"))
# Sample Output 1:
#
# Все именованные аргументы должны быть положительными числами
# None
# Sample Input 2:
#
# @validate_all_kwargs_int_pos
# def concatenate(*args, **kwargs):
#     result = ""
#     for arg in args + tuple(kwargs.values()):
#         result += str(arg)
#     return result
#
#
# print(concatenate(a=10, b=20, c=50))
# Sample Output 2:
#
# 102050
# Sample Input 3:
#
# @validate_all_args_str
# @validate_all_kwargs_int_pos
# def concatenate(*args, **kwargs):
#     result = ""
#     for arg in args + tuple(kwargs.values()):
#         result += str(arg)
#     return result
#
# print(concatenate('Hello', 2, 'World', a="i", b='Love', c="Python"))
# Sample Output 3:
#
# Все аргументы должны быть строками
# None


def validate_all_kwargs_int_pos(func):
    def validate(*args, **kwargs):
        if all(isinstance(v, int | float) and v>0 for v in kwargs.values()):
            return func(*args, **kwargs)
        else:
            print('Все именованные аргументы должны быть положительными числами')
    return validate

def validate_all_args_str(func):
    def validate(*args, **kwargs):
        if all(isinstance(i, str) for i in args):
            return func(*args, **kwargs)
        else:
            print('Все аргументы должны быть строками')
    return validate




@validate_all_kwargs_int_pos
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate(a=10, b=-20, c=50))

