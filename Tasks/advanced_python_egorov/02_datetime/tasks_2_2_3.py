# Напишите функцию count_dates_within_interval, которая принимает три аргумента:
#
# start_date - начало интервала
#
# end_date - конец интервала
#
# dates — список дат (тип date)
# Функция должна вернуть количество дат, попадающих в заданный промежуток времени,
# включая границы интервала.
#
# Не всегда дата начала меньше, чем дата конца интервала. Смотрите тесты


from datetime import date


def count_dates_within_interval(start_date: date,
                                end_date: date,
                                dates: list[date]) -> int:
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    return sum(1 for i in dates if start_date <= i <= end_date)


test_dates = [
    date(2021, 9, 1),
    date(2021, 9, 2),
    date(2021, 9, 3),
    date(2021, 9, 4),
    date(2021, 9, 5),
    date(2021, 9, 4),
    date(2021, 9, 3),
]
assert count_dates_within_interval(
    date(2021, 9, 1), date(2021, 9, 2), test_dates) == 2

assert count_dates_within_interval(
    date(2021, 9, 1), date(2021, 9, 3), test_dates) == 4

assert count_dates_within_interval(
    date(2021, 9, 3), date(2021, 9, 1), test_dates) == 4

assert count_dates_within_interval(
    date(2021, 9, 10), date(2021, 9, 6), test_dates) == 0

assert count_dates_within_interval(
    date(2021, 9, 10), date(2021, 9, 5), test_dates) == 1

assert count_dates_within_interval(
    date(2021, 8, 10), date(2021, 8, 20), test_dates) == 0

assert count_dates_within_interval(
    date(2021, 9, 20), date(2021, 8, 10), test_dates) == 7

print('Good')
