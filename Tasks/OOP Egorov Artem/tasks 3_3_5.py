# Создайте класс Rectangle, который имеет следующие методы:
#
# метод __init__, который устанавливает значения атрибутов width и height
#
# метод area, который возвращает площадь прямоугольника
#
# метод perimeter , который возвращает периметр прямоугольника


class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2


r1 = Rectangle(2, 3)
assert r1.width == 2
assert r1.height == 3
assert r1.perimeter() == 10
assert r1.area() == 6

r2 = Rectangle(10, 0.5)
assert r2.width == 10
assert r2.height == 0.5
assert r2.perimeter() == 21.0
assert r2.area() == 5.0
print('Все тесты пройдены успешно!')
