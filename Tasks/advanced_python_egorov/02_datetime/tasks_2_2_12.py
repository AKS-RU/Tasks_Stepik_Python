#                                         Пятница 13
# Перед вами имеется список all_dates_2023, который содержит в себе все даты 2023 года.
# Вам необходимо вывести на экран  только те даты, которые совпадают с названием задачи
# Выводить даты нужно в отдельных строках в порядке следования в списке all_dates_2023


from datetime import date

all_dates_2023 = [
    date(2023, 1, 1), date(2023, 1, 2), date(2023, 1, 3), date(2023, 1, 4),
    date(2023, 1, 5), date(2023, 1, 6), date(2023, 1, 7), date(2023, 1, 8),
    date(2023, 1, 9), date(2023, 1, 10), date(2023, 1, 11),
    date(2023, 1, 12), date(2023, 1, 13), date(2023, 1, 14),
    date(2023, 1, 15), date(2023, 1, 16), date(2023, 1, 17),
    date(2023, 1, 18), date(2023, 1, 19), date(2023, 1, 20),
    date(2023, 1, 21), date(2023, 1, 22), date(2023, 1, 23),
    date(2023, 1, 24), date(2023, 1, 25), date(2023, 1, 26),
    date(2023, 1, 27), date(2023, 1, 28), date(2023, 1, 29),
    date(2023, 1, 30), date(2023, 1, 31), date(2023, 2, 1),
    date(2023, 2, 2), date(2023, 2, 3), date(2023, 2, 4), date(2023, 2, 5),
    date(2023, 2, 6), date(2023, 2, 7), date(2023, 2, 8), date(2023, 2, 9),
    date(2023, 2, 10), date(2023, 2, 11), date(2023, 2, 12),
    date(2023, 2, 13), date(2023, 2, 14), date(2023, 2, 15),
    date(2023, 2, 16), date(2023, 2, 17), date(2023, 2, 18),
    date(2023, 2, 19), date(2023, 2, 20), date(2023, 2, 21),
    date(2023, 2, 22), date(2023, 2, 23), date(2023, 2, 24),
    date(2023, 2, 25), date(2023, 2, 26), date(2023, 2, 27),
    date(2023, 2, 28), date(2023, 3, 1), date(2023, 3, 2),
    date(2023, 3, 3), date(2023, 3, 4), date(2023, 3, 5), date(2023, 3, 6),
    date(2023, 3, 7), date(2023, 3, 8), date(2023, 3, 9),
    date(2023, 3, 10), date(2023, 3, 11), date(2023, 3, 12),
    date(2023, 3, 13), date(2023, 3, 14), date(2023, 3, 15),
    date(2023, 3, 16), date(2023, 3, 17), date(2023, 3, 18),
    date(2023, 3, 19), date(2023, 3, 20), date(2023, 3, 21),
    date(2023, 3, 22), date(2023, 3, 23), date(2023, 3, 24),
    date(2023, 3, 25), date(2023, 3, 26), date(2023, 3, 27),
    date(2023, 3, 28), date(2023, 3, 29), date(2023, 3, 30),
    date(2023, 3, 31), date(2023, 4, 1), date(2023, 4, 2),
    date(2023, 4, 3), date(2023, 4, 4), date(2023, 4, 5), date(2023, 4, 6),
    date(2023, 4, 7), date(2023, 4, 8), date(2023, 4, 9),
    date(2023, 4, 10), date(2023, 4, 11), date(2023, 4, 12),
    date(2023, 4, 13), date(2023, 4, 14), date(2023, 4, 15),
    date(2023, 4, 16), date(2023, 4, 17), date(2023, 4, 18),
    date(2023, 4, 19), date(2023, 4, 20), date(2023, 4, 21),
    date(2023, 4, 22), date(2023, 4, 23), date(2023, 4, 24),
    date(2023, 4, 25), date(2023, 4, 26), date(2023, 4, 27),
    date(2023, 4, 28), date(2023, 4, 29), date(2023, 4, 30),
    date(2023, 5, 1), date(2023, 5, 2), date(2023, 5, 3), date(2023, 5, 4),
    date(2023, 5, 5), date(2023, 5, 6), date(2023, 5, 7), date(2023, 5, 8),
    date(2023, 5, 9), date(2023, 5, 10), date(2023, 5, 11),
    date(2023, 5, 12), date(2023, 5, 13), date(2023, 5, 14),
    date(2023, 5, 15), date(2023, 5, 16), date(2023, 5, 17),
    date(2023, 5, 18), date(2023, 5, 19), date(2023, 5, 20),
    date(2023, 5, 21), date(2023, 5, 22), date(2023, 5, 23),
    date(2023, 5, 24), date(2023, 5, 25), date(2023, 5, 26),
    date(2023, 5, 27), date(2023, 5, 28), date(2023, 5, 29),
    date(2023, 5, 30), date(2023, 5, 31), date(2023, 6, 1),
    date(2023, 6, 2), date(2023, 6, 3), date(2023, 6, 4), date(2023, 6, 5),
    date(2023, 6, 6), date(2023, 6, 7), date(2023, 6, 8), date(2023, 6, 9),
    date(2023, 6, 10), date(2023, 6, 11), date(2023, 6, 12),
    date(2023, 6, 13), date(2023, 6, 14), date(2023, 6, 15),
    date(2023, 6, 16), date(2023, 6, 17), date(2023, 6, 18),
    date(2023, 6, 19), date(2023, 6, 20), date(2023, 6, 21),
    date(2023, 6, 22), date(2023, 6, 23), date(2023, 6, 24),
    date(2023, 6, 25), date(2023, 6, 26), date(2023, 6, 27),
    date(2023, 6, 28), date(2023, 6, 29), date(2023, 6, 30),
    date(2023, 7, 1), date(2023, 7, 2), date(2023, 7, 3), date(2023, 7, 4),
    date(2023, 7, 5), date(2023, 7, 6), date(2023, 7, 7), date(2023, 7, 8),
    date(2023, 7, 9), date(2023, 7, 10), date(2023, 7, 11),
    date(2023, 7, 12), date(2023, 7, 13), date(2023, 7, 14),
    date(2023, 7, 15), date(2023, 7, 16), date(2023, 7, 17),
    date(2023, 7, 18), date(2023, 7, 19), date(2023, 7, 20),
    date(2023, 7, 21), date(2023, 7, 22), date(2023, 7, 23),
    date(2023, 7, 24), date(2023, 7, 25), date(2023, 7, 26),
    date(2023, 7, 27), date(2023, 7, 28), date(2023, 7, 29),
    date(2023, 7, 30), date(2023, 7, 31), date(2023, 8, 1),
    date(2023, 8, 2), date(2023, 8, 3), date(2023, 8, 4), date(2023, 8, 5),
    date(2023, 8, 6), date(2023, 8, 7), date(2023, 8, 8), date(2023, 8, 9),
    date(2023, 8, 10), date(2023, 8, 11), date(2023, 8, 12),
    date(2023, 8, 13), date(2023, 8, 14), date(2023, 8, 15),
    date(2023, 8, 16), date(2023, 8, 17), date(2023, 8, 18),
    date(2023, 8, 19), date(2023, 8, 20), date(2023, 8, 21),
    date(2023, 8, 22), date(2023, 8, 23), date(2023, 8, 24),
    date(2023, 8, 25), date(2023, 8, 26), date(2023, 8, 27),
    date(2023, 8, 28), date(2023, 8, 29), date(2023, 8, 30),
    date(2023, 8, 31), date(2023, 9, 1), date(2023, 9, 2),
    date(2023, 9, 3), date(2023, 9, 4), date(2023, 9, 5), date(2023, 9, 6),
    date(2023, 9, 7), date(2023, 9, 8), date(2023, 9, 9),
    date(2023, 9, 10), date(2023, 9, 11), date(2023, 9, 12),
    date(2023, 9, 13), date(2023, 9, 14), date(2023, 9, 15),
    date(2023, 9, 16), date(2023, 9, 17), date(2023, 9, 18),
    date(2023, 9, 19), date(2023, 9, 20), date(2023, 9, 21),
    date(2023, 9, 22), date(2023, 9, 23), date(2023, 9, 24),
    date(2023, 9, 25), date(2023, 9, 26), date(2023, 9, 27),
    date(2023, 9, 28), date(2023, 9, 29), date(2023, 9, 30),
    date(2023, 10, 1), date(2023, 10, 2), date(2023, 10, 3),
    date(2023, 10, 4), date(2023, 10, 5), date(2023, 10, 6),
    date(2023, 10, 7), date(2023, 10, 8), date(2023, 10, 9),
    date(2023, 10, 10), date(2023, 10, 11), date(2023, 10, 12),
    date(2023, 10, 13), date(2023, 10, 14), date(2023, 10, 15),
    date(2023, 10, 16), date(2023, 10, 17), date(2023, 10, 18),
    date(2023, 10, 19), date(2023, 10, 20), date(2023, 10, 21),
    date(2023, 10, 22), date(2023, 10, 23), date(2023, 10, 24),
    date(2023, 10, 25), date(2023, 10, 26), date(2023, 10, 27),
    date(2023, 10, 28), date(2023, 10, 29), date(2023, 10, 30),
    date(2023, 10, 31), date(2023, 11, 1), date(2023, 11, 2),
    date(2023, 11, 3), date(2023, 11, 4), date(2023, 11, 5),
    date(2023, 11, 6), date(2023, 11, 7), date(2023, 11, 8),
    date(2023, 11, 9), date(2023, 11, 10), date(2023, 11, 11),
    date(2023, 11, 12), date(2023, 11, 13), date(2023, 11, 14),
    date(2023, 11, 15), date(2023, 11, 16), date(2023, 11, 17),
    date(2023, 11, 18), date(2023, 11, 19), date(2023, 11, 20),
    date(2023, 11, 21), date(2023, 11, 22), date(2023, 11, 23),
    date(2023, 11, 24), date(2023, 11, 25), date(2023, 11, 26),
    date(2023, 11, 27), date(2023, 11, 28), date(2023, 11, 29),
    date(2023, 11, 30), date(2023, 12, 1), date(2023, 12, 2),
    date(2023, 12, 3), date(2023, 12, 4), date(2023, 12, 5),
    date(2023, 12, 6), date(2023, 12, 7), date(2023, 12, 8),
    date(2023, 12, 9), date(2023, 12, 10), date(2023, 12, 11),
    date(2023, 12, 12), date(2023, 12, 13), date(2023, 12, 14),
    date(2023, 12, 15), date(2023, 12, 16), date(2023, 12, 17),
    date(2023, 12, 18), date(2023, 12, 19), date(2023, 12, 20),
    date(2023, 12, 21), date(2023, 12, 22), date(2023, 12, 23),
    date(2023, 12, 24), date(2023, 12, 25), date(2023, 12, 26),
    date(2023, 12, 27), date(2023, 12, 28), date(2023, 12, 29),
    date(2023, 12, 30), date(2023, 12, 31)
]

print(*(i for i in all_dates_2023 if i.day == 13 and i.isoweekday() == 5), sep='\n')