# Создайте базовый класс  Person, у которого есть:
#
# конструктор __init__, который должен принимать на вход имя и записывать его в атрибут name
#
# метод get_name, который возвращает атрибут name
#
# метод  is_employee, который возвращает  False
# Затем создайте подкласс Employee , унаследованный от Person. В нем должен быть реализован:
#
# метод  is_employee, который возвращает  True


class Person:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


class Employee(Person):

    def is_employee(self):
        return True


assert issubclass(Employee, Person)

p = Person("just human")
assert p.name == 'just human'
assert p.get_name() == 'just human'
assert p.is_employee() is False

emp = Employee("Geek")
assert emp.name == 'Geek'
assert emp.get_name() == 'Geek'
assert emp.is_employee() is True
print('Good')
