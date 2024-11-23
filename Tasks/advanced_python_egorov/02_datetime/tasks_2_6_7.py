# Поработаем с функцией json_serial из последнего примера
#
# def json_serial(obj):
#
#     if isinstance(obj, (datetime, date, time)):
#         return obj.isoformat()
#     raise TypeError("Type %s not serializable" % type(obj))
# Перепишите ее так, чтобы тип date сохранялся в формате dd.mm.yyyy, а для типа datetime
# использовался формат:
#
# "Date registry: <номер дня> <Название месяца>, <Год> <Часы>:<Минута>"
# К примеру, если взять значение 19 сентября 2020, 14:00, то оно представилось бы в таком виде
#
# "Date registry: 19 September, 2020 14:00"
# Формат времени менять не нужно
#
# В задании нужно изменить только содержимое функции json_serial


import json
from datetime import datetime, time, date

dict_with_times = {
    'date': date(2023, 9, 2),
    'datetime': datetime(2023, 9, 2, 15, 30, 0),
    'time': time(15, 30, 19),
}


def json_serial(obj):
    if isinstance(obj, time):
        return obj.isoformat()
    elif isinstance(obj, datetime):
        return obj.strftime('Date registry: %d %B, %Y %H:%M')
    elif isinstance(obj, date):
        return obj.strftime('%d.%m.%Y')

    raise TypeError("Type %s not serializable" % type(obj))


json_str = json.dumps(dict_with_times, default=json_serial)
print(json_str)
assert json_str == '{"date": "02.09.2023", "datetime": "Date registry: 02 September, 2023 15:30", "time": "15:30:19"}'

print('Good')

print(issubclass(datetime, date))
