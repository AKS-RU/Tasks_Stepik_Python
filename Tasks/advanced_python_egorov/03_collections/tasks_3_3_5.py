# Создайте класс MyList, унаследованный отUserList и предоставляющий дополнительно три
# следующих метода:
#
# .shift_left(), выполняющий сдвиг списка влево на один элемент. Под сдвигом влево понимается
# перенос первого элемента списка в конец. Изначальный список меняется, метод ничего не возвращает
#
# .shift_right(), выполняющий сдвиг списка вправо на один элемент. Под сдвигом вправо понимается
# перенос последнего элемента списка в начала. Изначальный список меняется, метод ничего не возвращает
#
# .for_each(function), вызывает переданную функцию function() для каждого элемента в базовом списке.
# Элементы должны обновится. Метод ничего не возвращает


from collections import UserList


# Напишите определение класса MyList
class MyList(UserList):

    def shift_left(self):
        self.data.append(self.data.pop(0))

    def shift_right(self):
        self.data.insert(0, self.data.pop())

    def for_each(self, func):
        self.data = [func(i) for i in self.data]


# Проверки для класса MyList

my_list = MyList([1, 2, 3, 4, 5])

assert my_list.data == [1, 2, 3, 4, 5]

my_list.shift_left()
assert my_list.data == [2, 3, 4, 5, 1]
my_list.shift_left()
my_list.shift_left()
assert my_list.data == [4, 5, 1, 2, 3]

my_list.shift_right()
assert my_list.data == [3, 4, 5, 1, 2]

my_list.for_each(lambda x: x ** 2)
assert my_list.data == [9, 16, 25, 1, 4]

print('OK')
