# Программа получает на вход год и номер месяца и должна вывести на экран количество
# дней в указанном месяце

import calendar


print((calendar.monthrange(int(input()), int(input()))[1]))
