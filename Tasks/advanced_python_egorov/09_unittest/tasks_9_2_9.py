# Перед вами функция divide_numbers

# def divide_numbers(a, b):
#     if b == 0:
#         raise ValueError("Division by zero is not allowed")
#     elif a < 0 or b < 0:
#         raise ValueError("Both numbers must be non-negative")
#     elif a % b != 0:
#         raise ValueError("Numbers must be divisible without remainder")
#     else:
#         return a // b
# Ваша задача определить все возможные варианты входных значений для данной функции и для
# каждого варианта написать тестовый случай
import unittest


def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    elif a < 0 or b < 0:
        raise ValueError("Both numbers must be non-negative")
    elif a % b != 0:
        raise ValueError("Numbers must be divisible without remainder")
    else:
        return a // b


class TestDivideNumbers(unittest.TestCase):

    def test_01(self):
        self.assertEqual(divide_numbers(10, 2), 5)

    def test_02(self):
        with self.assertRaisesRegex(ValueError, 'Division by zero is not allowed'):
            divide_numbers(5, 0)

    def test_03(self):
        with self.assertRaisesRegex(ValueError, 'Both numbers must be non-negative'):
            divide_numbers(-3, 2)

    def test_04(self):
        with self.assertRaisesRegex(ValueError, 'Both numbers must be non-negative'):
            divide_numbers(-10, -2)

    def test_05(self):
        with self.assertRaisesRegex(ValueError, 'Both numbers must be non-negative'):
            divide_numbers(10, -2)

    def test_06(self):
        with self.assertRaisesRegex(ValueError, 'Numbers must be divisible without remainder'):
            divide_numbers(7, 3)

    def test_07(self):
        with self.assertRaisesRegex(ValueError, 'Numbers must be divisible without remainder'):
            divide_numbers(3, 12)


if __name__ == '__main__':
    unittest.main()
