# Множественное вычисление-2
# Затем создайте функцию compute, которая принимает список функций и произвольное количество значений. Функция compute
# должна применить все функции сразу к каждому значению в переданном порядке и сформировать из полученных значений новый
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
# print(compute([square, inc], 10))
# Sample Output 1:
#
# [101]
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
# print(compute([inc, square, dec], 10, 20, 30, 40))
# Sample Output 2:
#
# [120, 440, 960, 1680]
# Sample Input 3:
#
# def inc(num):
#     return num + 1
#
# def dec(num):
#     return num - 1
#
# def repeater(value, n=3):
#     return str(value) * n
#
# def square(num):
#     return num ** 2
#
# print(compute([dec, inc, square, repeater], 5, 7, 0, True))
# Sample Output 3:
#
# ['252525', '494949', '000', '111']


def compute(func_lst, *args):
    result = []
    for i in args:
        for func in func_lst:
            i = func(i)
        result.append(i)
    return result

def square(num):
    return num ** 2

def inc(num):
    return num + 1

def dec(num):
    return num - 1

print(compute([square, inc], 10))
