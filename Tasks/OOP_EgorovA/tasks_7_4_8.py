# Как же без Фибоначчи
# Создайте объект итератор FibonacciIterator, который умеет выдавать последовательность Фибоначчи
# из n чисел. Число n поступает при инициализации класса FibonacciIterator.
#
# Будем считать, что последовательность Фибоначчи следующая: 0, 1, 1, 2, 3, 5, 8, 13, 21 и т.д.
# Каждое следующее число получается суммой двух предыдущих.
#
# Пример использования
#
# fibonacci_iter = FibonacciIterator(7)
#
# for number in fibonacci_iter:
#     print(number)
#
# # Печатает
# 0
# 1
# 1
# 2
# 3
# 5
# 8


class FibonacciIterator:

    def __init__(self, border):
        self.border = border
        self.a = 0
        self.b = 1
        self.count = 0

    def __iter__(self):
        while self.count < self.border:
            yield self.a
            c = self.a + self.b
            self.count += 1
            self.a = self.b
            self.b = c

    def __next__(self):
        return self


fibonacci_iter = FibonacciIterator(7)

for number in fibonacci_iter:
    print(number)
