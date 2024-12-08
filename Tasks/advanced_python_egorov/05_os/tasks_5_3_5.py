# Супер задание
# Оформите программу из прошлого урока в виде класса. Имя класса, состав его атрибутов и методов
# \вы выбираете сами. Главная цель данного класса - вывод информации обо всем содержимом первого
# уровня по указанному пути. Плюс необходимо добавить следующие возможности фильтрации:

# выводить информацию только о файлах
# выводить информацию только о каталогах
# выводить информацию только о файлах определенного расширения
# выводить информацию только о файлах, которые менялись не более N суток назад
# Все указанные фильтры являются необязательными. По умолчанию класс выводит информацию обо всем
# содержимом переданного каталога

# Не забывайте после отправки поделиться своим решением с другими учениками, оставив свой код на
# вкладке Решение


import os
from datetime import datetime, timedelta


class InfoDirect:

    def __init__(self, path: str):
        self.path = path

    def __str__(self):
        return '\n'.join(i for i in sorted(os.listdir(self.path)))

    @property
    def files(self):
        return [i for i in os.listdir(self.path) if os.path.isfile(
            os.path.join(self.path, i))]

    @property
    def directories(self):
        return [i for i in os.listdir(self.path) if os.path.isdir(
            os.path.join(self.path, i))]

    def ext_files(self, ext):
        ext = ext.lower()
        return [i for i in self.files if i.endswith(f'.{ext}')]

    def mod_files(self, day: int):
        threshold_date = datetime.now() - timedelta(days=day)
        result = []
        for i in self.files:
            info_mod = datetime.fromtimestamp(
                os.path.getmtime(os.path.join(self.path, i)))
            if info_mod < threshold_date:
                result.append(i)
        return result


a = InfoDirect(r'D:\USERS\User\Documents')
print(a.path)
print(a.files)
print(a.directories)
print(a.ext_files('PNg'))
print(a.mod_files(11))
