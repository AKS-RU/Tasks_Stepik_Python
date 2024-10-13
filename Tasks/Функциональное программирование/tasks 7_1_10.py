# Функция range - 1
# Ваша задача создать функцию-генератор my_range_gen, которая имеет один параметр n.
#
# Функция my_range_gen должна генерировать по порядку все числа от 0 до n не включительно. В общем, быть копией
# встроенной функции range, вызванной от одного аргумента.
#
# Ваша задача написать только определение функции-генератора my_range_gen
#
# Sample Input:
#
# for value in my_range_gen(5):
#     print(value)
# Sample Output:
#
# 0
# 1
# 2
# 3
# 4


def my_range_gen(n: int):
    cnt = 0
    while cnt<n:
        yield cnt
        cnt+=1


for value in my_range_gen(10):
    print(value)
