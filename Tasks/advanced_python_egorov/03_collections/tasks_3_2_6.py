# Создайте класс ExtraDict, унаследованный отUserDict и предоставляющий дополнительно
# следующие методы:
#
# map(func): принимает название функции в качестве аргумента и применяет ее ко всем значениям
# в базовом словаре
#
# remove(key): удаляет указанный ключ из базового словаря, в случае отсутствия ключа бросает
# исключение KeyError
#
# is_empty(): возвращает True или False в зависимости от того, пуст ли словарь или нет.

from math import factorial
from collections import UserDict


# Напишите определение класса ExtraDict
class ExtraDict(UserDict):

    def map(self, func):
        if not self.is_empty():
            self.data = dict(map(lambda x: (x[0], func(x[1])), self.items()))
            return self

    def remove(self, key):
        if self.is_empty():
            raise KeyError
        self.pop(key)

    def is_empty(self):
        return len(self) == 0


my_dict = ExtraDict({'a': 1, 'b': 2, 'c': 3})
print("Original dictionary:", my_dict.data)

my_dict.map(lambda x: x * 2)
print("Dictionary after applying 'map':", my_dict.data)

my_dict.map(factorial)
print("Dictionary after applying factorial:", my_dict.data)

my_dict.remove('b')
my_dict.pop('c')

print(my_dict.data)

assert not my_dict.is_empty()

my_dict.remove('a')

assert my_dict.is_empty()

try:
    my_dict.remove('a')
except KeyError:
    pass
