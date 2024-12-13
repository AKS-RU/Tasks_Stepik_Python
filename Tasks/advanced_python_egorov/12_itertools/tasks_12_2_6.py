# Двоичная система счисления
# Ваша задача написать функцию get_binary, которая принимает целое число n и выводит на экран все двоичные последовательности длины n в лексикографическом порядке.

# В двоичной системе присутствуют только цифры 0 и 1.

# Ваша задача написать только определение функции get_binary.

from itertools import product


def get_binary(n):
    for i in product('01', repeat=n):
        print(''.join(i))


get_binary(3)