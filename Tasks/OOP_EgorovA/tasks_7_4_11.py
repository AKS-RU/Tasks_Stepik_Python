# Бесконечная арифметическая прогрессия
# Создайте класс InfinityIterator, который реализует бесконечный итератор. Он должен возвращать
# элементы арифметической прогрессии с шагом 10. Начальное значение арифметическое прогрессии по
# умолчанию равно 0, но при инициализации класса InfinityIterator может быть передано другое
# значение.
#
# Каждый член арифметической прогрессии равен предыдущему, сложенному с одним и тем же числом d.
# В нашем случае значение d=10.
#
#
#
# Вот пример работы итератора InfinityIterator:
#
#
# >>> a = iter(InfinityIterator())
# >>> next(a)
# 0
# >>> next(a)
# 10
# >>> next(a)
# 20
# >>> next(a)
# 30


class InfinityIterator:

    def __init__(self, number=0):
        self.number = number
        self.step = 10

    def __iter__(self):
        while True:
            yield self.number
            self.number = self.number + self.step

    def __next__(self):
        pass


class InfinityIterator:

    def __init__(self, number=0):
        self.number = number
        self.step = 10

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            a = self.number
            self.number += self.step
            return a


a = iter(InfinityIterator())
for i in a:
    print((i))
    if i > 200:
        break
