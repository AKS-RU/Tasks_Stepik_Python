# Декоратор compose
# Ваша задача написать параметризированный декоратор compose, который принимает произвольное количество функций и
# применяет их последовательно к результату декорируемой функции
#
# Sample Input 1:
#
# def double_it(a):
#     return a * 2
#
#
# def increment(a):
#     return a + 1
#
# @compose(double_it, increment)
# def get_sum(*args):
#     return sum(args)
#
# print(get_sum(5))
# print(get_sum(20, 10))
# print(get_sum(5, 15, 25))
# Sample Output 1:
#
# 11
# 61
# 91
# Sample Input 2:
#
# def double_it(a):
#     return a * 2
#
#
# def increment(a):
#     return a + 1
#
# @compose(increment, increment, double_it)
# def get_sum(*args):
#     return sum(args)
#
# print(get_sum(5))
# print(get_sum(20, 10))
# print(get_sum(5, 15, 25))
# Sample Output 2:
#
# 14
# 64
# 94


from functools import wraps


def compose(*fnc: str):
    def decorator(func):
        @wraps(func)
        def dec_inner(*args, **kwargs):
            result = func(*args, **kwargs)
            for i in fnc:
                result = i(result)
            return result
        return dec_inner
    return decorator


def double_it(a):
    return a * 2


def increment(a):
    return a + 1

@compose(increment, increment, double_it)
def get_sum(*args):
    return sum(args)

print(get_sum(5))
print(get_sum(20, 10))
print(get_sum(5, 15, 25))