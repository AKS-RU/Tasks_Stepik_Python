# Свой print
# Создайте функцию custom_print, которая должна делать все то же самое, что и обычный print,
# только выводить значения через запятую

from functools import partial


def custom_print(*args):
    print(*args, sep=', ')


custom_print(1, 2, 3)
custom_print("Hi", True, 'Hello')
custom_print([1, 2, 3], {1, 2}, None)
