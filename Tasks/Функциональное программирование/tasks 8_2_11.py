# Сумма списка
# Напишите функцию sum_recursive, которая принимает на вход одномерный список из целых чисел и возвращает сумму элементов
# переданного списка. Не забывайте, что реализовать это нужно при помощи рекурсии.
#
# Ваша задача только написать определение функции sum_recursive
#
# Sample Input:
#
# print(sum_recursive([1, 2, 3]))
# Sample Output:
#
# 6


def sum_recursive(lst: list)-> int:
    if len(lst)==1:
        return lst[0]
    a = sum_recursive(lst[1:])
    return a+lst[0]

print(sum_recursive([1, 2, 3,4]))

