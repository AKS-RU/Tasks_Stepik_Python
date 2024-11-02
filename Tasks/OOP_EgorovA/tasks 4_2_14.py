#                            Отображение товара
# Давайте определим магические методы __str__ и __repr__ для класса GroceryItem, представляющего продуктовый товар:
#
# Создайте класс GroceryItem, который имеет следующие методы:
#
# метод __init__, который устанавливает значения атрибутов name, price и quantity: название товара, его цену и количество
#
# магический метод __str__, который возвращает строковое представление товара в следующем виде:
# Name: {name}
# Price: {price}
# Quantity: {quantity}
# магический метод __repr__, который возвращает однозначное строковое представление объекта
# GroceryItem({name}, {price}, {quantity})


class GroceryItem:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}'

    def __repr__(self):
        return f'GroceryItem({self.name}, {self.price}, {self.quantity})'


banana = GroceryItem('Banana', 10, 5)
print(banana)
print(f"{banana!r}")

dragon_fruit = GroceryItem('Dragon fruit', 5, 350)
print(str(dragon_fruit))
print(repr(dragon_fruit))
