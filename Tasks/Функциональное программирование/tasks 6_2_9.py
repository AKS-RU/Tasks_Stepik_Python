# Напишите функцию increase_3, которая принимает список целых чисел.
#
# Функция  increase_3 должна увеличить каждый элемент входного списка втрое, сформировать из этих значений кортеж и
# вернуть в качестве результата.
#
# Sample Input 1:
#
# numbers = [16, -1, 8, 6, -5, -9, 22, 26, 7, -10]
# print(increase_3(numbers))
# Sample Output 1:
#
# (48, -3, 24, 18, -15, -27, 66, 78, 21, -30)
# Sample Input 2:
#
# numbers = [1238, 16, -53, -59, 10]
# print(increase_3(numbers))
# Sample Output 2:
#
# (3714, 48, -159, -177, 30)


def increase_3(lst: list)->tuple:
    return tuple(list(map(lambda x: x*3, lst)))

numbers = [1238, 16, -53, -59, 10]
print(increase_3(numbers))