# Учет посещаемости сотрудников
# У вас есть набор данных о посещаемости сотрудников в течение дня, которые хранятся в списке
# кортежей. Каждый кортеж содержит время прихода или ухода сотрудника и его идентификатор
# вот в таком виде
#
# [
#     (time(9, 0), "ID1", "IN"),
#     (time(9, 5), "ID2", "IN"),
#     (time(9, 15), "ID3", "IN"),
#     (time(9, 30), "ID1", "OUT"),
#     (time(10, 0), "ID4", "IN")
# ]
# Данные уже расположены в хронологическом порядке
#
# Вам нужно создать функцию get_employee_attendance, которая принимает список посещаемости и
# возвращает словарь, где ключами будут объекты времени, а значениями - список сотрудников,
# которые были в офисе в это время.
#
# Тогда для значений выше результат будет следующий
#
# {
#     time(9, 0): ['ID1'],
#     time(9, 5): ['ID1', 'ID2'],
#     time(9, 15): ['ID1', 'ID2', 'ID3'],
#     time(9, 30): ['ID2', 'ID3'],
#     time(10, 0): ['ID2', 'ID3', 'ID4']
# }


from datetime import time


def get_employee_attendance(visit_data: list[tuple]) -> dict:
    result = {}
    lst = []
    for i in visit_data:
        if i[2] == 'IN':
            lst.append(i[1])
        else:
            if len(lst):
                lst.remove(i[1])
        result[i[0]] = lst.copy()

    return result


attendance = [
    (time(9, 0), "ID1", "IN"),
    (time(9, 5), "ID2", "IN"),
    (time(9, 15), "ID3", "IN"),
    (time(9, 30), "ID1", "OUT"),
    (time(10, 0), "ID4", "IN"),
    (time(10, 15), "ID2", "OUT"),
    (time(10, 30), "ID3", "OUT"),
    (time(10, 45), "ID4", "OUT"),
    (time(11, 0), "ID5", "IN"),
    (time(11, 15), "ID6", "IN"),
    (time(11, 30), "ID5", "OUT"),
    (time(11, 45), "ID6", "OUT")
]

assert get_employee_attendance(attendance) == {time(9, 0): ['ID1'],
                                               time(9, 5): ['ID1', 'ID2'],
                                               time(9, 15): ['ID1', 'ID2', 'ID3'],
                                               time(9, 30): ['ID2', 'ID3'],
                                               time(10, 0): ['ID2', 'ID3', 'ID4'],
                                               time(10, 15): ['ID3', 'ID4'],
                                               time(10, 30): ['ID4'],
                                               time(10, 45): [],
                                               time(11, 0): ['ID5'],
                                               time(11, 15): ['ID5', 'ID6'],
                                               time(11, 30): ['ID6'],
                                               time(11, 45): []}

attendance_2 = [
    (time(9, 0), "ID1", "IN"),
    (time(9, 5), "ID2", "IN"),
    (time(9, 15), "ID3", "IN"),
    (time(9, 30), "ID1", "OUT"),
    (time(10, 0), "ID4", "IN")
]

assert get_employee_attendance(attendance_2) == {time(9, 0): ['ID1'],
                                                 time(9, 5): ['ID1', 'ID2'],
                                                 time(9, 15): ['ID1', 'ID2', 'ID3'],
                                                 time(9, 30): ['ID2', 'ID3'],
                                                 time(10, 0): ['ID2', 'ID3', 'ID4']}

# только выход
attendance_3 = [
    (time(9, 30), "ID1", "OUT"),
    (time(10, 0), "ID2", "OUT"),
    (time(10, 30), "ID3", "OUT")
]

assert get_employee_attendance(attendance_3) == {time(9, 30): [],
                                                 time(10, 0): [],
                                                 time(10, 30): []}

# только вход
attendance_4 = [
    (time(9, 0), "ID1", "IN"),
    (time(9, 5), "ID2", "IN"),
    (time(9, 15), "ID3", "IN"),
    (time(10, 0), "ID4", "IN")
]

assert get_employee_attendance(attendance_4) == {time(9, 0): ["ID1"],
                                                 time(9, 5): ["ID1", "ID2"],
                                                 time(9, 15): ["ID1", "ID2", "ID3"],
                                                 time(10, 0): ["ID1", "ID2", "ID3", "ID4"]}

assert get_employee_attendance([]) == {}
print('Good')
