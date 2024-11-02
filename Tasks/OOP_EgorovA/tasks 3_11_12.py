# Задача «Оформление заказа» - 3
#
#
# Последний штрих — создание класса корзины, куда пользователь будет складывать товары. Для этого нам понадобятся
# ранее созданные классы User и Product
#
# Итак, создаем класс Cart, который содержит:
#
# метод __init__, принимающий на вход экземпляр класса User . Его необходимо сохранить в атрибуте user .
# Помимо этого, метод  должен создать атрибут goods — пустой словарь (лучше использовать defaultdict). Он нужен будет для хранения товаров и их количества (ключ словаря — товар, значение — количество). И еще нам понадобится создать защищенный атрибут .__total со значением 0. В нем будет храниться итоговая сумма заказа
#
# метод add принимает на вход экземпляр класса Product и необязательный аргумент — количество товаров (по умолчанию 1).
# Метод add  должен увеличить в корзине (атрибут goods) количество указанного товара  на переданное значение количества и пересчитать атрибут self.__total
#
# метод remove  принимает на вход экземпляр класса Product и необязательный аргумент — количество товаров
# (по умолчанию 1).  Метод remove  должен уменьшить в корзине (атрибут goods) количество указанного товара  на переданное значение количества и пересчитать атрибут self.__total. Обратите внимание на то, что количество товара в корзине не может стать отрицательным, как и итоговая сумма;
#
# свойство геттер total , которое возвращает значение self.__total;
#
# метод order  должен использовать метод payment  из класса User и передать в него итоговую сумму корзины.
# В случае, если средств пользователю хватило, вывести сообщение «Заказ оплачен»,
# в противном случае - «Проблема с оплатой»;
#
# метод print_check , печатающий на экран чек. Он должен начинаться со строки
# ---Your check---
# Затем выводится состав корзины в алфавитном порядке по названию товара в виде
# {Имя товара} {Цена товара} {Количество товара} {Сумма}
# И заканчивается чек строкой
# ---Total: {self.total}---
# Пример использования класса Cart
#
# billy = User('billy@rambler.ru')
#
# lemon = Product('lemon', 20)
# carrot = Product('carrot', 30)
#
# cart_billy = Cart(billy)
# print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
# cart_billy.add(lemon, 2)
# cart_billy.add(carrot)
# cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 2 40
# ---Total: 70---'''
# cart_billy.add(lemon, 3)
# cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 5 100
# ---Total: 130---'''
# cart_billy.remove(lemon, 6)
# cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# ---Total: 30---'''
# print(cart_billy.total) # 30
# cart_billy.add(lemon, 5)
# cart_billy.print_check()
# ''' Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 5 100
# ---Total: 130---'''
# cart_billy.order()
# ''' Печатает текст ниже
# Не хватает средств на балансе. Пополните счет
# Проблема с оплатой'''
# cart_billy.user.deposit(150)
# cart_billy.order() # Заказ оплачен
# print(cart_billy.user.balance) # 20


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:

    def __init__(self, login, balance=0):
        self.login = login
        self.__balance = 0
        self.balance = balance

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.__balance}'

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def deposit(self, value):
        self.__balance += value

    def is_money_enough(self, value):
        return value <= self.__balance

    def payment(self, value):
        if not self.is_money_enough(value):
            print('Не хватает средств на балансе. Пополните счет')
            return False
        self.__balance -= value
        return True


class Cart:

    def __init__(self, user):
        self.user = user
        self.goods = {}
        self.__total = 0

    def add(self, product, quantity=1):
        if product not in self.goods:
            self.goods.setdefault(product, quantity)
        else:
            self.goods[product] += quantity

        self.__total += product.price * quantity

    def remove(self, product, quantity=1):
        if self.goods.get(product) >= quantity:
            self.goods[product] -= quantity
            self.__total -= product.price * quantity
        else:
            quantity = self.goods[product]
            self.__total -= product.price * quantity
            self.goods[product] -= quantity

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.__total):
            return print('Заказ оплачен')
        print('Проблема с оплатой')

    def print_check(self):
        print('---Your check---')
        [print(f'{k.name} {k.price} {v} {k.price * v}') for k, v in sorted(self.goods.items(), key=lambda x: x[0].name)
         if v != 0]
        print(f'---Total: {self.__total}---')


billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user)  # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total)  # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order()  # Заказ оплачен
print(cart_billy.user.balance)  # 20
