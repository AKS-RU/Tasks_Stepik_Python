# Лучшая оценка - 2
#  Усовершенствуйте функцию get_info_marks из предыдущего урока так, чтобы она возвращала словарь, в котором для
# каждого студента формируется словарь, хранящий информацию как о лучшей оценке студента(ключ «best»), так
# и худшей (ключ «worst»)
#
# Параметры функции остаются неизменными.
#
# Sample Input 1:
#
# math = [90, 76, 94]
# history = [78, 79, 90]
# students = ["Marie", "Michael", "Marge"]
# print(get_info_marks(students, math, history))
# Sample Output 1:
#
# {'Marie': {'best': 90, 'worst': 78}, 'Michael': {'best': 79, 'worst': 76}, 'Marge': {'best': 94, 'worst': 90}}
# Sample Input 2:
#
# math = [90, 76, 94]
# history = [78, 79, 90]
# geography = [95, 80, 92]
# students = ["Marie", "Michael", "Marge"]
# print(get_info_marks(students, math, geography, history))
# Sample Output 2:
#
# {'Marie': {'best': 95, 'worst': 78}, 'Michael': {'best': 80, 'worst': 76}, 'Marge': {'best': 94, 'worst': 90}}
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
# {'Marie': {'best': 95, 'worst': 78}, 'Michael': {'best': 98, 'worst': 76}, 'Marge': {'best': 100, 'worst': 90}}


def get_info_marks(students: str, *args):
    return {i[0]: {'best': max(list(i[1:])), 'worst': min(list(i[1:]))} for i in list(zip(students, *args))}



math = [90, 76, 94]
history = [78, 79, 90]
geography = [95, 80, 92]
music = [93, 98, 100]
students = ["Marie", "Michael", "Marge"]
print(get_info_marks(students, math, geography, history, music))