# Реализуйте класс Wallet, аналог денежного кошелька, содержащий информацию о валюте и остатке имеющихся средств на
# счете. В данном классе должны быть реализованы:
#
# метод __init__, который создает атрибуты currency и balance. Значения атрибутов currency и balance поступают при вызове
# метода __init__. При этом значение атрибута currency должно быть строкой, состоящей только из трех заглавных букв.
# Для этого необходимо сделать именно в такой последовательности следующие проверки:
# В случае, если передается не строка, нужно возбуждать исключение TypeError с текстом «Неверный тип валюты» ;
# В случае, если передается строка, длина которой не равна трем символам, нужно возбуждать исключение NameError с текстом
# «Неверная длина названия валюты»
# В случае, если строка не состоит из заглавных символов, нужно возбуждать исключение ValueError с текстом
# «Название должно состоять только из заглавных букв»
# метод __eq__, для возможности сравнивания балансов кошельков. Операция сравнения доступна только для кошельков с
# одинаковой валютой. Если валюты различаются, необходимо возбудить исключение ValueError с текстом
# "Нельзя сравнить разные валюты". При попытке сравнить экземпляр класса Wallet с другими объектами необходимо
# возбудить исключение TypeError с текстом «Wallet не поддерживает сравнение с <объектом>»;
# методы __add__ и __sub__ для возможности суммирования и вычитания кошельков. Складывать и вычитать мы можем только
# с другим экземпляром класса Wallet и только в случае, когда у них совпадает валюта (атрибуты currency).
# Результатом такого сложения должен быть новый экземпляр класса Wallet , у которого валюта совпадает с валютой
# операндов и значение баланса равно сумме/вычитанию их балансов (при вычитании баланс может оказаться отрицательным).
# Если попытаться сложить с объектом не являющимся экземпляром Wallet или значения валют у объектов не совпадают,
# необходимо возбудить исключение ValueError с текстом  «Данная операция запрещена»


class Wallet:

    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError('Неверный тип валюты')
        elif len(currency) != 3:
            raise NameError('Неверная длина названия валюты')
        elif not currency.isupper():
            raise ValueError('Название должно состоять только из заглавных букв')
        self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if isinstance(other, Wallet):
            if self.currency == other.currency:
                return self.balance == other.balance
            raise ValueError('Нельзя сравнить разные валюты')
        raise TypeError(f'Wallet не поддерживает сравнение с {other}')

    def __add__(self, other):
        if isinstance(other, Wallet):
            if self.currency == other.currency:
                return Wallet(self.currency, self.balance + other.balance)
            raise ValueError('Данная операция запрещена')
        raise ValueError('Данная операция запрещена')

    def __sub__(self, other):
        if isinstance(other, Wallet):
            if self.currency == other.currency:
                return Wallet(self.currency, self.balance - other.balance)
            raise ValueError('Данная операция запрещена')
        raise ValueError('Данная операция запрещена')


wallet1 = Wallet('USD', 50)
wallet2 = Wallet('RUB', 100)
wallet3 = Wallet('RUB', 150)
# wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
# wallet5 = Wallet('qwerty', 150)  # исключение NameError('Неверная длина названия валюты')
# wallet6 = Wallet('abc', 150)  # исключение ValueError('Название должно состоять только из заглавных букв')

print(wallet2 == wallet3)  # False
# print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
# print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')

wallet7 = wallet2 + wallet3
print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
wallet2 + 45  # ValueError('Данная операция запрещена')
print('OK')
