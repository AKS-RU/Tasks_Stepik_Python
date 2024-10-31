#                         Класс Date
# Ваша задача - создать класс Date, который хранит информацию о дате: день, месяц и год.
#
# Также класс Date должен иметь фабричный метод from_str, который принимает строку в формате
#
# день-месяц-год
# и возвращает на ее основании вновь созданный экземпляр класса Date.
#
# Проанализируйте входные данные тестовых значений для понимая состава атрибутов класса Date.
#
# Для решения задания необходимо написать только реализацию класса Date.


class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_str(cls, line_str):
        return cls(*map(int, line_str.split('-')))


day_1 = Date(20, 9, 1997)
print(day_1.day)
print(day_1.month)
print(day_1.year)

day_2 = Date(1, 2, 2003)
print(day_2.day, day_2.month, day_2.year)

day_1 = Date.from_str('12-4-2024')
day_2 = Date.from_str('06-09-2022')
print(day_1.day, day_1.month, day_1.year)
print(day_2.day, day_2.month, day_2.year)
