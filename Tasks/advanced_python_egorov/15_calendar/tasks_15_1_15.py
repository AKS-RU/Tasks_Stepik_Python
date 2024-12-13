# По заданному году необходимо определить для каждого месяца сколько в нем было вторников.

# В качестве ответа необходимо по хронологическому порядку вывести все месяца в отдельных строках и
# напротив каждого месяца через пробел указать найденное количество вторников
import calendar
from collections import defaultdict


year_in = int(input())
result = defaultdict(int)

for index, month in enumerate(calendar.month_name[1:]):
    for lst_month in calendar.monthcalendar(year_in, index+1):
        if lst_month[1]:
            result[month] += 1

print(*(f'{k}: {v}' for k, v in result.items()), sep='\n')
