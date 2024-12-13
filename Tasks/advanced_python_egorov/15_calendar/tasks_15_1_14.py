# Распечатайте календарь для указанного месяца и года так, чтобы отсчет дней начинался с
# воскресенья

import calendar


calendar.setfirstweekday(calendar.SUNDAY)

calendar.prmonth(int(input()), int(input()))
