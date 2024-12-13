# Сколько еще работать? - 3
# Напишите функцию count_word_days_in_year, которая находит сколько рабочих дней будет или было
# в определенном году с учетом выходных дней.

# Функция count_word_days_in_year принимает обязательно значение года и необязательно список
# праздничных дат (объекты date), считает количество рабочих дней и возвращает найденный результат.

# Рабочим считаются все дни недели кроме субботы и воскресения и не попадающие на праздничные даты.
from datetime import date
import calendar


def count_word_days_in_year(years_in, lst=[]):
    years_iter = calendar.Calendar()
    result = 0

    result -= sum(1 for i in lst if i.weekday() <
                  5)  # Вычитаем субботы и воскресенья которые \
    # указаны как праздничные дни в переданном \
    # списке lst
    for m in range(1, 13):
        for d in years_iter.itermonthdays4(years_in, m):
            if d[3] < 5 and d[1] == m:
                result += 1
    return result


holidays = [
    date(2023, 1, 1),
    date(2023, 1, 2),
    date(2023, 1, 3),
    date(2023, 1, 4),
    date(2023, 1, 5),
    date(2023, 1, 6),
    date(2023, 1, 7),
    date(2023, 2, 23),
    date(2023, 3, 8),
    date(2023, 12, 31),
]
workdays = count_word_days_in_year(2023, holidays)
print(workdays)
