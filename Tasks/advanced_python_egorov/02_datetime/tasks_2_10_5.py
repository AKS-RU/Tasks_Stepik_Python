# Напишите функцию from_timestamp_to_readable_date, которая принимает временную метку Unix и
# возвращает строку в удобочитаемом формате
#
# День.Месяц.Год Часы:Минуты:Секунды
# Нужно преобразовать дату и время по времени UTC

from datetime import datetime, timedelta, timezone


def from_timestamp_to_readable_date(unix_timestamp: int) -> str:
    utc = timedelta(hours=0)
    tz = timezone(utc)
    dt = datetime.fromtimestamp(unix_timestamp, tz).strftime('%d.%m.%Y %H:%M:%S')
    return dt


assert from_timestamp_to_readable_date(0) == '01.01.1970 00:00:00'
assert from_timestamp_to_readable_date(86400) == '02.01.1970 00:00:00'
assert from_timestamp_to_readable_date(312313922) == '24.11.1979 17:52:02'
assert from_timestamp_to_readable_date(4232313922) == '13.02.2104 02:45:22'
