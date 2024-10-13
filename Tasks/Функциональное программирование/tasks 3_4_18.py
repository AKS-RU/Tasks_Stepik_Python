# Перепишите функцию my_func так, чтобы она стала чистой
#
# Sample Input 1:
#
# a = [10, 20, 30]
# res = my_func(a, 3)
# print(a)
# print(res)
# Sample Output 1:
#
# [10, 20, 30]
# [10, 20, 30, 1, 2, 3]
# Sample Input 2:
#
# b = [-3, -2, -1, 0]
# res = my_func(b, 5)
# print(b)
# print(res)
# Sample Output 2:
#
# [-3, -2, -1, 0]
# [-3, -2, -1, 0, 1, 2, 3, 4, 5]

def my_func(collection, n):
    lst = collection[::]
    for i in range(1, n + 1):
        lst.append(i)
    return lst

b = [-3, -2, -1, 0]
res = my_func(b, 5)
print(b)
print(res)