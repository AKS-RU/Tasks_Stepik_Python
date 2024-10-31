#                                        Задача «Корзина»
#
#
#                                             Часть 2
# С предыдущего урока у вас должен быть создан класс  File, у которого имеются:
#
# метод __init__;
#
# метод  restore_from_trash;
#
# метод  remove;
#
# метод read;
#
# метод write.
# Далее создайте класс  Trash, у которого есть:
#
# атрибут класса  content , изначально равный пустому списку
#
# статик-метод  add, который принимает файл и сохраняет его в корзину: для этого нужно добавить его в атрибут content и
# проставить файлу в атрибут in_trash значение True. Если в метод add передается
# не экземпляр класса File, необходимо вывести сообщение
# В корзину можно добавлять только файл
# статик-метод  clear, который запускает процесс очистки файлов в корзине. Необходимо для всех файлов, хранящихся в
# атрибуте content , в порядке их добавления в корзину вызвать метод файла remove.
# Атрибут content  после очистки должен стать пустым списком. Сама процедура очистки должна начинаться фразой
# Очищаем корзину
# и заканчиваться фразой
# Корзина пуста
# статик-метод  restore, который запускает процесс восстановления файлов из корзины. Необходимо для всех файлов,
# хранящихся в атрибуте content , в порядке их добавления в корзину вызвать метод файла restore_from_trash.
# Атрибут content  после очистки должен стать пустым списком. Сама процедура восстановления должна начинаться фразой
# Восстанавливаем файлы из корзины
# и заканчиваться фразой
# Корзина пуста


class File:

    def __init__(self, name_file):
        self.name = name_file
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            return print(f'ErrorReadFileDeleted({self.name})')
        elif self.in_trash:
            return print(f'ErrorReadFileTrashed({self.name})')
        print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted:
            return print(f'ErrorWriteFileDeleted({self.name})')
        elif self.in_trash:
            return print(f'ErrorWriteFileTrashed({self.name})')
        print(f'Записали значение {content} в файл {self.name}')


class Trash:
    content = []

    @staticmethod
    def add(file):
        if not isinstance(file, File):
            return print('В корзину можно добавлять только файл')
        Trash.content.append(file)
        file.in_trash = True

    @staticmethod
    def clear():
        print('Очищаем корзину')
        while len(Trash.content):
            Trash.content.pop(0).remove()
        print('Корзина пуста')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        while len(Trash.content):
            Trash.content.pop(0).restore_from_trash()
        print('Корзина пуста')


print('*' * 15, 'ТЕСТЫ', '*' * 15)

f1 = File('puppies.jpg')
f2 = File('cat.jpg')
f3 = File('xxx.doc')
passwords = File('pass.txt')

for file in [f1, f2, f3, passwords]:
    assert file.is_deleted is False
    assert file.in_trash is False

f3.read()
f3.remove()
assert f3.is_deleted is True
f3.read()
f3.write('hello')

assert Trash.content == []

Trash.add(f2)
Trash.add(passwords)
Trash.add(f3)

f1.read()
Trash.add(f1)
f1.read()

for file in [f1, f2, f3, passwords]:
    assert file.in_trash is True

for f in [f2, passwords, f3, f1]:
    assert f in Trash.content

Trash.restore()
assert Trash.content == [], 'После восстановления корзина должна была очиститься'

Trash.add(passwords)
Trash.add(f2)
Trash.add('hello')
Trash.add(f1)

for f in [passwords, f2, f1]:
    assert f in Trash.content

Trash.clear()

for file in [passwords, f2, f1]:
    assert file.is_deleted is True

assert Trash.content == [], 'После удаления файлов корзина должна была очиститься'

f1.read()

print('Все тесты пройдены успешно!')
