# Напишите функцию find_max, которая принимает список целых чисел и возвращает значение
# самого большого элемента

# Примечание: используйте для решения функцию reduce

from functools import reduce


def find_max(lst: list) -> int:
    return reduce(lambda x, y: x if x > y else y, lst)


print(find_max([10, 20, 4, 45, 99]))
print(find_max([-10, 20, 4, -45, -99]))
