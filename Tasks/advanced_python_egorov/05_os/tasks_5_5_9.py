# Менеджеры по продажам пришли с «хотелками», которые усовершенствуют предыдущую программу.
# Они просят дополнительно создать в каждом каталоге месяца отдельную папку для каждого дня
# этого месяца. Имя каталога должно содержать порядковый номер дня месяца из двух цифр, затем
# нижнее подчеркивание, после короткое английское название текущего месяца, и через еще одно
# нижнее подчеркивание две последние цифры текущего года.

from datetime import datetime, timedelta
import os
import calendar


year_lst = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025,]
month_lst = list(calendar.month_name[1:])


for i in year_lst:
    i = str(i)
    year_dir = f'sales_{i}'
    if not os.path.isdir(year_dir):
        os.mkdir(year_dir)
    for n, m in enumerate(month_lst):
        mont_dir = os.path.join(year_dir, f'{m}_{i[-2:]}')
        if not os.path.isdir(mont_dir):
            os.mkdir(mont_dir)
        for d in range(1, calendar.monthrange(int(i), n+1)[1]+1):
            tmp_date = datetime(year=int(i), month=n+1, day=d)
            day_dir = os.path.join(mont_dir, tmp_date.strftime('%d_%b_%y'))
            if not os.path.isdir(day_dir):
                os.mkdir(day_dir)
