# Декоратор multiply_result_by
# Создайте декоратор multiply_result_by, который принимает аргумент N и возвращает функцию-декоратор, которая
# умножает результат декорированной функции на N
#
# Sample Input 1:
#
# @multiply_result_by(2)
# def my_function(x, y):
#     return x + y
#
# print(my_function(5, 6))
# Sample Output 1:
#
# 22
# Sample Input 2:
#
# @multiply_result_by(3)
# @multiply_result_by(4)
# def my_function(x, y):
#     return x + y
#
#
# print(my_function(2, 3))
# Sample Output 2:
#
# 60


from functools import wraps


def multiply_result_by(n:int|float):
    def decorator(func):
        @wraps(func)
        def dec_inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return result*n
        return dec_inner
    return decorator


@multiply_result_by(3)
@multiply_result_by(4)
def my_function(x, y):
    return x + y


print(my_function(2, 3))

