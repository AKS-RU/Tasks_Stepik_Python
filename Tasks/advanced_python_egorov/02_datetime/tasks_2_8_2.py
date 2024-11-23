# Напишите функцию count_work_days, которая принимает две даты и находит количество рабочих
# дней между ними включительно.
#
# Рабочим днем считаются все дни недели кроме субботы и воскресения, наличие праздничных дней
# не рассматривается в данной задаче
#
# Не гарантируется, что первая входная дата будет меньше второй.


from datetime import date, timedelta


def count_work_days(dt_1: date, dt_2: date) -> int:
    if dt_1 > dt_2:
        dt_1, dt_2 = dt_2, dt_1

    diff = (dt_2 - dt_1).days

    return sum((dt_1 + timedelta(days=i)).isoweekday() not in (6, 7) for i in range(diff + 1))


start = date(2024, 3, 11)
end = date(2024, 3, 15)
print(count_work_days(start, end))
