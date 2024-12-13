# Напишите функцию count_word_days_in_month, которая находит сколько рабочих дней будет или
# было в определенном месяца.

# Функция count_word_days_in_month имеет два обязательный параметра: год и месяц.

# Рабочим считаются все дни недели кроме субботы и воскресения, наличие праздничных дней не
# рассматривается в данной задаче

import calendar


def count_word_days_in_month(year_in, month_in):
    month_iter = calendar.Calendar()
    result = sum(1 for i in month_iter.itermonthdays4(
        year_in, month_in) if i[3] < 5 and i[1] == month_in)
    return result


print(count_word_days_in_month(2024, 4))
