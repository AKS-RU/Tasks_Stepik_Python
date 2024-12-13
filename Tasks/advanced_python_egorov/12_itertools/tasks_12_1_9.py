# Ваша задача написать функцию infinity_generate, которая принимает итерабельную последовательность
# и возвращает бесконечный итератор, циклически перебирающий элементы этой последовательности.

import itertools


def infinity_generate(lst: list):
    return itertools.cycle(lst)


count = 0
for i in infinity_generate('ABC'):
    print(i)
    count += 1
    if count > 10:
        break
