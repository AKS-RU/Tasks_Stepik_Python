# Создайте класс Rectangle, у которого есть:
#
# конструктор __init__, принимающий 2 аргумента: длину и ширину.
# # свойство area, которое возвращает площадь прямоугольника;


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.width * self.length


print('*' * 15, 'ТЕСТЫ', '*' * 15)

r1 = Rectangle(5, 10)
assert isinstance(r1, Rectangle)
assert r1.area == 50
assert isinstance(type(r1).area, property), 'Вы не создали property area'

r2 = Rectangle(15, 3)
assert isinstance(r2, Rectangle)
assert r2.area == 45
assert isinstance(type(r2).area, property), 'Вы не создали property area'

r3 = Rectangle(43, 232)
assert r3.area == 9976

print('Все тесты пройдены успешно!')
