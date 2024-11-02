# Задача «Оформление заказа» - 2
#
#
# Далее для оформления заказа нам нужен пользователь. Для этого создадим класс User, который содержит:
#
# метод __init__, принимающий на вход логин пользователя и необязательный аргумент — баланс его счета (по умолчанию 0).
# Логин необходимо сохранить в атрибуте login , а баланс необходимо присвоить сеттеру   balance  (см. пункт 4)
#
# метод __str__, возвращающий строку вида
# Пользователь {login}, баланс - {balance}
# Cвойство геттер balance, которое возвращает значение self.__balance;
#
# Свойство сеттер balance, принимает новое значение баланса и устанавливает его в атрибут self.__balance ;
#
# метод deposit  принимает числовое значение и прибавляет его к атрибуту self.__balance ;
#
# метод is_money_enough, который принимает числовое значение и проверяет, имеется ли у пользователя такая сумма на
# балансе. Данный метод должен возвращать булево значение: если такая сумма есть – True, если нет – False:
#
# метод payment  принимает числовое значение, которое должно списаться с баланса пользователя. Если на счете у
# пользователя не хватает средств, то необходимо вывести фразу
# Не хватает средств на балансе. Пополните счет
# и отказ в платеже. Если средств хватает, списываем с баланса у пользователя указанную сумму.
#
# (Постарайтесь внутри реализации воспользоваться методом is_money_enough)


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
            return print('Не хватает средств на балансе. Пополните счет')
        self.__balance -= value


jack = User('jack@gmail.ru', 800)
print(jack)
print(jack.balance)
jack.payment(600)
jack.payment(200)
jack.payment(1)
jack.balance = 1
jack.payment(1)
print(jack)
