# Напишите функцию from_date_to_timestamp, которая принимает строку даты в формате
#
# День ПолноеНазваниеМесяца Год Часы:Минуты:Секунды
# Пример: 01 September 2012 12:32:21
# и возвращает временную метку переданной даты
#
# Нужно преобразовать дату и время по времени UTC

from datetime import datetime, timezone, timedelta


def from_date_to_timestamp(date_string: str) -> float:
    dt = datetime.strptime(date_string, '%d %B %Y %H:%M:%S').replace(tzinfo=timezone.utc)
    return dt.timestamp()


assert from_date_to_timestamp("01 September 2012 12:32:21") == 1346502741.0
assert from_date_to_timestamp("19 August 2018 00:50:00") == 1534639800.0
assert from_date_to_timestamp("28 February 2012 16:00:00") == 1330444800.0
