# Реализуйте класс Numbers, который предназначен для хранения произвольного количества чисел.
# Данный класс должен содержать:
#
# метод __init__, принимающий произвольное количество чисел и сохраняющий их внутри экземпляра;
#
# метод add_number, которой принимает числовое значение и добавляет его в конец коллекции экземпляра;
#
# метод get_positive, который возвращает список всех положительных чисел из коллекции экземпляра;
#
# метод get_negative, который возвращает список всех отрицательных чисел из коллекции экземпляра;
#
# метод get_zeroes,  который возвращает список всех нулевых значений из коллекции экземпляра.


class Numbers:
    def __init__(self, *args):
        self.lst = list(args)

    def add_number(self, value):
        self.lst.append(value)

    def get_positive(self):
        return list(filter(lambda x: x > 0, self.lst))

    def get_negative(self):
        return list(filter(lambda x: x < 0, self.lst))

    def get_zeroes(self):
        return list(filter(lambda x: x == 0, self.lst))


nums = Numbers(10, 20, 30, 0, 0, 5)

assert nums.get_positive() == [10, 20, 30, 5]
assert nums.get_zeroes() == [0, 0]
nums.add_number(100)
nums.add_number(0)
nums.add_number(-77)
assert nums.get_positive() == [10, 20, 30, 5, 100]
assert nums.get_negative() == [-77]
assert nums.get_zeroes() == [0, 0, 0]

nums1 = Numbers()
assert nums1.get_positive() == []
assert nums1.get_negative() == []
assert nums1.get_zeroes() == []

nums1.add_number(5)
nums1.add_number(3)
nums1.add_number(4)

assert nums1.get_positive() == [5, 3, 4]
assert nums1.get_negative() == []
assert nums1.get_zeroes() == []

print('Все тесты пройдены успешно!')
