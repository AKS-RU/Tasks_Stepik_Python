# Напишите функцию convert_str_to_datetime, которая принимает строку определенного формата и
# преобразовывает ее в дату и время.
#
# Формат строки
#
# КраткоеНазваниеМесяц День Год Часы(12 часовой формат):Минуты ПоловинаДня(AM или PM)
#
# Пример: Jul 1 2014 2:43 PM
#
# Гарантируется, что передаются всегда валидные значения


from datetime import datetime


def convert_str_to_datetime(date_string) -> datetime:
    return datetime.strptime(date_string, '%b %d %Y %I:%M %p')


assert convert_str_to_datetime('Jul 1 2014 2:43 PM') == datetime(2014, 7, 1, 14, 43)
assert convert_str_to_datetime('Aug 18 2005 6:00 AM') == datetime(2005, 8, 18, 6, 0)
assert convert_str_to_datetime('Dec 31 2020 11:59 PM') == datetime(2020, 12, 31, 23, 59)
assert convert_str_to_datetime('Feb 29 2012 09:29 PM') == datetime(2012, 2, 29, 21, 29)

print('OK')
