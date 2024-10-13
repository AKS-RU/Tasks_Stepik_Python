# Поиск уровня
# Создайте рекурсивную функцию find_level_element, которая определяет на каком уровне вложенности располагается
# интересующий нас элемент. Нумерация уровней вложенности начинается с единицы.
#
# Функция find_level_element принимает некое значение value и список значений lst.
#
# Функция find_level_element должна вернуть номер уровня, где встречается первое найденное значение value в списке
# lst на любом уровне. Если же в lst отсутствует значение value, функция find_level_element должна вернуть -1.
#
# Sample Input 1:
#
# print(find_level_element(5, [1, 2, 3, 4, 5, [5]]))
# Sample Output 1:
#
# 1
# Sample Input 2:
#
# print(find_level_element(5, [1, 2, 3, 4, [[5]], [5]]))
# Sample Output 2:
#
# 3
# Sample Input 3:
#
# print(find_level_element(9, [1, 2, 3, 4, [[5]], [5]]))
# Sample Output 3:
#
# -1
# Sample Input 4:
#
# print(find_level_element(9, [1, 2, 3, 4, 5,
#                              [6, 7, 8,
#                               [[[9]], 1, [2, [3], 4], 5, 6]]]))
# Sample Output 4:
#
# 5

stack=[]
def find_level_element(value: int | float | str, lst: list, level=1) -> int:
    cnt = -1
    for i in lst:
        if isinstance(i, list):
            return find_level_element(value, i, level + 1)
        else:
            if value is i:
                cnt += 1
                return level
    if cnt != -1:
        return level
    return cnt





print(find_level_element(9, [1, 2, 3, 4, 5,
                             [6, 7, 8,
                              [[[9]], 1, [2, [3], 4], 5, 6]]]))