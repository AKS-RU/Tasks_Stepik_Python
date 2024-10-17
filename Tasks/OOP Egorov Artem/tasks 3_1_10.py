# Hello Robot - 2
#  предыдущей задаче вы могли обратить внимание на то, что выводится всегда одно и то же имя робота в методе say_hello . Давайте это исправим при помощи атрибута экземпляра name . Для этого переопределяем класс Robot, в котором должны быть реализованы:
#
# Метод set_name, принимающий имя робота и сохраняющий его в атрибуте экземпляра name
#
# Метод say_hello. Метод должен проверить, есть ли у ЭК атрибут name . Если атрибут name  присутствует, необходимо напечатать фразу «Hello, human! My name is <name>». Если атрибут name  отсутствует у экземпляра, печатайте сообщение «У робота нет имени»
#
# Метод say_bye,  печатающий на экран фразу «See u later alligator»
# Необходимо написать только определение класса Robot.
#
# 🚀Подсказка🚀
# Sample Input 1:
#
# c3po = Robot()
# c3po.say_hello()
# c3po.set_name('R2D2')
# c3po.say_hello()
# c3po.say_bye()
# Sample Output 1:
#
# У робота нет имени
# Hello, human! My name is R2D2
# See u later alligator
# Sample Input 2:
#
# r = Robot()
# r.set_name('Chappy')
# r.say_hello()
#
# d = Robot()
# d.set_name('Dendy')
# d.say_hello()
# Sample Output 2:
#
# Hello, human! My name is Chappy
# Hello, human! My name is Dendy
# Sample Input 3:
#
# d = Robot()
# d.say_hello()
# d.set_name('Wally')
# d.say_hello()
# d.say_bye()
# Sample Output 3:
#
# У робота нет имени
# Hello, human! My name is Wally
# See u later alligator


class Robot:

    def say_hello(self):
        if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')
        else:
            print('У робота нет имени')

    def say_bye(self):
        print('See u later alligator')

    def set_name(self, name):
        self.name = name


if __name__ == '__main__':
    d = Robot()
    assert d.say_hello() == print('У робота нет имени')
    d.set_name('Wally')
    assert d.say_hello() == print('Hello, human! My name is Wally')
    assert d.say_bye() == print('See u later alligator')
    print('Успешно!')
