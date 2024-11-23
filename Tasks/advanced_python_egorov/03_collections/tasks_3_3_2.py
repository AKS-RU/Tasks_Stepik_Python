# Создайте класс StringDeque, унаследованный отUserString и предоставляющий дополнительно методы для
# добавления символов в начало строки и в конец. Для этого реализуйте методы:
#
# appendleft(symbol) принимает один строчный символ и добавляет его в начало строки
#
# append(symbol) принимает один строчный символ и добавляет его в конец строки
# Оба метода должны изменять состояние строки и ничего не возвращать
#
# Если на вход методам поступает строка, состоящая из не одного символа, вызывайте
# исключение ValueError. Также ValueError нужно вызывать в случае, если в данные
# методы передавать не строку


from collections import UserString


class StringDeque(UserString):

    def is_valid_symbol(self, symbol):
        if isinstance(symbol, str) and len(symbol) == 1:
            return True
        raise ValueError

    def appendleft(self, symbol):
        if self.is_valid_symbol(symbol):
            self.data = symbol + self.data

    def append(self, symbol):
        if self.is_valid_symbol(symbol):
            self.data = self.data + symbol


deque = StringDeque("abc")

assert type(deque) == StringDeque
deque.appendleft("d")
assert deque.data == 'dabc'
deque.append("e")
assert deque.data == 'dabce'

try:
    deque.append(123)
except ValueError:
    pass

try:
    deque.append('hello')
except ValueError:
    pass

try:
    deque.append('')
except ValueError:
    pass

try:
    deque.appendleft([1])
except ValueError:
    pass

try:
    deque.appendleft('hi')
except ValueError:
    pass

print('OK')
