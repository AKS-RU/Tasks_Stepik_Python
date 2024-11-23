# Написать функцию get_dates_until_end_of_month(date), которая принимает дату в качестве аргумента
# и возвращает список дат, начиная с указанной даты и до конца того же месяца.


from datetime import date


def get_dates_until_end_of_month(dt: date) -> list[date]:
    result = []
    for i in range(dt.day, 32):
        try:
            result.append(dt.replace(day=i))
        except:
            break
    return result


assert get_dates_until_end_of_month(date(2023, 12, 28)) == [
    date(2023, 12, 28),
    date(2023, 12, 29),
    date(2023, 12, 30),
    date(2023, 12, 31)
]
assert get_dates_until_end_of_month(date(2024, 2, 23)) == [
    date(2024, 2, 23),
    date(2024, 2, 24),
    date(2024, 2, 25),
    date(2024, 2, 26),
    date(2024, 2, 27),
    date(2024, 2, 28),
    date(2024, 2, 29)
]

assert get_dates_until_end_of_month(date(2023, 2, 25)) == [
    date(2023, 2, 25),
    date(2023, 2, 26),
    date(2023, 2, 27),
    date(2023, 2, 28),
]

assert get_dates_until_end_of_month(date(2022, 5, 10)) == [
    date(2022, 5, 10), date(2022, 5, 11), date(2022, 5, 12),
    date(2022, 5, 13), date(2022, 5, 14), date(2022, 5, 15),
    date(2022, 5, 16), date(2022, 5, 17), date(2022, 5, 18),
    date(2022, 5, 19), date(2022, 5, 20), date(2022, 5, 21),
    date(2022, 5, 22), date(2022, 5, 23), date(2022, 5, 24),
    date(2022, 5, 25), date(2022, 5, 26), date(2022, 5, 27),
    date(2022, 5, 28), date(2022, 5, 29), date(2022, 5, 30),
    date(2022, 5, 31)
]
print('Good')
