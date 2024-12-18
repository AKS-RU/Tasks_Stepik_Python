# Сортировка отрезков
# Напишите функцию get_sort_lines, которая принимает список кортежей, в котором хранится информация о координатах
# двух точек на координатной прямой. Функция get_sort_lines должна вернуть новый список, в котором элементы расположены
# в порядке возрастания расстояния между точками, хранящимися в одном элементе.
#
#
#
# В случае равенства расстояний необходимо сортировать по возрастанию значения координаты первой точки, затем
# по возрастанию значения второй точки
#
# Sample Input 1:
#
# lines = [(-4, 4), (2, 3), (5, 9), (-1, -3) ]
# print(get_sort_lines(lines))
# Sample Output 1:
#
# [(2, 3), (-1, -3), (5, 9), (-4, 4)]
# Sample Input 2:
#
# lines = [(5, 4), (2, 3), (1, 0), (-1, -2) ]
# print(get_sort_lines(lines))
# Sample Output 2:
#
# [(-1, -2), (1, 0), (2, 3), (5, 4)]
# Sample Input 3:
#
# lines = [(5, 6), (5, 4), (1, 0), (0, -1), (1, 2), (2, 1)]
# print(get_sort_lines(lines))
# Sample Output 3:
#
# [(0, -1), (1, 0), (1, 2), (2, 1), (5, 4), (5, 6)]


def get_sort_lines(lst: list[tuple[int, int]]) -> list[tuple[int, int]]:
    'Сортирует список кортежей по длине отрезка, первому значений, второму значению'
    return sorted(lst, key=lambda x: (abs(x[0]-x[1]),x[0],x[1]))



lines = [(5, 6), (5, 4), (1, 0), (0, -1), (1, 2), (2, 1)]
print(get_sort_lines(lines))
