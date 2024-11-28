# Интерфейс стека
# В этом задании создайте реализацию стека при помощи обычного списка в python

# Нам понадобятся сперва создать свое собственное исключение EmptyStackError

# Интерфейс вашего класса Stack должен выглядеть так:

# метод .push(item) добавляет новый элемент на вершину стека

# метод .pop() удаляет элемент с вершины стека возвращает его. При попытке удалить элемент из
# стека нужно возбуждать исключение EmptyStackError

# метод .peek()  возвращает элемент, находящийся на вершине стека, без его удаления. Это позволяет
# просмотреть элемент, который будет удален следующим.

# метод .is_empty()  возвращает True,  если стек пустой, в противном случае вернет False

# свойство .size возвращает количество элементов, находящихся в стеке на данный момент.

# Реализуйте класс Stack с описанным интерфейсом и исключение EmptyStackError


class EmptyStackError(Exception):
    pass


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.insert(0, item)

    def pop(self):
        if self.stack:
            return self.stack.pop(0)
        raise EmptyStackError

    def peek(self):
        return self.stack[0]

    def is_empty(self):
        return not bool(self.stack)

    @property
    def size(self):
        return len(self.stack)


# Проверки стека
my_stack = Stack()
assert my_stack.size == 0
assert my_stack.is_empty()
my_stack.push('A')
my_stack.push('W')
my_stack.push('M')
assert my_stack.size == 3
assert not my_stack.is_empty()
assert my_stack.pop() == 'M'

assert my_stack.peek() == 'W'
assert my_stack.pop() == 'W'

assert my_stack.peek() == 'A'
my_stack.push('hello')
assert my_stack.size == 2

assert my_stack.pop() == 'hello'
assert my_stack.pop() == 'A'
assert my_stack.is_empty()

try:
    my_stack.pop()
except EmptyStackError:
    print('OK')
