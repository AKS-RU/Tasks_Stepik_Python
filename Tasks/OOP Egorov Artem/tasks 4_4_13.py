# Создайте класс  Order, который имеет следующие методы:
#
# метод __init__, который устанавливает значения атрибутов cart и customer: список покупок и имя покупателя
#
# магический метод __add__, который описывает добавление товара в список покупок. Результатом такого сложения должен
# быть новый заказ, в котором все покупки берутся из старого заказа и в конец добавляется новый товар.
# Покупатель в заказе остается прежним
#
# магический метод __radd__, который описывает добавление товара в список покупок при правостороннем сложении.
# Результатом такого сложения должен быть новый заказ, в котором все покупки берутся из старого заказа и в начало
# списка покупок добавляется новый товар. Покупатель в заказе остается прежним
# магический метод __sub__, который описывает исключение товара из списка покупок.
# Результатом вычитания должен быть новый заказ
#
#
# магический метод __rsub__, который описывает исключение товара из списка покупок при правостороннем вычитании.
# Результатом должен быть таким же как и при __sub__


class Order:

    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __add__(self, other):
        lst = self.cart.copy()
        lst.append(other)
        return Order(lst, self.customer)

    def __radd__(self, other):
        lst = self.cart.copy()
        lst.insert(0, other)
        return Order(lst, self.customer)

    def __sub__(self, other):
        lst = self.cart.copy()
        if other in lst:
            lst.remove(other)
        return Order(lst, self.customer)

    def __rsub__(self, other):
        return self - other


order = Order(['banana', 'apple'], 'Гена Букин')

order_2 = order + 'orange'
print(order.cart, order.customer)
print(order_2.cart, order_2.customer)
assert order.cart == ['banana', 'apple']
assert order.customer == 'Гена Букин'
assert order_2.cart == ['banana', 'apple', 'orange']

order = 'mango' + order
assert order.cart == ['mango', 'banana', 'apple']
order = 'ice cream' + order
assert order.cart == ['ice cream', 'mango', 'banana', 'apple']

print(order.cart)
order = order - 'banana'
print(order.cart)
assert order.cart == ['ice cream', 'mango', 'apple']

order3 = order - 'banana'
assert order3.cart == ['ice cream', 'mango', 'apple']

order = order - 'mango'
assert order.cart == ['ice cream', 'apple']
order = 'lime' - order
assert order.cart == ['ice cream', 'apple']
print('Good')
