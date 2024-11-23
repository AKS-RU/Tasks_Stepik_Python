# Перед вами стоит задача написать  функцию count_goals, которая умеет считать итоговую статистику
# по забитым голам для каждого игрока за несколько сезонов. Ваша задача при помощи объекта Counter
# подсчитать итоговое количество голов, которое забил каждый футболист, находящийся в этом списке.
#
# Формат статистики представляет собой словарь: ключ - это номер года, а значением является словарь,
# где хранятся пары "Игрок" - "Количество Забитых Мячей"
#
# statistics = {
#     2010: {'Cristiano Ronaldo': 45, 'David Villa': 38},
#     2011: {'Cristiano Ronaldo': 43, 'Lionel Messi': 73}
# }
# Ваша задача написать только определение функции count_goals


from collections import Counter


def count_goals(stats: dict) -> Counter:
    result = Counter()
    for key, value in stats.items():
        for k, v in value.items():
            result[k] += v
    return result


# Ниже располагается код для проверки работы функции count_goals

statistics = {
    2010: {'Cristiano Ronaldo': 45, 'David Villa': 38, 'Diego Forlán': 35,
           'Lionel Messi': 52, "Samuel Eto'o": 34},
    2011: {'Cristiano Ronaldo': 60, 'Lionel Messi': 73,
           'Radamel Falcao': 34, 'Robin van Persie': 37,
           'Zlatan Ibrahimović': 35},
    2012: {'Cristiano Ronaldo': 63, 'Edinson Cavani': 29,
           'Lionel Messi': 91, 'Radamel Falcao': 34,
           'Robin van Persie': 30},
    2013: {'Cristiano Ronaldo': 69, 'Diego Costa': 27,
           'Lionel Messi': 45, 'Radamel Falcao': 31,
           'Zlatan Ibrahimović': 41},
    2014: {'Cristiano Ronaldo': 56, 'Diego Costa': 36,
           'Karim Benzema': 24, 'Lionel Messi': 58,
           'Sergio Agüero': 28},
    2015: {'Cristiano Ronaldo': 51, 'Lionel Messi': 52,
           'Luis Suárez': 49, 'Neymar': 39,
           'Robert Lewandowski': 37},
    2016: {'Cristiano Ronaldo': 55, 'Edinson Cavani': 41,
           'Lionel Messi': 59, 'Luis Suárez': 59,
           'Robert Lewandowski': 43},
    2017: {'Cristiano Ronaldo': 53, 'Edinson Cavani': 53,
           'Harry Kane': 56, 'Lionel Messi': 54,
           'Robert Lewandowski': 53},
    2018: {'Harry Kane': 41, 'Kylian Mbappé': 47,
           'Lionel Messi': 51, 'Mohamed Salah': 44,
           'Robert Lewandowski': 41},
    2019: {'Kylian Mbappé': 41, 'Lionel Messi': 45,
           'Raheem Sterling': 38, 'Robert Lewandowski': 36,
           'Sergio Agüero': 31},
    2020: {'Cristiano Ronaldo': 44, 'Erling Haaland': 27,
           'Lionel Messi': 31, 'Robert Lewandowski': 55,
           'Romelu Lukaku': 28},
    2021: {'Cristiano Ronaldo': 34, 'Harry Kane': 26,
           'Lionel Messi': 38, 'Mohamed Salah': 28,
           'Robert Lewandowski': 37},
    2022: {'Cristiano Ronaldo': 20, 'Kylian Mbappé': 21,
           'Lionel Messi': 23, 'Robert Lewandowski': 28,
           'Romelu Lukaku': 19}}

result = count_goals(statistics)

assert result['Lionel Messi'] == 672
assert result['Cristiano Ronaldo'] == 550
assert result['Kylian Mbappé'] == 109
assert result['Luis Suárez'] == 108
assert result['Karim Benzema'] == 24
assert result['Diego Forlán'] == 35
assert result['Raheem Sterling'] == 38
assert result['Mohamed Salah'] == 72
assert result['Robin van Persie'] == 67
assert result['Neymar'] == 39
assert len(result) == 21

assert result == Counter(
    {'Lionel Messi': 672, 'Cristiano Ronaldo': 550, 'Robert Lewandowski': 330,
     'Edinson Cavani': 123, 'Harry Kane': 123, 'Kylian Mbappé': 109, 'Luis Suárez': 108,
     'Radamel Falcao': 99, 'Zlatan Ibrahimović': 76, 'Mohamed Salah': 72, 'Robin van Persie': 67,
     'Diego Costa': 63, 'Sergio Agüero': 59, 'Romelu Lukaku': 47, 'Neymar': 39,
     'David Villa': 38, 'Raheem Sterling': 38, 'Diego Forlán': 35, "Samuel Eto'o": 34,
     'Erling Haaland': 27, 'Karim Benzema': 24})
