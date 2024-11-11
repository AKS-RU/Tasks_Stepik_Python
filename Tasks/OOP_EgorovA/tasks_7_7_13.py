# Создайте дескриптор RangeValidator, который валидирует значение на принадлежность к определенному
# интервалу. При инициализации класс RangeValidator получает значение начала и конца интервала.
#
# При попытке сохранить нечисловое значение в дескриптор, необходимо вызывать исключение :
#
# TypeError('Неправильный тип данных')
# При попытке сохранить значение в дескриптор, которое не принадлежит интервалу, необходимо
# вызывать исключение:
#
# ValueError(f"Значение должно быть между <начало_интервала> и <конец_интервала>")
# Ваша задача реализовать только класс RangeValidator


class RangeValidator:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __get__(self, instance, owner):
        return

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Неправильный тип данных')
        elif value < self.start or value > self.end:
            raise ValueError(f"Значение должно быть между {self.start} и {self.end}")


class Temperature:
    celsius = RangeValidator(-273.15, 1000)


class Temperature:
    celsius = RangeValidator(-273.15, 1000)


class Temperature:
    celsius = RangeValidator(-273.15, 1000)
    kelvin = RangeValidator(0, 273)


temp = Temperature()
try:
    temp.celsius = -300
except ValueError as ex:
    print(ex)
try:
    temp.kelvin = 500
except ValueError as ex:
    print(ex)
