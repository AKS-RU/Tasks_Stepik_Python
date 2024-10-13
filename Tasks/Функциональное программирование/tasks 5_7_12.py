# Функция aggregation - 3
# Перепишите функцию aggregation с прошлого шага так, чтобы у нее появился необязательный параметр initial по умолчанию
# равный None. Данный параметр отвечает за начальное состояние агрегации, если в него передать значение.
# Если ничего не передавать в initial, то функция aggregation работает как прежде
#
# Sample Input 1:
#
# def get_add(x, y):
#     return x + y
#
#
# print(aggregation(get_add, [5, 2, 4, 3, 5], initial=10))
# Sample Output 1:
#
# 29
# Sample Input 2:
#
# def get_add(x, y):
#     return x + y
#
# print(aggregation(get_add, [11, 4, 5, 7, 8, 10]))
# Sample Output 2:
#
# 45
# Sample Input 3:
#
# print(aggregation(lambda x, y: x + y, [4, 5, 6], initial=100))
# Sample Output 3:
#
# 115
# Sample Input 4:
#
# def get_product(x, y):
#     return x * y
#
# print(aggregation(get_product, [2, 5, 10, 1, 2]))
# Sample Output 4:
#
# 200
# Sample Input 5:
#
# print(aggregation(lambda x, y: x * y, [2, 5, 10, 1, 2], initial=50))
# Sample Output 5:
#
# 10000

def aggregation(func, data: list | tuple, initial=None):
    result = []
    if initial is None:
        result.append(func(data[0], data[1]))
        for i in range(2, len(data)):
            result.append(func(result[-1], data[i]))
        return result[-1]
    else:
        result.append(initial)
        for i in range(len(data)):
            result.append(func(result[-1], data[i]))
        return result[-1]



def get_product(x, y):
    return x * y

print(aggregation(lambda x, y: x * y, [2, 5, 10, 1, 2], initial=50))
