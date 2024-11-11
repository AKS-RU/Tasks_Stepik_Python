# Переводим из HEX с дескриптором
# Перед вами реализация класса Colour
#
# class Colour:
#     def __init__(self, hex_string):
#         self.hex = hex_string
#
#     @property
#     def r(self):
#         return int(self.hex[1:3], 16)
#
#     @property
#     def g(self):
#         return int(self.hex[3:5], 16)
#
#     @property
#     def b(self):
#         return int(self.hex[5:7], 16)
# Данный класс принимает обозначение цвета в формате HEX в виде строки. И далее при помощи
# свойств r, g, b получает соответствующие значения. Вот пример использования:
#
# colour = Colour("#ff8800")
# print(colour.r)  # печатает 255
# print(colour.g)  # печатает 136
# print(colour.b)  # печатает 0
# Ваша задача - переписать реализацию класса Colour, заменив свойства на использование дескриптора
# ColourComponent. Сам дескриптор ColourComponent должен иметь атрибуты start и еnd, обозначающие
# начальную и конечную позиции извлечения цвета.
#
# Вот такая заготовка у вас будет для класса Colour
#
# class Colour:
#     r = ColourComponent(1, 3)
#     g = ColourComponent(3, 5)
#     b = ColourComponent(5, 7)
#
#     def __init__(self, hex):
#         self.hex = hex
# Остается реализовать только дескриптор ColourComponent


class ColourComponent:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __get__(self, instance, owner):
        return int(instance.hex[self.start:self.end], 16)


class Colour:
    r = ColourComponent(1, 3)
    g = ColourComponent(3, 5)
    b = ColourComponent(5, 7)

    def __init__(self, hex):
        self.hex = hex


colour = Colour("#abcded")
print(colour.r)
print(colour.g)
print(colour.b)
