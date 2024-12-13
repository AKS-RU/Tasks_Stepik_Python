# Сколько еще работать? - 2
# Напишите функцию count_word_days_in_year, которая находит сколько рабочих дней будет или было
# в определенном году.

# Функция count_word_days_in_year принимает значение только года и возвращает найденное количество
# рабочих дней.

# Рабочим считаются все дни недели кроме субботы и воскресения, наличие праздничных дней не
# рассматривается в данной задаче

import calendar


def count_word_days_in_year(year_in):
    year_iter = calendar.Calendar()
    result = 0
    for i in range(1, 13):
        for d in year_iter.itermonthdays4(year_in, i):
            if d[3] < 5 and d[1] == i:
                result += 1
    return result


print(count_word_days_in_year(2021))
