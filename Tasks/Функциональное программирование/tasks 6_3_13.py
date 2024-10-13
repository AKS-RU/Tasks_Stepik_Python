# Напишите функцию filter_numbers, которая принимает список целых чисел и возвращает новый список, который состоит
# только из четных чисел входного списка или из тех, которые по модулю больше 100.
#
# Sample Input 1:
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
# print(filter_numbers(numbers))
# Sample Output 1:
#
# [2, 4, 6]
# Sample Input 2:
#
# numbers = [-100, 2, -300, -400, 5, -60, -61, -101, 101]
# print(filter_numbers(numbers))
# Sample Output 2:
#
# [-100, 2, -300, -400, -60, -101, 101]


def filter_numbers(lst: list) -> list[int]:
    return list(filter(lambda x: abs(x) > 100 or x % 2 == 0, lst))


numbers = [-100, 2, -300, -400, 5, -60, -61, -101, 101]
print(filter_numbers(numbers))
