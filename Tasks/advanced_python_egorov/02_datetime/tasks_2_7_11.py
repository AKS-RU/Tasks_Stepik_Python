# апишите  функцию get_diff_dates_in_day, которая рассчитывает количества полных дней между
# двумя объектами datetime.
#
# Для выполнения задания необходимо написать только определение функции get_diff_dates_in_day


from datetime import datetime


def get_diff_dates_in_days(dt1: datetime, dt2: datetime) -> int:
    return abs(dt1 - dt2).days


# Проверки для функции get_diff_dates_in_days

date1 = datetime(2023, 1, 1, 12, 0, 0)  # 1 января 2023 года, 12:00:00
date2 = datetime(2023, 1, 5, 18, 30, 0)  # 5 января 2023 года, 18:30:00
print(get_diff_dates_in_days(date1, date2))
assert get_diff_dates_in_days(date1, date2) == 4

date3 = datetime(2023, 1, 3, 18, 30, 0)  # 3 января 2023 года, 18:30:00
date4 = datetime(2023, 1, 1, 12, 0, 0)  # 1 января 2023 года, 12:00:00
assert get_diff_dates_in_days(date3, date4) == 2

date5 = datetime(2023, 2, 1, 12, 0, 0)  # 1 февраля 2023 года, 12:00:00
date6 = datetime(2023, 2, 2, 11, 59, 59)  # 2 февраля 2023 года, 11:59:59
assert get_diff_dates_in_days(date5, date6) == 0

date7 = datetime(2023, 3, 1, 8, 0, 0)  # 1 марта 2023 года, 08:00:00
date8 = datetime(2023, 2, 1, 8, 0, 0)  # 1 февраля 2023 года, 08:00:00
assert get_diff_dates_in_days(date7, date8) == 28

date9 = datetime(2022, 12, 31, 23, 59, 59)  # 31 декабря 2022 года, 23:59:59
date10 = datetime(2023, 1, 1, 0, 0, 0)  # 1 января 2023 года, 00:00:00
assert get_diff_dates_in_days(date9, date10) == 0

print('OK')
