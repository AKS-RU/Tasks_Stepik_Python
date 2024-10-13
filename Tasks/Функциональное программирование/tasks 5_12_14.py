# Декоратор add_attrs
# Ваша задача написать параметризированный декоратор add_attrs, который принимает произвольное количество
# именованных аргументов и на их основании добавляет новые атрибуты для оригинальной функции
#
# Sample Input 1:
#
# @add_attrs(test=True, ordered=True)
# def add(a, b):
#     return a + b
#
# print(add(10, 5))
# print(add.test)
# print(add.ordered)
# Sample Output 1:
#
# 15
# True
# True
# Sample Input 2:
#
# @add_attrs(hello='World', marks=[1, 2, 3], cash=100)
# def add(a, b):
#     return a + b
#
# print(add(10, 5))
# print(add.hello)
# print(add.marks)
# print(add.cash)
# print(getattr(add, 'ordered', None))
# Sample Output 2:
#
# 15
# World
# [1, 2, 3]
# 100
# None


from functools import wraps


def add_attrs(**attrs):
    def decorator(func):
        @wraps(func)
        def dec_inner(*args, **kwargs):
            for k, v in attrs.items():
                setattr(dec_inner, k, v)
            return func(*args, **kwargs)
        return dec_inner
    return decorator


@add_attrs(hello='World', marks=[1, 2, 3], cash=100)
def add(a, b):
    return a + b

print(add(10, 5))
print(add.hello)
print(add.marks)
print(add.cash)
print(getattr(add, 'ordered', None))