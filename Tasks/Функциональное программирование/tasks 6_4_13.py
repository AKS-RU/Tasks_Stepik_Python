# Напишите функцию zip_with_function(), которая принимает список списков и функцию, которая принимает несколько
# аргументов и возвращает значение. Функция zip_with_function() должна использовать функцию zip() для объединения
# списков в кортежи, а затем применять заданную функцию к кортежам из соответствующих позиций каждого списка.
# Результатом должен быть новый список, содержащий значения, возвращаемые функцией для каждой комбинации элементов.
#
# Например, имеется функция
#
# def get_sum_two_numbers(a, b):
#     return a + b
# Тогда вызов
#
# zip_with_function([[1, 2, 4], [3, 5, 8]], get_sum_two_numbers)
# должен вернуть список [4, 7, 12].
#
# Ваша задача написать только определение функции zip_with_function
#
# Sample Input 1:
#
# def get_sum_two_numbers(a: int, b: int) -> int:
#     return a + b
#
#
# print(zip_with_function([[1, 2, 4], [3, 5, 8]], get_sum_two_numbers))
# Sample Output 1:
#
# [4, 7, 12]
# Sample Input 2:
#
# def get_sum_two_numbers(a: int, b: int) -> int:
#     return a + b
#
# print(zip_with_function([[10, 20], [30, 0]], get_sum_two_numbers))
# Sample Output 2:
#
# [40, 20]
# Sample Input 3:
#
# def get_sum_three_numbers(a: int, b: int, c: int) -> int:
#     return a + b + c
#
# print(zip_with_function([[2, 5, 8], [3, 4, 7], [5, 6, 5]], get_sum_three_numbers))
# Sample Output 3:
#
# [10, 15, 20]

def zip_with_function(lst: list[list[int]], func):
    return [func(*i) for i in zip(*lst)]



def get_sum_three_numbers(a: int, b: int, c: int) -> int:
    return a + b + c

print(zip_with_function([[2, 5, 8], [3, 4, 7], [5, 6, 5]], get_sum_three_numbers))