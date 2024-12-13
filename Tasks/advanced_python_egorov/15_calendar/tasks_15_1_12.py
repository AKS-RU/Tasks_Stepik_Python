# Напишите функцию get_forward_months, которая принимает номер месяца (число от 1 до 12) и
# возвращает список всех 12 кратких названий месяцев, начинающихся с текущего и следующих
# в хронологическом порядке.

# Если передано число, не являющееся номером месяца, необходимо вызвать исключение

# ValueError('Не правильный номер месяца')

import calendar


def get_forward_months(month_in):
    if not isinstance(month_in, int) or not (0 < month_in < 13):
        raise ValueError('Не правильный номер месяца')

    lst_month = list(calendar.month_abbr)[1:]
    lst_res = []

    for i in range(len(lst_month)):
        lst_res.append(lst_month[(i+month_in-1) % len(lst_month)])
    return lst_res


month = 4
print(get_forward_months(month))
