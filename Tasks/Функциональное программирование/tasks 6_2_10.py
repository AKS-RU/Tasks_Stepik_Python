# Напишите функцию convert_to, которая имеет следующие параметры:
#
#     —   values - список однотипных элементов. Элементы могут быть типа float, int, str
#
#     —   type_to - необязательный параметр, по умолчанию принимает тип int
#
# Функция  convert_to должна конвертировать все элементы списка values в тип type_to и возвращать новый список в
# качестве результата. Используйте функцию map для конвертирования элементов
#
# Sample Input 1:
#
# numbers = [116, -411, 448, 636, -254, -295, 220, 216, 187, -150]
# print(convert_to(numbers, str))
# Sample Output 1:
#
# ['116', '-411', '448', '636', '-254', '-295', '220', '216', '187', '-150']
# Sample Input 2:
#
# numbers = [116, -411, 448, 636, -254, -295, 220, 216, 187, -150]
# print(convert_to(numbers, float))
# Sample Output 2:
#
# [116.0, -411.0, 448.0, 636.0, -254.0, -295.0, 220.0, 216.0, 187.0, -150.0]
# Sample Input 3:
#
# numbers = ['-383', '-101', '121', '40', '278', '118', '-462']
# print(convert_to(numbers))
# Sample Output 3:
#
# [-383, -101, 121, 40, 278, 118, -462]
# Sample Input 4:
#
# numbers = ['-383', '-101', '121', '40', '278', '118', '-462']
# print(convert_to(numbers, float))
# Sample Output 4:
#
# [-383.0, -101.0, 121.0, 40.0, 278.0, 118.0, -462.0]


def convert_to(values: list, type_to: str=int):
    return list(map(type_to, values))

numbers = ['-383', '-101', '121', '40', '278', '118', '-462']
print(convert_to(numbers))