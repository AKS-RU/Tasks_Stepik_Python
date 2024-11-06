#                    Класс Countdown
# Создайте класс Countdown, который должен принимать начальное значение и вести обратный отсчет
# до нуля, возвращая каждое значение в последовательности каждый раз, когда вызывается __next__.
# Когда обратный отсчет достигает нуля, итератор должен вызвать исключение StopIteration.
# Для этого вам понадобится реализовать:
#
# метод __init__. Он должен принимать одно положительное число - начало отсчета
#
# методы __iter__ и __next__ для итерирования по значениям класса Countdown.


class Countdown:

    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        res = self.number
        if res < 0:
            raise StopIteration
        self.number -= 1
        return res


for i in Countdown(10):
    print(i)
