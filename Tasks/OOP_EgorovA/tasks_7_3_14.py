# Создайте класс PowerTwo, который возвращает следующую степень двойки, начиная с нулевой степени
# (20=1). Внутри класса реализуйте:
#
# метод __init__. Он должен принимать одно положительное число - степень двойки, до которой нужно
# итеририроваться включительно (см пример ниже)
#
# методы __iter__ и __next__ для итерирования по степеням двойки


class PowerTwo:

    def __init__(self, pow):
        self.pow = pow
        self.number = 2
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.pow:
            raise StopIteration
        self.count += 1
        return self.number ** self.count


numbers = PowerTwo(2)

assert hasattr(numbers, '__next__') is True
assert hasattr(numbers, '__iter__') is True

iterator = iter(numbers)
print('Элементы итератора PowerTwo(2)')
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
    raise ValueError('Не реализовали StopIteration')
except StopIteration:
    pass

print('-' * 15)
print('Элементы итератора PowerTwo(20)')
for i in PowerTwo(20):
    print(i)
