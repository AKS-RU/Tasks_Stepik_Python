# Переводим из HEX
# Ваша задача - реализовать класс, который принимает обозначение цвета палитры в формате HEX в виде строки и может
# перевести его в формат RGB при помощи свойств red, green, blue.
#
# Ознакомиться с форматом HEX и RGB вы можете самостоятельно в следующей статье.
#
# Для решения данной задачи напишите только реализацию класса Colour.


class Colour:

    def __init__(self, rgb):
        self.rgb = rgb

    @property
    def red(self):
        return int(self.rgb[1:3], 16)

    @property
    def green(self):
        return int(self.rgb[3:5], 16)

    @property
    def blue(self):
        return int(self.rgb[5:], 16)


colour = Colour("#00ff2d")
print(colour.red)
print(colour.green)
print(colour.blue)
