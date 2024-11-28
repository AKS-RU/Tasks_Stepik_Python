#                   Группировка цветов
# Взгляните на список кортежей ниже

# [('red', 1), ('blue', 2), ('red', 2), ('blue', 2), ('red', 3), ('blue', 4), ('blue', 2)]
# Ваша задача выполнить группировку данных: нужно сгруппировать вместе все числа, которые имеют
# одинаковый цвет, причем исключить повторяющиеся значения. В данном случае ответ был бы следующим

# defaultdict({'red': {1, 2, 3}, 'blue': {2, 4}})
# Логику нахождения результата вам необходимо описать внутри функции group_by_color, она принимает
# список кортежей и возвращает defaultdict, в котором сгруппированы числа по цветам


from collections import defaultdict

# Напишите реализацию функции group_by_colors


def group_by_colors(colors: list[tuple[str, int]]) -> defaultdict:
    result = defaultdict(set)
    for key, value in colors:
        result[key].add(value)
    return result


# Ниже располагается код для проверки функции group_by_colors

result_1 = group_by_colors([('red', 1), ('blue', 2), ('red', 2),
                            ('blue', 2), ('red', 3), ('blue', 4),
                            ('blue', 2)])
assert isinstance(result_1, defaultdict)
assert dict(result_1) == {'red': {1, 2, 3}, 'blue': {2, 4}}

result_2 = group_by_colors(([('red', 1), ('blue', 2), ('red', 2), ('blue', 2),
                             ('red', 3), ('blue', 4), ('green', 1), ('green', 2),
                             ('red', 4), ('blue', 3), ('red', 5), ('blue', 6),
                             ('green', 3), ('green', 4), ('red', 6), ('blue', 5),
                             ('green', 5), ('green', 6), ('red', 7), ('blue', 7)]))

assert isinstance(result_2, defaultdict)
assert dict(result_2) == {'red': {1, 2, 3, 4, 5, 6, 7}, 'blue': {
    2, 3, 4, 5, 6, 7}, 'green': {1, 2, 3, 4, 5, 6}}

result_3 = group_by_colors([])
assert dict(result_3) == {}

result_4 = group_by_colors(
    [('blue', 5), ('blue', 5), ('blue', 5), ('blue', 5)])
assert dict(result_4) == {'blue': {5}}
print('Good')
