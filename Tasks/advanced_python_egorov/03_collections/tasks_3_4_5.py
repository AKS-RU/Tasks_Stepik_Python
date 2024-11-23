# В этом задании необходимо создать экземпляр  класса Counter на основании словаря players,
# в котором хранятся пары имя игрока-количество баллов. Но нужно взять только те пары,
# в которых количество баллов превышает 1700.
#
# Сохраните полученный экземпляр  класса Counter в переменную filter_players, выводить
# на экран ничего не нужно


from collections import Counter

players = {
    'Steven Brock': 2100, 'Jennifer Murphy': 1600, 'Christina Cox': 1900,
    'Julie Sherman': 2000, 'Shannon Day': 2000, 'Lisa Singh': 1600,
    'Mark Burns': 1900, 'Christian Woodward': 1500, 'Kenneth Burke': 1200,
    'Kimberly Miller': 2100, 'Mrs. Amy Morton': 2200, 'Carol Daugherty': 1500,
    'Joshua Flynn': 1000, 'Gregory Cox': 1300, 'Michelle Davis': 2100,
    'Anthony Shelton': 1000, 'Desiree Walton': 1900, 'Sara Walker': 1400,
    'Charles Kennedy': 2100, 'Anna Owens': 1100, 'Christopher Patterson': 1300,
    'Herbert Campbell': 2200, 'Jessica Marsh': 1200, 'Scott Greene': 1200,
    'Andrea Gray': 2000, 'Rachel Decker': 1000, 'Kelly Hamilton': 1800,
    'Christopher Taylor': 1000, 'Amanda Obrien': 1800, 'Regina Grant': 1300,
    'Frederick Gross': 1200, 'Mary Parker': 1700, 'Steven Hickman': 1600,
    'Kimberly Henry': 1000, 'Christopher Chambers': 2200, 'Lori Rodgers': 2000,
    'Carla Oconnor': 1500, 'Evan Lee': 2200, 'David Jones': 1200,
    'Rachel Richard': 1500, 'Casey Hansen': 1000, 'Leslie Krueger': 2100,
    'Robin Smith': 1600, 'Cynthia Robinson': 1400, 'John Lambert': 2200,
    'Christopher Shelton': 1300, 'Michelle Wagner': 2200, 'Kevin Odonnell': 2000,
    'Benjamin Riley': 1100, 'Amanda Reed': 1200
}

filter_players = Counter({k: v for k, v in players.items() if v > 1700})

print(filter_players)
