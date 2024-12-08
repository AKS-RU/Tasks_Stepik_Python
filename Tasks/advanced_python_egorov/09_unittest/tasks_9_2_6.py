# В вашем распоряжении имеется функция linear_search

# def linear_search(lst, target):
#     for i, element in enumerate(lst):
#         if element == target:
#             return i
#     return -1
# которая выполняет линейный поиск в списке

# Ваша задача написать как минимум два тестовых кейса внутри класса TestLinearSearchFunction
# ля функции linear_search.


# Внутри класса TestLinearSearchFunction необходимо только описать тестовые случае, больше в
# этом задании ничего не требуется. Запуск тестов выполнится автоматически

import unittest


def linear_search(lst, target):
    for i, element in enumerate(lst):
        if element == target:
            return i
    return -1


class TestLinearSearchFunction(unittest.TestCase):

    def test_01(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)
        self.assertNotEqual(linear_search([1, 2, 3, 4, 5], 4), 2)

    def test_02(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 4), 3)
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 1), 0)


unittest.main()
