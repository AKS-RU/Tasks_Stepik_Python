# Тестируем класс
# Перед вами класс Book

# class Book:
#     def __init__(self, title, author, pages, price):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.price = price

#     def __str__(self):
#         return f"{self.title} by {self.author}"

#     def get_reading_time(self):
#         return f"{self.pages * 1.5} minutes"

#     def apply_discount(self, discount):
#         if not isinstance(discount, float):
#             raise ValueError('Discount must be float number')
#         if 0 <= discount <= 1:
#             discounted_price = self.price - (discount * self.price)
#             return f"${discounted_price}"
#         raise ValueError('Discount must be float number between 0 and 1')
# Ваша задача написать случай для каждого метода класса Book

# Ваша задача написать тестовые кейсы для каждого метода класса Book .
# Оформить их необходимо внутри класса TestBookClass. Я заранее приготовил вам названия для
# тестовых случаев, но вы можете воспользоваться своими.


# Внутри класса TestBookClass необходимо только описать тестовые случае, больше в этом
# задании ничего не требуется. Запуск тестов выполниться автоматически

# Для тестирования вы можете создать экземпляры класса Book внутри тестовых методов


import unittest


class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_reading_time(self):
        return f"{self.pages * 1.5} minutes"

    def apply_discount(self, discount):
        if not isinstance(discount, float):
            raise ValueError('Discount must be float number')
        if 0 <= discount <= 1:
            discounted_price = self.price - (discount * self.price)
            return f"${discounted_price}"
        raise ValueError('Discount must be float number between 0 and 1')


class TestBookClass(unittest.TestCase):

    def setUp(self):
        self.book_test = Book('Война и мир', 'Л. Толстой', 2144, 150)

    def test_init_method(self):
        self.assertEqual(self.book_test.title,  'Война и мир')
        self.assertEqual(self.book_test.author,  'Л. Толстой')
        self.assertEqual(self.book_test.pages,  2144)
        self.assertEqual(self.book_test.price,  150)

    def test__str__method(self):
        self.assertEqual(str(self.book_test), "Война и мир by Л. Толстой")

    def test_get_reading_time(self):
        self.assertEqual(self.book_test.get_reading_time(), f"3216.0 minutes")

    def test_apply_discount_not_float(self):
        with self.assertRaisesRegex(ValueError, 'Discount must be float number'):
            self.book_test.apply_discount(12)

    def test_apply_discount_more_than_1(self):
        with self.assertRaisesRegex(ValueError, 'Discount must be float number between 0 and 1'):
            self.book_test.apply_discount(-0.5)

    def test_apply_discount_less_than_0(self):
        with self.assertRaisesRegex(ValueError, 'Discount must be float number between 0 and 1'):
            self.book_test.apply_discount(1.1)

    def test_apply_discount_good_case(self):
        self.assertEqual(self.book_test.apply_discount(0.1), '$135.0')


if __name__ == '__main__':
    unittest.main()
