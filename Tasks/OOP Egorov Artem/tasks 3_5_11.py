#  Создайте класс Student, у которого есть:
#
# конструктор __init__, который принимает 3 аргумента и создает приватные атрибуты __name, __age, __branch;
#
# приватный метод __display_details , который выводит на экран информацию о студенте в следующем виде:
# Имя: <name>
# Возраст: <age>
# Направление: <branch>
# метод access_private_method, который вызывает приватный метод __display_details.


class Student:

    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f'Имя: {self.__name}\nВозраст: {self.__age}\nНаправление: {self.__branch}')

    def access_private_method(self):
        self.__display_details()


print('*' * 15, 'ТЕСТЫ', '*' * 15)
adam = Student("Adam Smith", 25, "Information Technology")
piter = Student("Piter Parker", 34, "Information Security")

adam.access_private_method()
assert piter._Student__age == 34, 'Где приватный атрибут __age?'
assert piter._Student__branch == "Information Security", 'Где приватный атрибут __branch?'
assert piter._Student__name == "Piter Parker", 'Где приватный атрибут __name?'
piter.access_private_method()
adam._Student__display_details()
piter._Student__display_details()
print('Все тесты пройдены успешно!')
