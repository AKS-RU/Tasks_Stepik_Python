# А как же без корзины товаров
# Создайте дата-класс Product, который хранит информацию о названии продукта и о его цене.
# При выводе товара должна отображаться только информация о его имени. Обязательно
# назовите name атрибут, который хранит название. Цену товара можете назвать как хотите
#
# Затем создайте класс продуктовой корзины Cart, в котором должна быть реализована возможность
#
# добавлять товары в корзины при помощи метода add_product. Добавляется один продукт за один
# вызов метода
#
# посчитать общую сумму содержащихся товаров в корзине при помощи метода get_total
#
# возможность применить скидку через apply_discount. Данный метод должен принимать размер
# скидки - целое число от 1 до 100, обозначающее % от цены, и сохранять его в экземпляре класса.
# Если передать любое другое значение, то нужно вызывать исключение.
# Данный метод возвращать ничего не должен
# raise ValueError('Неправильное значение скидки')


from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float = field(default=0, repr=False)


class Cart:

    def __init__(self):
        self.products = []
        self.discount = 0

    def add_product(self, product):
        self.products.append(product)

    def get_total(self):
        if self.discount:
            tmp = sum(list(map(lambda x: x.price, self.products)))
            result = tmp - tmp * self.discount / 100
            del tmp
            return result
        return sum(list(map(lambda x: x.price, self.products)))

    def apply_discount(self, discount):
        if not isinstance(discount, int) or discount > 100 or discount < 1:
            raise ValueError('Неправильное значение скидки')
        self.discount = discount


product1 = Product('Книга', 100.0)
product2 = Product('Флешка', 50.0)
product3 = Product('Ручка', 10.0)
print(product1, product2, product3)

cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)
print(cart.get_total())

# Применение скидки 200%
try:
    cart.apply_discount(20)
except ValueError as e:
    print(e)
print(cart.get_total())
