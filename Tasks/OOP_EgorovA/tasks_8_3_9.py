# Фичи от продажников - 2
# Сотрудники отдела продаж придумали новый тип промокода и хотят, чтобы вы его добавили.
# Идея его заключается в том, что он распространяется только на определенные товары в корзине.
#
# Для этого вам нужно доработать дата-класс Promo, чтобы он мог принимать список товаров, на
# который будет распространяться промокод. Если список товаров не передать при создании, то данный
# промокод применяется ко всей корзине целиком.
#
# Также необходимо доработать метод add_product в классе Cart. Необходимо добавить возможность
# передавать в него количество товара, которое добавляется в корзину. Например, строка
#
# cart.add_product(product1, 5)
# говорит о том, что нужно добавить в корзину 5 единиц товара product1. Если не передавать
# количество
#
# cart.add_product(product1)
# то нужно считать, что добавили одну единицу товара.
#
# Вся остальная реализация остается из предыдущего задания.


from dataclasses import dataclass, field

ACTIVE_PROMO = []


@dataclass
class Product:
    name: str
    price: float = field(default=0, repr=False)


@dataclass
class Promo:
    name: str
    discount: int
    list_product: list = field(default=None)

    def __post_init__(self):
        if not Cart.is_discount(self.discount):
            self.discount = 0


class Cart:

    def __init__(self):
        self.products = []
        self.discount = 0
        self.promo = ''
        self.product_promo = None

    def add_product(self, product, value=1):
        self.products.append((product, value))

    def get_total(self):
        if self.discount and self.product_promo is None:
            tmp = sum(list(map(lambda x: x[0].price * x[1], self.products)))
            result = tmp - tmp * self.discount / 100
            del tmp
            return result
        elif self.discount and self.product_promo is not None:
            tmp_1 = 0
            tmp_2 = 0
            for i in self.products:
                if i[0] in self.product_promo:
                    tmp_1 += i[0].price * i[1]
                else:
                    tmp_2 += i[0].price * i[1]
            result = tmp_2 + (tmp_1 - tmp_1 * self.discount / 100)
            del tmp_1, tmp_2
            return result
        return sum(list(map(lambda x: x[0].price * x[1], self.products)))

    @staticmethod
    def is_discount(discount):
        return isinstance(discount, int) and 1 < discount < 100

    def apply_discount(self, discount):
        if not self.is_discount(discount):
            raise ValueError('Неправильное значение скидки')
        self.discount = discount

    def apply_promo(self, name):
        for i in ACTIVE_PROMO:
            if i.name is name:
                self.discount = i.discount
                self.promo = name
                self.product_promo = i.list_product
                print(f'Промокод {name} успешно применился')
                break
        else:
            print(f'Промокода {name} не существует')


book = Product('Книга', 100.0)
usb = Product('Флешка', 50.0)
pen = Product('Ручка', 10.0)

ACTIVE_PROMO = [
    Promo('new', 20, [pen]),
    Promo('all_goods', 30),
    Promo('sale', 50, [book, usb]),
]

cart = Cart()
cart.add_product(book, 10)
cart.add_product(pen)
cart.add_product(book, 5)
cart.add_product(usb, 5)
cart.add_product(usb, 15)
cart.add_product(pen, 2)

print(cart.get_total())

# Применение промокода в 50% на книги и флешки
cart.apply_promo('sale')
print(cart.get_total())
print(cart.product_promo)
print(cart.discount)
print(cart.products)
