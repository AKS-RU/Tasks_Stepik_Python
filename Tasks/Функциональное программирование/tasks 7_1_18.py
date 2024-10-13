# Измените функцию-генератор my_range_gen так, чтобы она могла вызываться от одного или двух аргументов.
#
# Если вызов происходит от одного аргумента n, то my_range_gen  генерирует все числа от 0 до n не включительно.
#
# Если вызов происходит от двух аргументов a и b, то my_range_gen  генерирует все числа от a включительно до b не
# включительно.
#
# Sample Input 1:
#
# for value in my_range_gen(5):
#     print(value)
# Sample Output 1:
#
# 0
# 1
# 2
# 3
# 4
# Sample Input 2:
#
# for value in my_range_gen(3, 8):
#     print(value)
# Sample Output 2:
#
# 3
# 4
# 5
# 6
# 7
# Sample Input 3:
#
# for value in my_range_gen(7, 2):
#     print(value)
# print('End')
# Sample Output 3:
#
# End
# Sample Input 4:
#
# for value in my_range_gen(234, 241):
#     print(value)
# Sample Output 4:
#
# 234
# 235
# 236
# 237
# 238
# 239
# 240


def my_range_gen(a: int, b: int = 0):
    if b == 0:
        start, end = b, a
    else:
        start, end = a, b

    while start < end:
        yield start
        start += 1


for value in my_range_gen(234, 241):
    print(value)
