# Рекурсивный разворот списка
# Встроенная функция reversed позволяет расположить элементы упорядоченной коллекции в обратном порядке. Но работает
# данная функция только на первый уровень вложенности. Это значит, что результатом следующий инструкции
#
# print(list(reversed([[1, 2, 3], [4, 5], [6, 7, 8]])))
# будет следующий список
#
# [[6, 7, 8], [4, 5], [1, 2, 3]]
# Порядок элементов на втором уровне не поменялся.
#
# Ваша задача написать рекурсивную функцию reversed_recursive, которая принимает на вход вложенный список произвольной
# вложенности и располагает все элементы на каждом уровне в обратном направлении
#
# Ваша задача только написать определение рекурсивной функции reversed_recursive
#
# Sample Input 1:
#
# print(reversed_recursive([1, 2, 3, 4, 5]))
# Sample Output 1:
#
# [5, 4, 3, 2, 1]
# Sample Input 2:
#
# print(reversed_recursive([[1, 2, 3], [4, 5], [6, 7, 8]]))
# Sample Output 2:
#
# [[8, 7, 6], [5, 4], [3, 2, 1]]
# Sample Input 3:
#
# print(reversed_recursive([[1, 2, 3], [4, [5, [6]]], 7]))
# Sample Output 3:
#
# [7, [[[6], 5], 4], [3, 2, 1]]


def reversed_recursive(lst: list) -> list:
    result = lst[::]
    result.reverse()
    for value in result:
        if isinstance(value, list):
            value.reverse()
            reversed_recursive(value)
    return result




a = [[1, 2, 3], [4, [5, [6]]], 7]
print(reversed_recursive(a))
print(a)
