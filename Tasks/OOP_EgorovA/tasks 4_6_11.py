# Класс четырехугольника
# Сейчас вам нужно создать класс Quadrilateral(четырехугольник), в котором есть:
#
# метод __init__, принимающий, как правило, два значения: длину и ширину четырехугольника. Но иногда в метод __init__
# может передаваться только один аргумент, который сразу задает одно значение для ширины и длины
# (тем самым получается квадрат);
#
# метод __str__ , который работает следующим образом:
# если длина и ширина одинаковые, возвращает строку «Квадрат размером <длина>х<ширина>»
# в противном случае возвращает строку «Прямоугольник размером <длина>х<ширина>»
#  метод bool , возвращающий True, если объект является квадратом, и False в противном случае


class Quadrilateral:

    def __init__(self, length, weight=0):
        if weight:
            self.length = length
            self.weight = weight
        else:
            self.length = length
            self.weight = length

    def __str__(self):
        if self.length == self.weight:
            return f'Квадрат размером {self.length}х{self.weight}'
        return f'Прямоугольник размером {self.length}х{self.weight}'

    def __bool__(self):
        return self.length == self.weight


a = Quadrilateral(5)
print(a)
print(bool(a))
