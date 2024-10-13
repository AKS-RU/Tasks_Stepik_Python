# Произведение элементов списка
# Напишите функцию multu_recursive, которая принимает на вход вложенный список, конечными элементами которого являются
# целые числа  и строки, и возвращает произведение числовых элементов переданного списка. Уровень вложенности исходного
# списка произвольный.
#
# Произведение пустого списка должно быть равно 1. Также единице должно быть равно произведение списка, в котором нету
# ни одного числового значения.
#
# Ваша задача только написать определение рекурсивной функции multu_recursive
#
# Sample Input 1:
#
# print(multu_recursive([1, 2, 3, 4, 5]))
# Sample Output 1:
#
# 120
# Sample Input 2:
#
# print(multu_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
# Sample Output 2:
#
# 40320
# Sample Input 3:
#
# print(multu_recursive([1, 2, 3, 4, [[5]], [5]]))
# Sample Output 3:
#
# 600
# Sample Input 4:
#
# print(multu_recursive(['1', '2', '3', '4', '5']))
# Sample Output 4:
#
# 1


def multu_recursive(lst: list) -> int:
    result = 1
    for value in lst:
        if isinstance(value, list):
            result *= multu_recursive(value)
        else:
            if isinstance(value, int):
                result *= value
    return result


print(multu_recursive(['1', '2', '3', '4', '5']))
