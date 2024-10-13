# Сумма списка
# Напишите функцию sum_recursive, которая принимает на вход вложенный список, конечными элементами которого являются
# целые числа, и возвращает сумму элементов переданного списка. Уровень вложенности списка произвольный.
#
# Ваша задача только написать определение рекурсивной функции sum_recursive
#
# Sample Input 1:
#
# print(sum_recursive([1, 2, 3, 4, 5]))
# Sample Output 1:
#
# 15
# Sample Input 2:
#
# print(sum_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
# Sample Output 2:
#
# 36
# Sample Input 3:
#
# print(sum_recursive([1, 2, 3, 4, [[5]], [5]]))
# Sample Output 3:
#
# 20


def sum_recursive(lst: list)->int:
    total = 0
    for value in lst:
        # проверяем тип элемента
        if isinstance(value, list):
            # если это список, то
            # вызываем рекурсивный шаг для
            # нахождения суммы его элементов
            sum_nested = sum_recursive(value)
            total += sum_nested
        else:
            # Если это число, то сразу добавляем к total
            total += value

    return total


print(sum_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))