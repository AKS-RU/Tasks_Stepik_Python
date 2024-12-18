# Ваша задача - написать функцию get_only_dirs, которая принимает путь и находит, какое количество
# папок находится по этому пути. В результате своей работы функция get_only_dirs должна напечатать
# названия всех каталогов, расположенных по этому пути, и их количество.

# Названия папок должны идти в алфавитном порядке, каждое следующее название должно печататься с
# новой строки. Также на самой последней строке функция get_only_dirs должна распечатать
# количество найденных папок


import os


def get_only_dirs(path: str) -> None:
    count = 0
    for i in sorted(os.listdir(path)):
        if os.path.isdir(os.path.join(path, i)):
            print(i)
            count += 1
    print(count)
