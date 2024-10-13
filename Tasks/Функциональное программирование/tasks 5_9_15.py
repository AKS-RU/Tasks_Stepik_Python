#                                        Чиним баги Кузьмы
# Программист Кузьма познакомился с декораторами и решил написать свой первый пример, где он пытался сопроводить вызов
#                                        функции add дополнительными выводами на экран. Вот что получилось:
#
# def decorator(func):
#     def wrapper():
#         print('---Start calculation---')
#         result = func()
#         print(f'---Finish calculation. Result is {result}---')
#         return result
#     return wrapper
#
#
# @decorator
# def add(a, b):
#     return a + b
# По его задумке декоратор должен сопровождать вызов декорируемой функции сообщениями
#
# ---Start calculation---
#
# и
#
# ---Finish calculation. Result is {result}---
#
# Но во время тестирования функции add Кузьма столкнулся с ошибкой
#
# takes 0 positional arguments but 2 were given
# Помогите исправить его декоратор так, чтобы все заработало.
#
#
#
# Для проверки правильности работы программы перед непосредственной отправкой пользуйтесь кнопкой «Запустить»
#
# Sample Input 1:
#
# add(1, 4)
# Sample Output 1:
#
# ---Start calculation---
# ---Finish calculation. Result is 5---
# Sample Input 2:
#
# add(100, 24)
# Sample Output 2:
#
# ---Start calculation---
# ---Finish calculation. Result is 124---
# Sample Input 3:
#
# add(10, 20)
# add(50, 7)
# Sample Output 3:
#
# ---Start calculation---
# ---Finish calculation. Result is 30---
# ---Start calculation---
# ---Finish calculation. Result is 57---




def decorator(func):
    def wrapper(*args,**kwargs):
        print('---Start calculation---')
        result = func(*args, **kwargs)
        print(f'---Finish calculation. Result is {result}---')
        return result
    return wrapper


@decorator
def add(a, b):
    return a + b



add(1, 4)