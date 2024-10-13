# Нахождение самого большого элемента списка
# Напишите функцию get_max_recursive, которая принимает на вход вложенный список, конечными элементами которого являются
# целые числа, и возвращает самый большой элемент переданного списка. Уровень вложенности исходного списка произвольный.
#
# Ваша задача только написать определение рекурсивной функции get_max_recursive
#
# Sample Input 1:
#
# print(get_max_recursive([1, 2, 3, 4, 5]))
# Sample Output 1:
#
# 5
# Sample Input 2:
#
# print(get_max_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
# Sample Output 2:
#
# 8
# Sample Input 3:
#
# print(get_max_recursive([1, 2, 3, 4, [[5]], [5]]))
# Sample Output 3:
#
# 5

def get_max_recursive(lst: list) -> int:
    total = 0
    for value in lst:
        if isinstance(value, list):
            x = get_max_recursive(value)
            if total < x:
                total = x
        else:
            if total < value:
                total = value
    return total


print(get_max_recursive([1, 2, 3, 4, [[5]], [5]]))
