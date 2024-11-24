# Найти разницу между двумя списками, включая повторяющиеся элементы
# Создайте функцию find_difference_with_counter(lst1, lst2), которая будет принимать два списка и
# возвращать список, содержащий отсортированные элементы, которые присутствуют в lst1,
# но отсутствуют в lst2, учитывая повторяющиеся элементы. Функция должна использовать
# класс Counter для выполнения этой задачи.


from collections import Counter


def find_difference_with_counter(lst1: list, lst2: list) -> list:

    return list((Counter(lst1)-Counter(lst2)).elements())


print(find_difference_with_counter([1, 2, 2, 3, 4, 4, 5],
                                   [2, 3, 3, 4, 5, 6]))
assert find_difference_with_counter([1, 2, 2, 3, 4, 4, 5],
                                    [2, 3, 3, 4, 5, 6]) == [1, 2, 4]
assert find_difference_with_counter([1, 1, 2, 3, 3, 4, 4, 5, 6, 7],
                                    [1, 1, 2, 4, 5, 6]) == [3, 3, 4, 7]

assert find_difference_with_counter([1, 1, 1, 1],
                                    [1, 1, ]) == [1, 1]

assert find_difference_with_counter([1, 1, ],
                                    [1, 1, 1, 1]) == []

print('OK')
