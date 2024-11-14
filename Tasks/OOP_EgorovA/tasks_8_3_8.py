# Фичи от продажников
# Пришли сотрудники отдела продаж и решили добавить возможность работы продуктовой корзины
# с промокодами
#
#  Для этого нужно создать дата-класс Promo, который содержит код промокода и значение его скидки.
#
# Примечание: в реальных приложениях используется база данных для хранения всех активных промокодов,
# у нас ее нет, поэтому давайте договоримся, что все активные промокоды будут находиться в
# глобальной переменной ACTIVE_PROMO.
#
# Проверьте, чтобы значение скидки было целым числом и находилось в пределах от 1 до 100,
# обозначает % от цены. При всех остальных значениях будем считать, что промокод не дает скидку
# (как вариант,  можете указать, что значение скидки составляет 0)
#
# Далее вам понадобится добавить метод apply_promo в классе Cart, который получает на вход код
# промокода и проверяет, заведен ли в переменной ACTIVE_PROMO промокод с таким названием.
# Если существует, то необходимо применить его номинал к корзине товаров.
# Сам метод apply_promo ничего не возвращает,
# только печатает текст "Промокод <promo> успешно применился" или "Промокода <promo> не существует"
#
# А вот при вызове метода get_total должен учитываться промокод или скидка, если они были применены.
#
# Примечание: промокод нельзя использовать вместе со скидкой. Используется последнее значение,
# которое применилось.


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

    def __post_init__(self):
        if not Cart.is_discount(self.discount):
            self.discount = 0


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
                print(f'Промокод {name} успешно применился')
                break
        else:
            print(f'Промокода {name} не существует')


ACTIVE_PROMO = [
    Promo('new', 20),
    Promo('all_goods', 30),
]

product1 = Product('Книга', 100.0)
product2 = Product('Флешка', 50.0)
product3 = Product('Ручка', 10.0)
print(product1, product2, product3)

cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)
print(cart.get_total())

# Применение промокода в 30%
cart.apply_promo('all_goods')
# Применение скидки в 10%. Промокод должен отмениться
cart.apply_discount(10)
print(cart.get_total())
