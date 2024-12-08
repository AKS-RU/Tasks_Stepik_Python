# Напишите функцию get_permissions, которая принимает путь к файлу и возвращает буквенную
# запись к его правам

import os
import stat


def get_permissions(path: str) -> str:
    stat_info = os.stat(path)
    return stat.filemode(stat_info.st_mode)[1:]
