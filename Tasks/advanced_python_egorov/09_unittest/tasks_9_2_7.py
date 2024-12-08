# Обычно функция, для которой пишут тесты, определена совершенно в другом модуле. В файлике, где
# выполняется тестирование, импортируют модуль и обращаются к интересующей функции.

# Давайте потренируемся так делать. В вашем распоряжении будет модуль check_list.py, в котором
# находятся две функции is_sorted_ascending и is_sorted_descending

# def is_sorted_ascending(lst: list) -> bool:
#     return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))


# def is_sorted_descending(lst: list) -> bool:
#     return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))
# Данные функции проверяют отсортирован ли переданный список, состоящий из чисел, в порядке
# возрастания или убывания соответственно

# Ваша задача написать как минимум по два тестовых кейса для каждой функции из модуля
# check_list.py внутри класса CheckListTestCase

import unittest
from check_list import is_sorted_ascending, is_sorted_descending


class CheckListTestCase(unittest.TestCase):

    def test_01(self):
        lst_ = [1, 4, 3, 6, 7, 8, 2]
        lst_.sort()
        self.assertTrue(is_sorted_ascending(lst_))

    def test_02(self):
        lst_ = [1, 10, 3, 34, 7, 12, 3, 0]
        self.assertFalse(is_sorted_ascending(lst_))

    def test_03(self):
        lst_ = [1, 4, 3, 6, 7, 8, 2]
        lst_.sort(reverse=True)
        self.assertTrue(is_sorted_descending(lst_))

    def test_04(self):
        lst_ = [1, 10, 3, 34, 7, 12, 0]
        self.assertFalse(is_sorted_descending(lst_))


unittest.main()
