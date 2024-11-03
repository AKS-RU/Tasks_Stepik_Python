# Задача «Оформление заказа»
# Вы наверняка сталкивались с оформлением заказов в онлайн магазинах. Давайте и мы воссоздадим этот процесс
#
#
#
# Часть 1
# Для этого нам понадобится реализовать несколько классов и связать их между собой. Первый класс, который мы реализуем,
# будет Product. Это класс, описывающий товар. В нем должно быть реализовано:
#
# метод __init__, принимающий на вход имя товара и его стоимость. Эти значения необходимо сохранить в
# атрибутах name и price
# Пример работы с классом Product
#
# carrot = Product('carrot', 30)
# print(carrot.name, carrot.price)


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


carrot = Product('carrot', 30)
print(carrot.name, carrot.price)