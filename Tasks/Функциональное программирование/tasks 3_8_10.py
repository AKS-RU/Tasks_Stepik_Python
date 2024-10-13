# Создадим функцию print_scores, которая выводит результаты, набранные учеником в тесте.
#
# Функция принимает имя студента и его оценки, их может быть произвольное количество.
#
# Функция сперва выводит имя студента, а затем на отдельных строках все его оценки в порядке возрастания
#
# Sample Input:
#
# print_scores("Jud", 100, 95, 88, 92, 99)
# Sample Output:
#
# Student name: Jud
# 88
# 92
# 95
# 99
# 100


def print_scores(name, *args):
    print(f'Student name: {name}')
    print(*(i for i in sorted(args)), sep='\n')

print_scores("Jud", 100, 95, 88, 92, 99)
