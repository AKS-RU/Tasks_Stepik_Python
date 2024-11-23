# Напишите функцию get_day_of_year, которая принимает объект даты dt и возвращает порядковый
# номер данной даты в году
#
# Например, 1 января любого года это первый день в году, 2 января - второй день в году,
# 1 февраля - 32й день в году и т.д.


from datetime import date


def get_day_of_year(dt: date) -> int:
    return int(dt.strftime('%j'))


assert get_day_of_year(date(2023, 1, 3)) == 3
assert get_day_of_year(date(2023, 1, 8)) == 8
assert get_day_of_year(date(2023, 1, 31)) == 31
assert get_day_of_year(date(2023, 2, 28)) == 59
assert get_day_of_year(date(2024, 2, 28)) == 59
assert get_day_of_year(date(2023, 3, 1)) == 60
assert get_day_of_year(date(2020, 3, 1)) == 61
assert get_day_of_year(date(2023, 6, 15)) == 166
assert get_day_of_year(date(2000, 6, 15)) == 167
assert get_day_of_year(date(2023, 12, 31)) == 365
assert get_day_of_year(date(2004, 12, 31)) == 366
print('Good')
