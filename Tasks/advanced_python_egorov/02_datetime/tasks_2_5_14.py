# Создайте функцию get_format_date, которая принимает объект datetime и возвращает строку
# форматирования даты в удобочитаемом виде следующего формата
#
# Today is <Название_дня_недели>, <День> <Полное_название_месяца> <Год>


from datetime import datetime


def get_format_date(dt: datetime) -> str:
    return dt.strftime('Today is %A, %d %B %Y')


dt_1 = datetime(2023, 9, 1, 18, 45, 30)
assert get_format_date(dt_1) == 'Today is Friday, 01 September 2023'

dt_2 = datetime(2018, 2, 10, 9, 4, 59)
assert get_format_date(dt_2) == 'Today is Saturday, 10 February 2018'

dt_3 = datetime(2000, 8, 15, 10, 30, 0)
assert get_format_date(dt_3) == 'Today is Tuesday, 15 August 2000'

print('Good')
