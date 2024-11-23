# Написать функцию-генератор all_sundays, которая принимает в качестве аргумента год (целое число)
# и генерирует все даты, являющиеся воскресеньями в этом году.


from typing import Generator
from datetime import date, timedelta


def all_sundays(year: int) -> Generator[int, None, None]:
    start_date = date(year, 1, 1)
    for i in range(367):
        tmp_date = start_date + timedelta(days=i)
        if tmp_date.isoweekday() == 7 and tmp_date.year == year:
            yield tmp_date


for sunday in all_sundays(2023):
    print(sunday)

assert list(all_sundays(2021)) == [date(2021, 1, 3), date(2021, 1, 10), date(2021, 1, 17),
                                   date(2021, 1, 24), date(2021, 1, 31), date(2021, 2, 7),
                                   date(2021, 2, 14), date(2021, 2, 21), date(2021, 2, 28),
                                   date(2021, 3, 7), date(2021, 3, 14), date(2021, 3, 21),
                                   date(2021, 3, 28), date(2021, 4, 4), date(2021, 4, 11),
                                   date(2021, 4, 18), date(2021, 4, 25), date(2021, 5, 2),
                                   date(2021, 5, 9), date(2021, 5, 16), date(2021, 5, 23),
                                   date(2021, 5, 30), date(2021, 6, 6), date(2021, 6, 13),
                                   date(2021, 6, 20), date(2021, 6, 27), date(2021, 7, 4),
                                   date(2021, 7, 11), date(2021, 7, 18), date(2021, 7, 25),
                                   date(2021, 8, 1), date(2021, 8, 8), date(2021, 8, 15),
                                   date(2021, 8, 22), date(2021, 8, 29), date(2021, 9, 5),
                                   date(2021, 9, 12), date(2021, 9, 19), date(2021, 9, 26),
                                   date(2021, 10, 3), date(2021, 10, 10), date(2021, 10, 17),
                                   date(2021, 10, 24), date(2021, 10, 31), date(2021, 11, 7),
                                   date(2021, 11, 14), date(2021, 11, 21), date(2021, 11, 28),
                                   date(2021, 12, 5), date(2021, 12, 12), date(2021, 12, 19),
                                   date(2021, 12, 26)]
assert list(all_sundays(2022)) == [date(2022, 1, 2), date(2022, 1, 9), date(2022, 1, 16),
                                   date(2022, 1, 23), date(2022, 1, 30), date(2022, 2, 6),
                                   date(2022, 2, 13), date(2022, 2, 20), date(2022, 2, 27),
                                   date(2022, 3, 6), date(2022, 3, 13), date(2022, 3, 20),
                                   date(2022, 3, 27), date(2022, 4, 3), date(2022, 4, 10),
                                   date(2022, 4, 17), date(2022, 4, 24), date(2022, 5, 1),
                                   date(2022, 5, 8), date(2022, 5, 15), date(2022, 5, 22),
                                   date(2022, 5, 29), date(2022, 6, 5), date(2022, 6, 12),
                                   date(2022, 6, 19), date(2022, 6, 26), date(2022, 7, 3),
                                   date(2022, 7, 10), date(2022, 7, 17), date(2022, 7, 24),
                                   date(2022, 7, 31), date(2022, 8, 7), date(2022, 8, 14),
                                   date(2022, 8, 21), date(2022, 8, 28), date(2022, 9, 4),
                                   date(2022, 9, 11), date(2022, 9, 18), date(2022, 9, 25),
                                   date(2022, 10, 2), date(2022, 10, 9), date(2022, 10, 16),
                                   date(2022, 10, 23), date(2022, 10, 30), date(2022, 11, 6),
                                   date(2022, 11, 13), date(2022, 11, 20), date(2022, 11, 27),
                                   date(2022, 12, 4), date(2022, 12, 11), date(2022, 12, 18),
                                   date(2022, 12, 25)]
