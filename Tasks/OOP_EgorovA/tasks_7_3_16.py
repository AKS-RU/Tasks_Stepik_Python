# Класс FileReader
# Ниже в коде представлена реализация класса FileReader, который должен при итерации считывать
# построчно содержимое файла
#
# Ваша задача - дописать метод __next__, чтобы он возвращал по порядку строки из файла, пока
# содержимое файла не закончится. Строку нужно очистить слева и справа от символов пробелов и
# переносов на новую строку
#
# Файл для проверки можно скачать здесь


# class FileReader:
#     def __init__(self, filename):
#         self.file = open(filename)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         pass
#
# for line in FileReader('lorem.txt'):
#     print(line)


class FileReader:
    def __init__(self, filename):
        self.file = open(filename)

    def __iter__(self):
        return self

    def __next__(self):
        res = self.file.readline()
        if res == '':
            self.file.close()
            raise StopIteration
        return res.strip()


for line in FileReader('lorem.txt'):
    print(line)
