# Создайте класс Folder, который содержит

# метод инициализации, сохраняющий путь к папке
# атрибут count, являющийся non-data дескриптором FileCount
# Дескриптор FileCount должен при обращении возвращать количество файлов,
# содержащихся внутри папки

# Пример использования

# folder = Folder('/')
# print('file count: ', folder.count)

import os


class FileCount:

    def __get__(self, instance, owner):
        return len(os.listdir(instance.path))


class Folder:
    count = FileCount()

    def __init__(self, path):
        self.path = path


folder_include = Folder('include')
print(folder_include.count)
assert folder_include.count == 4

folder_nested = Folder('nested')
assert folder_nested.count == 3

print('Good')
