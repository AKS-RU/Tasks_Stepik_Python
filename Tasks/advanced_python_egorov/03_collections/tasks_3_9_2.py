# Интерфейс очереди
# Очередь (по-английски «queue») - это универсальная структура данных, которая может использоваться
# на любом языке программирования. В большинстве языков реализацию готовой очереди можно найти в
# стандартной библиотеке или можно ее реализовать самому. В этом задании мы выбираем последний
# вариант и реализуем свою собственную очередь на базе обычного питоновского списка.

# Интерфейс вашего класса Queue должен выглядеть так:

# метод .enqueue(item) добавляет новый элемент в конец очереди.

# метод .dequeue() удаляет элемент из начала очереди и возвращает его. Элемент, который был
# добавлен первым, будет удален первым. При попытке удалить элемент из пустой очереди нужно
# возбуждать исключение IndexError

# метод .peek()  возвращает элемент, находящийся в начале очереди, без его удаления. Это
# позволяет просмотреть элемент, который будет удален следующим.

# метод .is_empty()  проверяет, пуста ли очередь, и возвращает булевское значение (True или False).

# свойство .size возвращает количество элементов, находящихся в очереди в данный момент.

# Реализуйте класс Queue с описанным интерфейсом


class Queue():

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def is_empty(self):
        return not bool(self.queue)

    @property
    def size(self):
        return len(self.queue)


my_queue = Queue()
assert my_queue.size == 0
assert my_queue.is_empty()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
assert my_queue.size == 3
assert not my_queue.is_empty()
assert my_queue.dequeue() == 1

assert my_queue.peek() == 2
assert my_queue.dequeue() == 2

assert my_queue.peek() == 3
my_queue.enqueue('hello')
assert my_queue.size == 2

assert my_queue.dequeue() == 3
assert my_queue.dequeue() == 'hello'
assert my_queue.is_empty()

print('OK')
try:
    my_queue.dequeue()
except IndexError:
    pass
