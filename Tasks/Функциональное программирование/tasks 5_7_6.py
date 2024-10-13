# Множественное вычисление
# Затем создайте функцию compute, которая принимает список функций и произвольное количество значений. Функция compute
# должна применить каждую функцию к каждому значению в переданном порядке и сформировать из полученных значений новый
# список, который и будет возвращаться в качестве ответа
#
# Sample Input 1:
#
# def square(num):
#     return num ** 2
#
# def inc(num):
#     return num + 1
#
# def dec(num):
#     return num - 1
#
# print(compute([square, inc, dec], 10))
# Sample Output 1:
#
# [100, 11, 9]
# Sample Input 2:
#
# def square(num):
#     return num ** 2
#
# def inc(num):
#     return num + 1
#
# def dec(num):
#     return num - 1
#
# print(compute([inc, dec, square], 10, 20, 30, 40))
# Sample Output 2:
#
# [11, 21, 31, 41, 9, 19, 29, 39, 100, 400, 900, 1600]
# Sample Input 3:
#
# def inc(num):
#     return num + 1
#
# def dec(num):
#     return num - 1
#
# def repeater(value, n=10):
#     return str(value) * n
#
# def square(num):
#     return num ** 2
#
# print(compute([repeater, dec, inc, square], 5, 7, 0, True))
# Sample Output 3:
#
# ['5555555555', '7777777777', '0000000000', 'TrueTrueTrueTrueTrueTrueTrueTrueTrueTrue', 4, 6, -1, 0, 6, 8, 1, 2,
# 25, 49, 0, 1]


def compute(func_lst, *args):
    return [f(i) for f in func_lst for i in args]



def inc(num):
    return num + 1

def dec(num):
    return num - 1

def repeater(value, n=10):
    return str(value) * n

def square(num):
    return num ** 2

print(compute([repeater, dec, inc, square], 5, 7, 0, True))