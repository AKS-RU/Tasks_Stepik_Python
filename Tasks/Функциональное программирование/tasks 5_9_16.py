#                                       Чиним баги Кузьмы - 2
# Теперь убедитесь, что декоратор Кузьмы из предыдущего задания успешно работает и с другими функциями, вне
# зависимости от количества аргументов и их типов.
#
# Для решения задачи вам необходимо написать только определение функции-декоратора decorator.
#
#
#
# Для проверки правильности работы программы перед непосредственной отправкой пользуйтесь кнопкой «Запустить»
#
# Sample Input 1:
#
# @decorator
# def add(*values):
#     return sum(values)
#
# add(1, 4, 5, 6)
# Sample Output 1:
#
# ---Start calculation---
# ---Finish calculation. Result is 16---
# Sample Input 2:
#
# @decorator
# def add_with_factor(*values, factor=1):
#     return sum(values) * factor
#
#
# add_with_factor(1, 4, 5, 6, factor=2)
# Sample Output 2:
#
# ---Start calculation---
# ---Finish calculation. Result is 32---
# Sample Input 3:
#
# @decorator
# def concatenate(**kwargs):
#     result = ""
#     for arg in kwargs.values():
#         result += str(arg)
#     return result
#
# concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!")
# Sample Output 3:
#
# ---Start calculation---
# ---Finish calculation. Result is ЯВыучуЭтотПитон!---


def decorator(func):
    def wrapper(*args,**kwargs):
        print('---Start calculation---')
        result = func(*args, **kwargs)
        print(f'---Finish calculation. Result is {result}---')
        return result
    return wrapper


@decorator
def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += str(arg)
    return result


concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!")