# Декоратор limit_query
# Напишите декоратор limit_query, который ограничивает вызов оригинальной функции так, чтобы она могла вызываться не
# больше трех раз. Когда декорируемая функция исчерпает лимит вызовов, необходимо выводить на экран фразу
#
#  «Лимит вызовов закончен, все 3 попытки израсходованы»
#
# Если лимит исчерпан, оригинальная функция не должна быть вызвана, декоратор возвращает None
#
# Sample Input:
#
# @limit_query
# def add(a: int, b: int):
#     return a + b
#
# print(add(4, 5))
# print(add(5, 8))
# print(add(9, 43))
# print(add(10, 33))
# print(add.__name__)
# Sample Output:
#
# 9
# 13
# 52
# Лимит вызовов закончен, все 3 попытки израсходованы
# None
# add


from functools import wraps


def limit_query(func):
    cnt = 1
    @wraps(func)
    def inner_dec(*args, **kwargs):
        nonlocal cnt
        if cnt <= 3:
            cnt += 1
            return func(*args, **kwargs)
        else:
            print('Лимит вызовов закончен, все 3 попытки израсходованы')

    return inner_dec


@limit_query
def add(a: int, b: int):
    return a + b

print(add(4, 5))
print(add(5, 8))
print(add(9, 43))
print(add(10, 33))
print(add.__name__)
