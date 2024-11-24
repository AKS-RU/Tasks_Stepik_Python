# Напишите функцию find_most_common_element, которая принимает список и находит наиболее
# распространенный элемент заданного списка.


from collections import Counter
from typing import Optional


def find_most_common_element(lst: list[int]) -> Optional[int]:
    result = (Counter(lst).most_common())
    if result:
        return result[0][0]


assert find_most_common_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4
assert find_most_common_element([3, 8, 7, 3, 3, 5, 3, 5, 1, 3, 3]) == 3
assert find_most_common_element([1, 2, 3]) == 1
assert find_most_common_element([5]) == 5

print('OK')
