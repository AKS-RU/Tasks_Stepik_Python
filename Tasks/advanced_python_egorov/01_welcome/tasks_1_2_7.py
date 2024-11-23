# Корзина товаров
# В этом задании предлагается разработать два класса: ShoppingCart (Корзина для покупок) и
# Product (Товар). Класс ShoppingCart позволяет добавлять и удалять товары, а также вычислять
# общую стоимость товаров в корзине. Класс Product представляет товар с именем и ценой.
#
#
#
# Класс ShoppingCart и его методы:
#
# метод __init__, который инициализирует пустой список _items, представляющий товары в корзине.
#
# метод add_item(self, item), который добавляет товар в корзину. Принимает экземпляр класса Product
# как аргумент и добавляет его в список _items.
#
# метод remove_item(self, item), который удаляет товар из корзины. Принимает экземпляр класса
# Product и удаляет его единожды из списка _items. При отсутствии товара в корзине необходимо
# вызывать исключение ValueError
#
# создайте метод __len__ для возможности определения количества товаров в корзине
#
# вычисляемое свойство total_price, которое вычисляет общую стоимость товаров в корзине.
# Вычисление осуществляется путем суммирования цен всех товаров в атрибуте_items.
#
# вычисляемое свойство items, которое возвращает список товаров в корзине в порядке
# увеличения цены, в случае совпадения цены необходимо отсортировать в алфавитном порядке.
#
# Класс Product  должен быть дата-классом и содержать следующие атрибуты:
#
# name - название товара
# price - цена товара


from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float


class ShoppingCart:

    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    @property
    def total_price(self):
        return sum(map(lambda x: x.price, self._items))

    @property
    def items(self):
        return sorted(self._items, key=lambda x: (x.price, x.name))


apple = Product("Apple", 1.5)
banana = Product("Banana", 0.75)
chocolate = Product("Chocolate", 2.99)

cart = ShoppingCart()
cart.add_item(banana)
cart.add_item(apple)
cart.add_item(chocolate)

assert len(cart) == 3
assert cart.items == [banana, apple, chocolate]
milk = Product('Milk', 1)
cart.add_item(milk)
assert cart.items == [banana, milk, apple, chocolate]
print("Items in the cart:", [item.name for item in cart.items])
print("Total price:", cart.total_price)
assert cart.total_price == 6.24
cart.add_item(banana)
assert len(cart) == 5
assert cart.total_price == 6.99
cart.remove_item(milk)
assert len(cart) == 4
cart.remove_item(banana)
cart.remove_item(banana)
assert len(cart) == 2
try:
    cart.remove_item(banana)
except ValueError:
    pass

print('OK')
