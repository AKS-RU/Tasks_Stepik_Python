# Поиск во вложенном списке
# Ранее мы уже делали проверку на вхождение элемента в линейный список. Теперь ваша задача переписать функцию is_member
# так, чтобы она могла искать элемент в списке с произвольной вложенностью.
#
# Функция принимает некое значение value и список значений lst.
#
# Функция is_member должна вернуть True, если значение value присутствует в списке lst на любом уровне, и False в
# противном случае.
#
# Sample Input 1:
#
# print(is_member(5, [1, 2, 3, 4, 5]))
# Sample Output 1:
#
# True
# Sample Input 2:
#
# print(is_member(8, [[1, 2, 3], [4, [5, 6]], 7]))
# Sample Output 2:
#
# False
# Sample Input 3:
#
# print(is_member(9, [1, 2, 3, 4, 5,
#                  [6, 7, 8,
#                   [9, 1, [2, [3], 4], 5, 6]]]))
# Sample Output 3:
#
# True


# def is_member(value: int | float | str, lst: list) -> bool:
#     result = []
#
#     def is_member_inner(lst_in: list)->list:
#         nonlocal result
#         for i in lst_in:
#             if isinstance(i, list):
#                 is_member_inner(i)
#             else:
#                 result.append(i is value)
#         return result
#
#     is_member_inner(lst)
#     return any(result)


def is_member(value: int | float | str, lst: list) -> bool:
    result = []
    for val in lst:
        if isinstance(val, list):
            result += [is_member(value, val)]
        else:
            result.append(val is value)
    return any(result)


print(is_member(9, [1, 2, 3, 4, 5,
                    [6, 7, 8,
                     [9, 1, [2, [3], 4], 5, 6]]]))
