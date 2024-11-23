# У вас есть данные о количестве учеников в разных классах. Напишите функцию count_students,
# которая принимает на вход кортеж с данными о классах и количестве учеников в каждом классе,
# а затем возвращает объект Counter, где ключами являются названия классов,
# а значениями - общее количество учеников в каждом классе.
#
# В данных могут повторяться классы, в таком случае значение учеников нужно суммировать


from collections import Counter


def count_students(data: tuple) -> Counter:
    result = Counter()
    for k, v in data:
        result[k] += v
    return result


# Ниже располагаются проверки для функции count_students

classes_1 = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)
assert count_students(classes_1) == Counter({'VI': 6, 'V': 3, 'VII': 1})

classes_2 = (
    ('V', 20),
    ('VI', 15),
    ('VII', 18),
    ('V', 25),
)
assert count_students(classes_2) == Counter({'V': 45, 'VII': 18, 'VI': 15})

classes_3 = ()
assert count_students(classes_3) == Counter()

# Тест 3: Один класс
classes_4 = (
    ('IX', 30),
)
# Ожидаемый результат: {'IX': 30}
assert count_students(classes_4) == Counter({'IX': 30})

# Тест 4: Разные классы без учеников
classes_5 = (
    ('IV', 0),
    ('VIII', 0),
    ('X', 0),
)
assert count_students(classes_5) == Counter({'IV': 0, 'VIII': 0, 'X': 0})
