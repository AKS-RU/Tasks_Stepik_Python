#  Создайте класс City, у которого есть:
#
# конструктор __init__, принимающий единственный аргумент - название города. Вам необходимо сохранить его в качестве
#  атрибута экземпляра name, причем вам нужно преобразовать переданное имя города таким образом, чтобы первая буква
#  каждого слова была заглавной, а остальные оказались строчными (пример "new york" - > "New York")
#
# магический метод __str__, возвращающий имя города;
#
# магический метод __bool__, возвращающий False, если название города заканчивается на любую гласную букву
#  латинского алфавита (a, e, i, o, u), в противном случае True.


class City:

    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return self.name[-1] not in ('a', 'e', 'i', 'o', 'u')


p1 = City('new york')
assert p1.name == "New York"
assert p1.__str__() == "New York"
assert isinstance(p1, City)
print(p1)
assert bool(p1)

p2 = City('SaN frANCISco')
assert isinstance(p2, City)
assert p2.name == "San Francisco"
print(p2)
assert not bool(p2)

p3 = City('NIZHNY NoVGORod')
assert p3.name == "Nizhny Novgorod"
print(p3)
assert bool(p3)
assert isinstance(p3, City)
