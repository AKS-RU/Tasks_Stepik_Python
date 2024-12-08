# Напишите функцию check_list, которая по входящему списку, состоящему из целых чисел,
# возвращает логическое значение следующим образом:

# False, когда хотя бы один элемент в списке равен 0
# True в остальных случаях
# Примечание: используйте для решения функцию reduce

from functools import reduce


def check_list(lst: list) -> bool:
    return bool(reduce(lambda x, y: x if x < y else y, lst))


print(check_list([5, 2, 3, 4, 1, 0, 6]))
