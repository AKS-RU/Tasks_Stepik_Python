# Размер файла
# Создайте класс File, представляющий файл с указанным размером в байтах. Основная цель класса заключается в
# предоставлении удобного метода для преобразования размера файла из байтов в человеко-читаемые единицы измерения
# (Килобайты, Мегабайты, Гигабайты). Класс File должен иметь:
#
# метод __init__, который принимает размер файла в байтах как аргумент и инициализирует атрибут _size_in_bytes с
# этим значением.
#
# свойство-геттер size, которое вычисляет и возвращает размер файла в удобной для чтения строковой форме. В зависимости
# от значения _size_in_bytes, метод форматирует вывод в байтах, килобайтах, мегабайтах или гигабайтах.
#
# Если размер меньше 1 КБ, выводится размер в байтах в формате "{значение } B".
# Если размер от 1 КБ до 1 МБ, выводится размер в килобайтах с двумя знаками после запятой в формате "{значение } KB".
# Если размер от 1 МБ до 1 ГБ, выводится размер в мегабайтах с двумя знаками после запятой в формате "{значение } MB".
# В противном случае (если размер больше 1 ГБ), выводится размер в гигабайтах с двумя знаками после запятой в
# формате "{значение } GB".
# свойство-сеттер size, которое позволяет изменять значение атрибута _size_in_bytes


class File:

    def __init__(self, size_in_bytes):
        self._size_in_bytes = size_in_bytes

    @property
    def size(self):
        if self._size_in_bytes < 1024:
            return f'{self._size_in_bytes} B'
        elif self._size_in_bytes >= 1024 and self._size_in_bytes / 1024 < 1024:
            return f'{self._size_in_bytes / 1024:.2f} KB'
        elif self._size_in_bytes / 1024 >= 1024 and self._size_in_bytes / 1024 / 1024 < 1024:
            return f'{self._size_in_bytes / 1024 / 1024:.2f} MB'
        elif self._size_in_bytes / 1024 / 1024 >= 1024 and self._size_in_bytes / 1024 / 1024 / 1024 < 1024:
            return f'{self._size_in_bytes / 1024 / 1024 / 1024:.2f} GB'

    @size.setter
    def size(self, new_size_in_bytes):
        self._size_in_bytes = new_size_in_bytes


print('*' * 15, 'ТЕСТЫ', '*' * 15)

file = File(5)
assert file.size == "5 B"
file.size = 1023
assert file.size == "1023 B"
file.size = 1024
assert file.size == "1.00 KB"

file_1 = File(1500000)
assert file_1._size_in_bytes == 1500000
assert file_1.size == "1.43 MB"

file_2 = File(1500)
assert file_2.size == "1.46 KB"

file_3 = File(2789326322)
assert file_3.size == "2.60 GB"
file_3.size = 1073741824
assert file_3.size == "1.00 GB"

print('Все тесты пройдены успешно!')
