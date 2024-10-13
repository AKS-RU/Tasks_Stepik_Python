#                    Декоратор reverse
# Реализуйте декоратор reverse, который сделает так, чтобы декорированная функция принимала все свои позиционные
# аргументы в обратном порядке. Именованные аргументы должны игнорироваться декоратором reverse.
#
# Sample Input:
#
# @reverse
# def get_max_index(*args):
#     if not args:
#         return None
#     max_index = 0
#     for i in range(len(args)):
#         if args[i] > args[max_index]:
#             max_index = i
#     return max_index
#
#
# print(get_max_index(1, 2, 3, 4, 5))
# print(get_max_index(3, 4, 1, 5, 2))
# print(get_max_index(5, 3, 4, 1, 2))
# print(get_max_index.__name__)
# Sample Output:
#
# 0
# 1
# 4
# get_max_index



from functools import wraps


def reverse(func):
    @wraps(func)
    def dec_reverse(*args, **kwargs):
        args = args[::-1]
        return func(*args, **kwargs)
    return dec_reverse


@reverse
def get_max_index(*args):
    if not args:
        return None
    max_index = 0
    for i in range(len(args)):
        if args[i] > args[max_index]:
            max_index = i
    return max_index


print(get_max_index(1, 2, 3, 4, 5))
print(get_max_index(3, 4, 1, 5, 2))
print(get_max_index(5, 3, 4, 1, 2))
print(get_max_index.__name__)