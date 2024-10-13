# Напишите рекурсивную функцию find_min, которая найдет наименьшее число в списке. Для этого функция принимает в качестве
# аргумента список для поиска наименьшего значения
#
# Sample Input 1:
#
# numbers = [10, 32, 24, 17, -5, 10, -22]
# print(find_min(numbers))
# Sample Output 1:
#
# -22
# Sample Input 2:
#
# numbers = [-230, 101, 323, -200, 17, -5, 10, -22]
# print(find_min(numbers))
# Sample Output 2:
#
# -230


def find_min(lst: list) -> int:
    if len(lst) == 1:
        return lst[0]
    min_find=find_min(lst[1:])
    if lst[0]<min_find:
        min_find=lst[0]
    return min_find


numbers = [-230, 101, 323, -200, 17, -5, 10, -22]
print(find_min(numbers))
print(numbers)
