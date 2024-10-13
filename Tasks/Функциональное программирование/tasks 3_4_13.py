# Исправьте функции так, чтобы добавление одной оценки студенту не влияло на оценки других учеников
#
# Sample Input 1:
#
# ivan = create_student('Ivan', 15)
# anatoliy = create_student('Anatoliy', 16)
#
# add_mark(ivan, 5)
# add_mark(ivan, 5)
# add_mark(anatoliy, 3)
# add_mark(anatoliy, 4)
# print(ivan['marks'])
# print(anatoliy['marks'])
# Sample Output 1:
#
# [5, 5]
# [3, 4]
# Sample Input 2:
#
# ivan = create_student('Ivan', 15, [3, 4, 5])
# anatoliy = create_student('Anatoliy', 16, [2])
# add_mark(ivan, 4)
# add_mark(ivan, 5)
# add_mark(anatoliy, 4)
# add_mark(anatoliy, 5)
# add_mark(anatoliy, 2)
# print(ivan['marks'])
# print(anatoliy['marks'])
# Sample Output 2:
#
# [3, 4, 5, 4, 5]
# [2, 4, 5, 2]


def create_student(name, age, marks=None):
    if marks is None:
        marks = []
    return {
        'name': name,
        'age': age,
        'marks': marks  # оценки
    }


def add_mark(student, mark):
    student['marks'].append(mark)