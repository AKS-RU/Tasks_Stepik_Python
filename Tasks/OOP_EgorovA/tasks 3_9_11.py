# Класс, содержащий набор функций
# Физики заказали вам создать несколько функций, которые помогают конвертировать температуру из градусов по Цельсию в
# градусы по Кельвину и по Фаренгейту. Но так как все эти функции работают с температурами, мы решаем объединить их в
# один класс TemperatureConverter
#
# Создайте класс TemperatureConverter, который имеет следующие методы:
#
#  статический метод celsius_to_fahrenheit, который принимает температуру в градусах Цельсия и переводит ее в градусы
# по Фаренгейту, используя следующую формулу:
#
#
# статический метод fahrenheit_to_celsius, который принимает температуру в градусах по Фаренгейту и переводит ее в
# градусы Цельсия, используя следующую формулу:
#
#
# статический метод celsius_to_kelvin, который переводит из Цельсия в Кельвин путем прибавления значения 273.15
#
#
# статический метод kelvin_to_celsius, который переводит из Кельвин в градусы по Цельсию путем уменьшения
# значения на 273.15
#
# два статических метода fahrenheit_to_kelvin и kelvin_to_fahrenheit, выполняющих преобразование градусов по
# Фаренгейту в Кельвины и наоборот. Рассчитываются они по следующим формулам
#
#
#
#
# статический метод format, принимающий значение градусов и один из символов K, F, C. Возвращает строку с красивым
# отображением градусов в указанной единице измерения.
# F соответствует °F
#
# C соответствует °C
#
# K соответствует °K


class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(temp_degree):
        return temp_degree * (9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(temp_fahrenheit):
        return (temp_fahrenheit - 32) * (5 / 9)

    @staticmethod
    def celsius_to_kelvin(temp_degree):
        return temp_degree + 273.15

    @staticmethod
    def kelvin_to_celsius(temp_kelvin):
        return temp_kelvin - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(temp_fahrenheit):
        return (5 / 9 * (temp_fahrenheit - 32)) + 273.15

    @staticmethod
    def kelvin_to_fahrenheit(temp_kelvin):
        return round((9 / 5 * (temp_kelvin - 273.15)) + 32, 2)

    @staticmethod
    def format(value, k_f_c):
        return f'{value}{chr(176)}{k_f_c}'


print('*' * 15, 'ТЕСТЫ', '*' * 15)

assert TemperatureConverter.celsius_to_fahrenheit(0) == 32.0
assert TemperatureConverter.celsius_to_fahrenheit(10) == 50.0
assert TemperatureConverter.celsius_to_fahrenheit(15) == 59.0
assert TemperatureConverter.celsius_to_fahrenheit(20) == 68.0
assert TemperatureConverter.celsius_to_fahrenheit(25) == 77.0
assert TemperatureConverter.celsius_to_fahrenheit(30) == 86.0

assert TemperatureConverter.fahrenheit_to_celsius(86) == 30.0
assert TemperatureConverter.fahrenheit_to_celsius(77) == 25.0
assert TemperatureConverter.fahrenheit_to_celsius(68) == 20.0
assert TemperatureConverter.fahrenheit_to_celsius(59) == 15.0
assert TemperatureConverter.fahrenheit_to_celsius(50) == 10.0
assert TemperatureConverter.fahrenheit_to_celsius(32) == 0

converter = TemperatureConverter()
assert converter.celsius_to_kelvin(100) == 373.15
assert converter.kelvin_to_celsius(273.15) == 0
assert converter.fahrenheit_to_kelvin(50) == 283.15
assert converter.fahrenheit_to_kelvin(134.33) == 330.0
assert converter.kelvin_to_fahrenheit(54.0) == -362.47
assert converter.kelvin_to_fahrenheit(1653.0) == 2515.73
assert converter.format(1653.0, 'K') == '1653.0°K'
assert converter.format(45, 'F') == '45°F'
assert converter.format(36.6, 'C') == '36.6°C'

print('Все тесты пройдены успешно!')
