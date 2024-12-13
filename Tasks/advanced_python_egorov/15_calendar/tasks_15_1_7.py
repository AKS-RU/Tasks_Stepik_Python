# Программа получает на вход год и номер месяца и должна вывести на экран календарь за
# указанный месяц

import calendar

year_in = int(input())
month_in = int(input())

calendar.prmonth(year_in, month_in)
