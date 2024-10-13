# Фильтрация
# Напишите функцию filter_list, которая принимает функцию f и список lst.
#
# Функция f обязательно должна проверять определенное условие и возвращать булев тип.
#
# Задача функции filter_list состоит в том, чтобы вернуть новый список, составленный из элементов входного lst,
# отфильтрованных согласно функции f.
#
# Sample Input 1:
#
# def is_even(num):
#     return num % 2 == 0
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = filter_list(is_even, numbers) # берем только четные
# print(even_numbers)
# Sample Output 1:
#
# [2, 4, 6, 8, 10]
# Sample Input 2:
#
# def is_positive(num):
#     return num > 0
#
# numbers = [-1, 2, -3, 4, 5, -6, 7, -8, -9, 10]
# positive_numbers = filter_list(is_positive, numbers) # берем только положительные
# print(positive_numbers)
# Sample Output 2:
#
# [2, 4, 5, 7, 10]



def filter_list(func, lst: list):
    return [i for i in lst if func(i)]



def is_positive(num):
    return num > 0

numbers = [-1, 2, -3, 4, 5, -6, 7, -8, -9, 10]
positive_numbers = filter_list(is_positive, numbers) # берем только положительные
print(positive_numbers)
