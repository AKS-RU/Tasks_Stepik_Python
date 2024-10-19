# Температура в градусах Цельсия
# Создайте класс Celsius, который представляет температуру в градусах Цельсия. Основная задача класса -
# предоставить возможность конвертировать температуру из градусов Цельсия в градусы Фаренгейта, а также обеспечить
# контроль за корректностью введенных значений.
#
#  Класс Celsius, должен иметь:
#
# метод __init__, который принимает значение температуры в градусах по Цельсию и сохраняет в атрибут экземпляра.
#
# метод to_fahrenheit, который выполняет конвертацию температуры из градусов Цельсия в градусы Фаренгейта по формуле
#
# °F = (°C × 9/5) + 32
#
# и возвращает результат этой конвертации.
#
# свойство-геттер temperature, которое предоставляет доступ к значению температуры
#
# свойство-сеттер temperature, которое выполняется при установке нового значения температуры. Если значение
# меньше -273.15 градусов Цельсия (абсолютный ноль), вызывается исключение ValueError. В противном случае,
# происходит установка нового значения температуры.


class Celsius:

    def __init__(self, temperature=None):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temp * 9 / 5) + 32

    @property
    def temperature(self):
        return self.temp

    @temperature.setter
    def temperature(self, new_temperature):
        if new_temperature >= -273.15:
            self.temp = new_temperature
        else:
            raise ValueError


print('*' * 15, 'ТЕСТЫ', '*' * 15)

celsius = Celsius(25)
assert celsius.temperature == 25
assert celsius.to_fahrenheit() == 77.0

celsius.temperature = 30
assert celsius.temperature == 30
assert celsius.to_fahrenheit() == 86.0

print('Все тесты пройдены успешно!')
