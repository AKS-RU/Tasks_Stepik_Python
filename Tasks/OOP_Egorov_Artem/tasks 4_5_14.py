# Создайте класс  Fruit, который имеет:
#
# метод __init__, который устанавливает значения атрибутов name и price: название и цена фрукта
#
# методы сравнения. Здесь вы сами решаете, какие магические методы реализовывать. Главное, чтобы фрукты могли
# сравниваться с числами и другими фруктами по цене. Смотрите тесты ниже в коде.


class Fruit:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if type(other) in (int, float):
            return self.price == other
        elif isinstance(other, Fruit):
            return self.price == other.price

    def __gt__(self, other):
        if type(other) in (int, float):
            return self.price > other
        elif isinstance(other, Fruit):
            return self.price > other.price

    def __lt__(self, other):
        if type(other) in (int, float):
            return self.price < other
        elif isinstance(other, Fruit):
            return self.price < other.price

    def __ge__(self, other):
        return self == other or self > other

    def __le__(self, other):
        return self == other or self < other


apple = Fruit("Apple", 0.5)
orange = Fruit("Orange", 1)
banana = Fruit("Banana", 1.6)
lime = Fruit("Lime", 1.0)

assert (banana > 1.2) is True
assert (banana >= 1.2) is True
assert (banana == 1.2) is False
assert (banana != 1.2) is True
assert (banana < 1.2) is False
assert (banana <= 1.2) is False

assert (apple > orange) is False
# assert (apple >= orange) is False
assert (apple == orange) is False
assert (apple != orange) is True
assert (apple < orange) is True
assert (apple <= orange) is True

assert (orange == lime) is True
assert (orange != lime) is False
assert (orange > lime) is False
assert (orange < lime) is False
assert (orange <= lime) is True
assert (orange >= lime) is True
print('Good')
