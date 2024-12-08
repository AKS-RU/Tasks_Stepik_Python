# Напишите функцию check_list, которая по входящему списку, состоящему из целых чисел,
# возвращает логическое значение следующим образом:

# True , когда есть хотя бы один непустой элемент в списке

# False в остальных случаях
# Примечание: под непустым элементом подразумевается любой правдивый объект, то есть такой,
# который при преобразовании в значение bool будет равен True.

# Примечание: используйте для решения функцию reduce

from functools import reduce


def check_list(lst: list) -> bool:
    return bool(reduce(lambda x, y: x if x > y else y, filter(lambda x: bool(x) == True, lst), False))


print(check_list([0, '', None, []]))
print(check_list([5, 2, 3, 4, 1, 6]))
print(check_list([0, 5, '', None, []]))
