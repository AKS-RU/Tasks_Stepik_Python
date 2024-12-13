# Аудит
# День аудита в компании "Рога и копыта" приходится на каждый первый понедельник месяца.
# Сотрудники этого предприятия просят вас написать программу, которая выведет на экран информацию
# для каждого отдельного месяца с датой аудита за указанный год.

# Программа должна запрашивать год и выводить в хронологическом порядке краткое название месяца и
# через пробел дату аудита

import calendar
from collections import defaultdict


def monday_audit(year_in):
    result = defaultdict(int)

    for index, month in enumerate(calendar.month_name[1:]):
        for i in calendar.monthcalendar(year_in, index+1):
            if i[0]:
                result[month[:3]] = f'{i[0]}/{index+1}/{year_in}'
                break

    print(*(f'{k}: {v}'for k, v in result.items()), sep='\n')


monday_audit(int(input()))
