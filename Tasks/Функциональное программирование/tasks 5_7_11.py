# Функция aggregation - 2
# Перепишите функцию aggregation так, чтобы она возвращала итоговое значение агрегации.
#
# Функция aggregation по-прежнему должна принимать на вход функцию func и коллекцию элементов sequence.
#
# Sample Input 1:
#
# def get_add(x, y):
#     return x + y
#
#
# print(aggregation(get_add, [5, 2, 4, 3, 5]))
# Sample Output 1:
#
# 19
# Sample Input 2:
#
# def get_max(x, y):
#     return max(x, y)
#
# # агрегируем нахождение максимума
# print(aggregation(get_max, [1, 4, 5, 7, 6, 5, 8, 10, 5]))
# Sample Output 2:
#
# 10
# Sample Input 3:
#
# def get_min(x, y):
#     return min(x, y)
#
# # агрегируем нахождение минимума
# print(aggregation(get_min, [9, 6, 7, 8, 5, 1, 2, 4]))
# Sample Output 3:
#
# 1
# Sample Input 4:
#
# def get_product(x, y):
#     return x * y
#
# print(aggregation(get_product, [2, 6, 5, 10, 5, 1, 2]))
# Sample Output 4:
#
# 6000
# Sample Input 5:
#
# def get_add(x, y):
#     return x + y
#
# print(aggregation(get_add, [11, 4, 5, 7, 8, 10]))
# Sample Output 5:
#
# 45


def aggregation(func, data: list|tuple):
    result = []
    result.append(func(data[0], data[1]))
    for i in range(2,len(data)):
        result.append(func(result[-1], data[i]))
    return result[-1]


def get_add(x, y):
    return x + y


def get_add(x, y):
    return x + y

print(aggregation(get_add, [11, 4, 5, 7, 8, 10]))