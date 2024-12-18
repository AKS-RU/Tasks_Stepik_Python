# Создайте класс Person, у которого есть:
#
# конструктор __init__, принимающий 3 аргумента: name, surname, gender. Атрибут gender может принимать только
# 2 значения: «male» и «female», по умолчанию «male». Если в атрибут gender передается любое другое значение,
# печатать сообщение: «Не знаю, что вы имели в виду? Пусть это будет мальчик!» и
# проставить в атрибут gender значение «male»;
#
# переопределить метод __str__ следующим образом:
# если объект - мужчина (атрибут gender = «male»), возвращать строку «Гражданин <Фамилия> <Имя>»
# если объект - женщина (атрибут gender = «female»), возвращать строку «Гражданка <Фамилия> <Имя>»
# p1 = Person('Chuck', 'Norris')
# print(p1) # печатает "Гражданин Norris Chuck"
# p2 = Person('Mila', 'Kunis', 'female')
# print(p2) # печатает "Гражданка Kunis Mila"
# p3 = Person('Оби-Ван', 'Кеноби', True)# печатает "Не знаю, что вы имели в виду? Пусть это будет мальчик!"
# print(p3) # печатает "Гражданин Кеноби Оби-Ван"


class Person:

    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender in ('male', 'female'):
            self.gender = gender
        else:
            print('Не знаю, что вы имели в виду? Пусть это будет мальчик!')
            self.gender = 'male'

    def __str__(self):
        if self.gender in 'male':
            return f'Гражданин {self.surname} {self.name}'
        return f'Гражданка {self.surname} {self.name}'


p = Person('Mila', 'Kunis', 'female')
print(p.name)
print(p.surname)
print(p.gender)
print(p)
