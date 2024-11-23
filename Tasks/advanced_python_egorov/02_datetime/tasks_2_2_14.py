# Напишите программу для подсчета общего числа понедельников, которым посчастливилось быть 1-м
# числом месяца в периоде с 2014 по 2022 год включительно.

from datetime import date

start_date = date(2014, 1, 1)
end_date = date(2022, 12, 31)
count = 0

for i in range(start_date.toordinal(), end_date.toordinal()):
    my_date = date.fromordinal(i)
    if my_date.day == 1 and my_date.isoweekday() == 1:
        count += 1

print(count)
