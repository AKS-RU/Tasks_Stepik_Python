# Теперь перед вами стоит задача написать  функцию count_min_goals, которая умеет среди всей
# итоговой статистики находить для каждого игрока минимальное количество голов за один год,
# которое забил каждый игрок
#
# Формат статистики не изменился
#
# statistics = {
#     2010: {'Cristiano Ronaldo': 45, 'David Villa': 38},
#     2011: {'Cristiano Ronaldo': 43, 'Lionel Messi': 73}
# }
# Ваша задача написать только определение функции count_min_goals


from collections import Counter


def count_min_goals(stats: dict) -> Counter:
    result = Counter()
    for key, value in stats.items():
        for k, v in value.items():
            if result[k] > v or result[k] == 0:
                result[k] = v
    return result


statistics = {
    2020: {'Messi': 20, 'Neymar': 30, 'Ronaldo': 25},
    2021: {'Neymar': 23, 'Griezmann': 47, 'Messi': 29},
    2022: {'Griezmann': 35, 'Messi': 34, 'Ronaldo': 34}
}
assert count_min_goals(statistics) == Counter(
    {'Griezmann': 35, 'Ronaldo': 25, 'Neymar': 23, 'Messi': 20})

statistics = {
    2015: {'Benzema': 32, 'Griezmann': 43, 'Messi': 52, 'Neymar': 39, 'Ronaldo': 51},
    2016: {'Benzema': 26, 'Griezmann': 37, 'Messi': 36, 'Neymar': 35, 'Ronaldo': 42},
    2017: {'Benzema': 27, 'Griezmann': 51, 'Messi': 42, 'Neymar': 49, 'Ronaldo': 30},
    2018: {'Benzema': 32, 'Griezmann': 41, 'Messi': 45, 'Neymar': 30, 'Ronaldo': 43},
    2019: {'Benzema': 29, 'Griezmann': 39, 'Messi': 51, 'Neymar': 31, 'Ronaldo': 48},
    2020: {'Benzema': 33, 'Griezmann': 41, 'Messi': 36, 'Neymar': 30, 'Ronaldo': 25},
    2021: {'Benzema': 54, 'Griezmann': 47, 'Messi': 29, 'Neymar': 36, 'Ronaldo': 21},
    2022: {'Benzema': 29, 'Griezmann': 35, 'Messi': 34, 'Neymar': 36, 'Ronaldo': 34}
}
assert count_min_goals(statistics) == Counter(
    {'Griezmann': 35, 'Neymar': 30, 'Messi': 29, 'Benzema': 26, 'Ronaldo': 21})

print('OK')
