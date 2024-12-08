# Напишите функцию is_dir_empty, которая принимает путь в папке и проверяет, пустая она или нет.

# В случае, если в папке отсутствуют файлы, необходимо вернуть True, иначе False

import os


def is_dir_empty(path: str) -> bool:
    return not os.listdir(path)


print(is_dir_empty('./files'))
