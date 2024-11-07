# Вспоминаем задачу про структуру LIFO
#
# Теперь научим его итерироваться. У вас имеется готовый код класса Stack (см. ниже в блоке кода).
# Обратите внимание на реализацию метода __iter__
#
# def __iter__(self):
#     return StackIterator(self)
# Значит класс Stack логику перебора элементов делегирует классу StackIterator. Ваша задача
# реализовать итератор в классе StackIterator, который обходит элементы стека сверху вниз
#
# Необходимо написать только реализацию класса StackIterator


class StackIterator:

    def __init__(self, stack):
        lst = stack.items.copy()
        self.iterable = lst[::-1]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        try:
            return self.iterable[self.index]
        except IndexError:
            self.index = -1
            raise StopIteration


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print("Empty Stack")
        else:
            return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            print("Empty Stack")
        else:
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __iter__(self):
        return StackIterator(self)


stack = Stack()

stack.push(100)
stack.push(True)
stack.push('hello')
stack.push('world')

# Используем итератор для обхода стека
for item in stack:
    print(item)

print(stack.items)
