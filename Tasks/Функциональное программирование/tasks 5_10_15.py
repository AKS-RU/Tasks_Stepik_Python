# Фильтрация аргументов
# Ваша задача создать два декоратора
#
#     1️⃣ filter_even, который фильтрует только позиционные аргументы. Среди всех переданных значений он оставляет только
# четные числа, False и коллекции, длина которых четная
#
#     2️⃣ delete_short, который фильтрует только именованные аргументы. Среди всех переданных значений он оставляет только
# те, имена которых более четырех символов
#
# Sample Input 1:
#
# @delete_short
# def info_kwargs(**kwargs):
#     """Выводит информацию о переданных kwargs"""
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
#
# info_kwargs(first_name="John", last_name="Doe", age=33)
# Sample Output 1:
#
# first_name = John
# last_name = Doe
# Sample Input 2:
#
# @filter_even
# def concatenate(*args):
#     result = ""
#     for arg in args:
#         result += arg
#     return result
#
# print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))
# Sample Output 2:
#
# НуПитон?
# Sample Input 3:
#
# @filter_even
# @delete_short
# def concatenate(*args, **kwargs):
#     result = ""
#     for arg in args + tuple(kwargs.values()):
#         result += str(arg)
#     return result
#
#
# print(concatenate("Я", "хочу", "Выучить", "Питон", a="За", qwerty=10, c="Месяцев"))
# Sample Output 3:
#
# хочу10


def delete_short(func):
    def delete(*args, **kwargs):
        dct = {}
        dct = {k: v for k, v in kwargs.items() if len(str(k)) > 4}
        return func(*args,**dct)

    return delete


def filter_even(func):
    def filter(*args, **kwargs):
        lst = [i for i in args if
               isinstance(i, int) and i % 2 == 0 or i == False or isinstance(i, str | list | tuple | dict) and len(
                   i) % 2 == 0]
        return func(*lst,**kwargs)

    return filter


@filter_even
@delete_short
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate("Я", "хочу", "Выучить", "Питон", a="За", qwerty=10, c="Месяцев"))
