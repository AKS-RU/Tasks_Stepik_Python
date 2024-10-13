# Лучшая оценка
# За все время обучения студенты сдают массу экзаменов и получают за них оценки. Университет решил собрать информацию
# о лучшей оценке у каждого студента. Ваша задача написать программу, которая проанализирует результаты всех экзаменов
# и найдет для каждого студента лучший балл
#
# Напишите функция get_info_marks, которая имеет следующие параметры:
#
#     —  students содержит имена студентов в виде списка (можете переименовать параметр по своему усмотрению). Это
# обязательный параметр;
#
#     —  marks - произвольное количество списков, в которых содержатся оценки (можете переименовать параметр по
# своему усмотрению).
#
# Функция get_info_marks должна найти лучшую оценку для каждого студента и составить из этих данных словарь, где
# ключ - имя студента, значение - лучшая оценка.
#
# Что касается оценок, это представляет собой несколько списков из целых чисел. Каждый список содержит оценки для
# студентов за один конкретный экзамен. По месту оценки в списке определяется, к какому студенту она относится.
#
# Sample Input 1:
#
# math = [90, 76, 94]
# history = [78, 79, 90]
# students = ["Marie", "Michael", "Marge"]
# print(get_info_marks(students, math, history))
# Sample Output 1:
#
# {'Marie': 90, 'Michael': 79, 'Marge': 94}
# Sample Input 2:
#
# math = [90, 76, 94]
# history = [78, 79, 90]
# geography = [95, 80, 92]
# students = ["Marie", "Michael", "Marge"]
# print(get_info_marks(students, math, geography, history))
# Sample Output 2:
#
# {'Marie': 95, 'Michael': 80, 'Marge': 94}
# Sample Input 3:
#
# math = [90, 76, 94]
# history = [78, 79, 90]
# geography = [95, 80, 92]
# music = [93, 98, 100]
# students = ["Marie", "Michael", "Marge"]
# print(get_info_marks(students, math, geography, history, music))
# Sample Output 3:
#
# {'Marie': 95, 'Michael': 98, 'Marge': 100}


def get_info_marks(students: str, *args):
    return {i[0]: max(list(i[1:])) for i in list(zip(students, *args))}





math = [90, 76, 94]
history = [78, 79, 90]
geography = [95, 80, 92]
music = [93, 98, 100]
students = ["Marie", "Michael", "Marge"]
print(get_info_marks(students, math, geography, history, music))
