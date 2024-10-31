# Перед вами имеется реализация класса Circle. Ваша задача добавить в него следующее:
#
# класс-метод from_diameter, принимающий диаметр круга. Метод from_diameter должен возвращать новый экземпляр класса
# Circle(учитывайте, что экземпляры круга создаются по радиусу);
#
# статик-метод is_positive, принимающий одно число. Метод is_positive должен возвращать ответ, является ли переданное
# число положительным;
#
# статик-метод area, который принимает радиус и возвращает площадь круга. Для этого воспользуйтесь формулой
# pi∗r**2
# и в качестве значения pi возьмите 3.14
# Ваша задача только добавить реализацию трех методов в класс Circle

class Circle:

    def __init__(self, radius):
        if not Circle.is_positive(radius):
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @staticmethod
    def is_positive(number):
        return number > 0

    @staticmethod
    def area(radius):
        return round(3.14 * radius ** 2, 2)


print('*' * 15, 'ТЕСТЫ', '*' * 15)

circle_1 = Circle.from_diameter(10)
assert isinstance(circle_1, Circle)
assert circle_1.radius == 5.0
print(f"circle_1.radius={circle_1.radius}")
assert Circle.is_positive(10)
assert not Circle.is_positive(-5)
assert Circle.area(1) == 3.14
assert Circle.area(2) == 12.56

print('Все тесты пройдены успешно!')
