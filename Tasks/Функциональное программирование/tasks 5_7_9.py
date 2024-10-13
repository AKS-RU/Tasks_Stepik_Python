# Фильтрация - 2
# На основании предыдущей функции filter_list, напишем новую функцию filter_collection. Особенность функции
# filter_collection заключается в том, что она возвращает тот же тип коллекции, который она принимала на вход.
#
# А остальной принцип  ее работы похож с функцией filter_list: обе принимают функцию f для проверки, при
# помощи которой фильтруются элементы коллекции
#
# Функция f обязательно должна проверять определенное условие и возвращать булев тип.
#
# Sample Input 1:
#
# def is_even(num):
#     return num % 2 == 0
#
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# even_numbers = filter_collection(is_even, numbers)
# print(even_numbers)
# Sample Output 1:
#
# (2, 4, 6, 8, 10)
# Sample Input 2:
#
# def is_positive(num):
#     return num > 0
#
# numbers = [-1, 2, -3, 4, 5, -6, 7, -8, -9, 10]
# positive_numbers = filter_collection(is_positive, numbers)
# print(positive_numbers)
# Sample Output 2:
#
# [2, 4, 5, 7, 10]
# Sample Input 3:
#
# print(filter_collection(lambda x: x not in 'aeiou', 'I never heard those lyrics before'))
# Sample Output 3:
#
# I nvr hrd ths lyrcs bfr


def filter_collection(func, data):
    def data_type():
        nonlocal result
        if isinstance(data, str):
            return ''.join(result)
        else:
            return type(data)(result)
    result =[i for i in data if func(i)]
    return data_type()

def is_even(num):
    return num % 2 == 0

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_numbers = filter_collection(is_even, numbers)
print(even_numbers)