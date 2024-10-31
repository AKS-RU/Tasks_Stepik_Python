#                     По следам утиной типизации
# Перед вами класс BankAccount
#
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def __str__(self):
#         return self.name
# Ваша задача дописать его таким образом, чтобы его экземпляры могли участвовать в операции сортировки списка,
# в котором могут находиться только числа и другие экземпляры класса BankAccount
from functools import total_ordering


@total_ordering
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if isinstance(other, BankAccount):
            return self.balance < other.balance
        elif type(other) in (int, float):
            return self.balance < other


values = [
    BankAccount('Petrovich', 5),
    BankAccount('Ivan', 10),
    BankAccount('Andrey', 3),
    BankAccount('Lena', 15),
    BankAccount('Petr', 150)
]
values.sort(reverse=True)
print(*values)
