#    Создайте класс Money, у которого есть:
#
# конструктор __init__, принимающий 2 аргумента: dollars, cents. По входным аргументам вам необходимо создать атрибут
# экземпляра total_cents.
#
# свойство-геттер dollars, которое возвращает количество имеющихся долларов;
#
# свойство-сеттер dollars, которое принимает целое неотрицательное число — количество долларов и устанавливает при
# помощи него новое значение в атрибут экземпляра total_cents, при этом значение центов должно сохраняться.
# В случае, если в сеттер передано число, не удовлетворяющее условию, нужно вывести на экран сообщение "Error dollars";
#
# свойство геттер cents, которое возвращает количество имеющихся центов;
#
# свойство сеттер cents, которое принимает целое неотрицательное число меньшее 100  количество центов и устанавливает
# при помощи него новое значение в атрибут экземпляра total_cents, при этом значение долларов должно сохраняться.
# В случае, если в сеттер передано число, не удовлетворяющее условию, нужно вывести на экран сообщение "Error cents";
#
# метод __str__ (информация по данному методу), который возвращает строку вида
#    "Ваше состояние составляет {dollars} долларов {cents} центов". Для нахождения долларов и центов в
# методе __str__ пользуйтесь свойствами
# В экземпляр класса кроме атрибута total_cents сохранять ничего не нужно!


class Money:

    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, dollars):
        if isinstance(dollars, int) and dollars >= 0:
            a = self.total_cents % 100
            self.total_cents = dollars * 100 + a
        else:
            print('Error dollars')

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, cents):
        if isinstance(cents, int) and cents >= 0 and cents < 100:
            a = self.total_cents // 100
            self.total_cents = a * 100 + cents
        else:
            print('Error cents')

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'


print('*' * 15, 'ТЕСТЫ', '*' * 15)

bill = Money(101, 99)
assert isinstance(bill, Money)

print(bill)  # Ваше состояние составляет 101 долларов 99 центов
print(bill.dollars, bill.cents)  # 101 99
bill.dollars = 666
print(bill.dollars, bill.cents)  # 101 99
print(bill)  # Ваше состояние составляет 666 долларов 99 центов
bill.cents = 12
print(bill)  # Ваше состояние составляет 666 долларов 12 центов
assert bill.total_cents == 66612
print(bill.dollars, bill.cents)  # 101 99
assert list(bill.__dict__.keys()) == ['total_cents']

ken = Money(111, 90)
assert isinstance(ken, Money)
print(ken)
ken.dollars = 'hello'  # Error dollars
ken.dollars = 0
print(ken)
ken.cents = [1, 2, 3]  # Error cents
ken.cents = 100  # Error cents
ken.cents = 99
print(ken)

print('Все тесты пройдены успешно!')
