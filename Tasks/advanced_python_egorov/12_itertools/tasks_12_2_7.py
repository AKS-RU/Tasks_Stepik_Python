# Ваша задача написать функцию get_binary_advanced, которая принимает целые числа N и K выводит
# на экран все двоичные последовательности длины N в лексикографическом порядке, в которых
# содержится ровно K единиц.

# В двоичной системе присутствуют только цифры 0 и 1.

# Ваша задача написать только определение функции get_binary_advanced.

import itertools


def get_binary_advanced(n, k):
    for i in itertools.product('01', repeat=n):
        if i.count('1') == k:
            print(''.join(i))


get_binary_advanced(4, 2)
