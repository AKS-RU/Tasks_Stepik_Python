# Напишите функцию find_number_week_of_week, которая принимает объект даты dt и возвращает номер
# недели этой даты в формате ISO-календаря.


from datetime import date


def find_number_week_of_week(dt: date) -> int:
    return dt.isocalendar().week


assert find_number_week_of_week(date(2023, 1, 3)) == 1
assert find_number_week_of_week(date(2023, 1, 8)) == 1
assert find_number_week_of_week(date(2023, 1, 9)) == 2
assert find_number_week_of_week(date(2023, 1, 31)) == 5
assert find_number_week_of_week(date(2023, 4, 10)) == 15
assert find_number_week_of_week(date(2023, 12, 30)) == 52
print('Good')
