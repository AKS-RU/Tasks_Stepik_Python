# Напишите функцию is_third_tuesday, которая принимает дату в определенном формате (см примеры), и
# возвращает True, если текущий день является третьим вторником месяца. В противном случае - False

from datetime import datetime


def is_third_tuesday(dt_str: str) -> bool:
    dt = datetime.strptime(dt_str, '%b %d, %Y').date()
    count = 1
    if dt.isoweekday() == 2:
        for i in range(1, dt.day):
            if datetime(dt.year, dt.month, i).isoweekday() == 2:
                count += 1
    return count == 3


assert is_third_tuesday("Sep 19, 2023")
assert not is_third_tuesday("Sep 12, 2023")
assert is_third_tuesday("Jul 18, 2023")
assert not is_third_tuesday("Jul 11, 2023")
assert not is_third_tuesday('Jun 23, 2015')
assert is_third_tuesday('Jun 16, 2015')
assert is_third_tuesday('Jul 21, 2015')
assert is_third_tuesday("Oct 20, 2015")
assert is_third_tuesday("Nov 17, 2015")

print('Good')
