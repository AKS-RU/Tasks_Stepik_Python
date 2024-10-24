# Создайте класс Robot, у которого есть:
#
# атрибут класса population. В этом атрибуте будет храниться общее количество роботов, изначально принимает значение 0;
#
# конструктор __init__, принимающий 1 аргумент name. Данный метод должен сохранять атрибут name и печатать сообщение
# вида "Робот <name> был создан". Помимо инициализации робота данный метод должен увеличивать популяцию роботов
# на единицу;
#
# метод destroy, должен уменьшать популяцию роботов на единицу и печатать сообщение вида "Робот <name> был уничтожен"
#
# метод say_hello, который печатает сообщение вида "Робот <name> приветствует тебя, особь человеческого рода"
#
# метод класса  how_many, который печатает сообщение вида "<population>, вот сколько нас еще осталось"


class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print(f'Робот {self.name} был создан')
        Robot.population += 1

    def destroy(self):
        Robot.population -= 1
        print(f'Робот {self.name} был уничтожен')

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')

    @classmethod
    def how_many(cls):
        print(f'{cls.population}, вот сколько нас еще осталось')


print('*' * 15, 'ТЕСТЫ', '*' * 15)

droid1 = Robot("R2-D2")
assert droid1.name == 'R2-D2'
assert Robot.population == 1
droid1.say_hello()
Robot.how_many()
droid2 = Robot("C-3PO")
assert droid2.name == 'C-3PO'
assert Robot.population == 2
droid2.say_hello()
Robot.how_many()
droid1.destroy()
assert Robot.population == 1
droid2.destroy()
assert Robot.population == 0
Robot.how_many()

print('Все тесты пройдены успешно!')
