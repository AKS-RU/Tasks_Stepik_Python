# Конструктор
# Создайте класс Constructor, в котором реализованы:
#
# Метод add_atribute , принимающий на вход название атрибута в виде строки и его значение. Задача метода add_atribute
# — создать или изменить атрибут экземпляра по переданному имени атрибута;
#
# Метод display ,  печатающий на экран словарь __dict__ у экземпляра.
# Необходимо написать только определение класса Constructor
#
# 🚀Подсказка🚀
# Sample Input 1:
#
# obj1 = Constructor()
# obj1.display()
# obj1.add_atribute('color', 'red')
# obj1.add_atribute('width', 20)
# obj1.display()
# Sample Output 1:
#
# {}
# {'color': 'red', 'width': 20}
# Sample Input 2:
#
# obj2 = Constructor()
# obj3 = Constructor()
#
# obj2.display()
# obj3.display()
#
# obj2.add_atribute('height', 100)
#
# obj3.add_atribute('a', 100)
# obj3.add_atribute('b', 300)
# obj3.add_atribute('c', 200)
# obj3.add_atribute('b', 1)
#
# obj2.display()
# obj3.display()
# Sample Output 2:
#
# {}
# {}
# {'height': 100}
# {'a': 100, 'b': 1, 'c': 200}

from typing import Any


class Constructor:

    def add_atribute(self, name_attr: str, value: Any):
        setattr(self, name_attr, value)

    def display(self):
        print(self.__dict__)
        return self.__dict__


if __name__ == '__main__':
    obj2 = Constructor()
    obj3 = Constructor()

    assert obj2.display() == {}
    assert obj3.display() == {}

    obj2.add_atribute('height', 100)

    obj3.add_atribute('a', 100)
    obj3.add_atribute('b', 300)
    obj3.add_atribute('c', 200)
    obj3.add_atribute('b', 1)

    assert obj2.display() == {'height': 100}
    assert obj3.display() == {'a': 100, 'b': 1, 'c': 200}
    print('Все тесты пройдены!')
