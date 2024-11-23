# Создайте множество, содержащее все возможные значения времени от 00:00:00 до 23:59:45
# с интервалом в 15 секунд.
#
# Сохраните его в переменную times, выводить на экран ничего не нужно


from datetime import time

end_time = time(23, 59, 45)


def hour_second(dates):
    sec = dates.hour * 3600 + dates.minute * 60 + dates.second
    return sec


def second_hour(sec):
    return time(hour=sec // 3600, minute=(sec % 3600) // 60, second=sec % 60)


times = set(
    second_hour(i) for i in range(hour_second(end_time) + 1) if second_hour(i).second % 15 == 0)

print(times)
