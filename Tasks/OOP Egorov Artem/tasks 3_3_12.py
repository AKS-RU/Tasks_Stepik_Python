# Треугольники
# Создайте класс Triangle, в котором реализованы следующие методы
#
# метод __init__, принимающий три стороны треугольника
#
# метод is_exists, который отвечает на вопрос существует ли треугольник с текущими сторонами
# Треугольник существует, если каждая сторона треугольника меньше суммы двух других сторон.
# метод is_equilateral, который проверяет является ли треугольник равносторонним
# Треугольник называется равносторонним, если у него все стороны равны
# метод is_isosceles, который проверяет является ли треугольник равнобедренным и существующим.
# Треугольник называется равнобедренным, если у него две стороны равны


class Triangle():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_exists(self):
        a, b, c = self.a, self.b, self.c
        return a < (b + c) and b < (a + c) and c < (a + b)

    def is_equilateral(self):
        a, b, c = self.a, self.b, self.c
        return a == b and b == c

    def is_isosceles(self):
        a, b, c = self.a, self.b, self.c
        return (a == b or b == c or c == a) and self.is_exists()


triangle = Triangle(3, 4, 5)
assert triangle.is_exists() is True
assert triangle.is_equilateral() is False
assert triangle.is_isosceles() is False

triangle = Triangle(5, 5, 5)
assert triangle.is_exists() is True
assert triangle.is_equilateral() is True
assert triangle.is_isosceles() is True

triangle = Triangle(5, 4, 5)
assert triangle.is_exists() is True
assert triangle.is_equilateral() is False
assert triangle.is_isosceles() is True

triangle = Triangle(5, 16, 5)
assert triangle.is_exists() is False
assert triangle.is_equilateral() is False
assert triangle.is_isosceles() is False
print('Все тесты пройдены успешно!')
