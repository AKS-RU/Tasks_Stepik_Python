# Создайте класс BankDeposit, который имеет следующие методы:
#
# метод __init__, который устанавливает значения атрибутов name, balance и rate: владелец депозита, значение депозита
# и годовая процентная ставка.
#
# приватный метод __calculate_profit, который возвращает количество денег, которое заработает владелец счета через год
# с учетом его годовой ставки.
#
# публичный метод get_balance_with_profit, который возвращает общее количество средств, которое будет у владельца
# депозита через год.


class BankDeposit:

    def __init__(self, name, balance, rate):
        self.name = name
        self.balance = balance
        self.rate = rate

    def __calculate_profit(self):
        return self.balance * self.rate / 100

    def get_balance_with_profit(self):
        return self.__calculate_profit() + self.balance


print('*' * 15, 'ТЕСТЫ', '*' * 15)
account = BankDeposit("John Connor", 1000, 5)
assert account.name == "John Connor"
assert account.balance == 1000
assert account.rate == 5
assert account._BankDeposit__calculate_profit() == 50.0
assert account.get_balance_with_profit() == 1050.0

account_2 = BankDeposit("Sarah Connor", 200, 27)
assert account_2.name == "Sarah Connor"
assert account_2.balance == 200
assert account_2.rate == 27
assert account_2._BankDeposit__calculate_profit() == 54.0
assert account_2.get_balance_with_profit() == 254.0
print('Все тесты пройдены успешно!')
