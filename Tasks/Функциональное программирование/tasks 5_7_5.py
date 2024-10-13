# Напишите функцию apply, которая принимает функцию и итерируемый объект (например, список) и применяет функцию к
# каждому элементу итерируемого объекта.
#
# В качестве ответа функция apply должна вернуть список из вычисленных значений.
#
# Sample Input 1:
#
# def square(num):
#     return num ** 2
#
# print(apply(square, [5, 7, 0, 3]))
# Sample Output 1:
#
# [25, 49, 0, 9]
# Sample Input 2:
#
# def repeater(value, n=5):
#     return str(value) * n
#
# print(apply(repeater, ['Hi', True, 0, [1, 2]]))
# Sample Output 2:
#
# ['HiHiHiHiHi', 'TrueTrueTrueTrueTrue', '00000', '[1, 2][1, 2][1, 2][1, 2][1, 2]']
# Sample Input 3:
#
# def repeater(value, n=5):
#     return str(value) * n
#
#
# print(apply(repeater, 'hello'))
# Sample Output 3:
#
# ['hhhhh', 'eeeee', 'lllll', 'lllll', 'ooooo']


def apply(func, lst):
    return [func(i) for i in lst]


def square(num):
    return num ** 2


print(apply(square, [5, 7, 0, 3]))