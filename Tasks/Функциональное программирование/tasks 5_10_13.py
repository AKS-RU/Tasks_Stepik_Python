#               Валидация args
# Напишите декоратор validate_all_args_str, который проверяет на корректность (валидирует) переданные позиционные
# аргументы. Корректным он считает любое строковое значение, стоящее в позиционном аргументе; ключевые аргументы при
# проверке игнорируются. Если было передано хотя бы одно не строковое значение в позиционный аргумент, функция-декоратор
# validate_all_args_str должна
#
# вывести на экран фразу «Все аргументы должны быть строками»
# вернуть None и не запускать оригинальную  функцию
# Если же все аргументы корректны, validate_all_args_str запускает оригинальную функцию со всеми переданными значениями.
#
#
#
#
# Sample Input 1:
#
# @validate_all_args_str
# def concatenate(*args):
#     result = ""
#     for arg in args:
#         result += arg
#     return result
#
#
# print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))
# Sample Output 1:
#
# НуКогдаУжеЯВыучуПитон?
# Sample Input 2:
#
# @validate_all_args_str
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
# ЯВыучуЭтотПитон!
# Sample Input 3:
#
# @validate_all_args_str
# def concatenate(*args):
#     result = ""
#     for arg in args:
#         result += arg
#     return result
#
#
# print(concatenate("Через", 9, "Месяцев"))
# Sample Output 3:
#
# Все аргументы должны быть строками
# None
# Sample Input 4:
#
# @validate_all_args_str
# def concatenate(*args, **kwargs):
#     result = ""
#     for arg in args + tuple(kwargs.values()):
#         result += str(arg)
#     return result
#
#
# print(concatenate("Я", "думаю", "Выучить", "Питон", a="За", b=10, c="Месяцев"))
# Sample Output 4:
#
# ЯдумаюВыучитьПитонЗа10Месяцев


def validate_all_args_str(func):
    def validate(*args, **kwargs):
        if all(isinstance(i, str) for i in args):
            return func(*args, **kwargs)
        else:
            print('Все аргументы должны быть строками')
    return validate


@validate_all_args_str
def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += str(arg)
    return result


print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))
