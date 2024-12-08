# Имеется архив files.zip, в котором содержаться файлы различных форматов.

# Посчитайте и выведите на экран суммарный размер в байтах всех файлов формата json.

from zipfile import ZipFile


with ZipFile('files.zip', mode='r') as archive:
    result = 0
    for i in archive.namelist():
        if i.endswith('.json'):
            result += (archive.getinfo(i)).file_size

print(result)
