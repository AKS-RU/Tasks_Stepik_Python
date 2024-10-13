# Декоратор uppercase_elements
# Ваша задача написать логику работы декоратора uppercase_elements, который умеет работать с функциями, возвращающими
# коллекции элементов. Задача декоратора uppercase_elements преобразовать каждый строковый элемент коллекции к заглавному
# регистру. В случае, если оригинальная функция возвращает словарь, то элементом считаем только строковые ключи словаря.
#
# Элементы, не являющиеся строкой, не должны изменяться декоратором uppercase_elements
#
# Гарантируется, что коллекции, возвращаемые оригинальной функцией, не являются вложенными
#
# Sample Input 1:
#
# @uppercase_elements
# def my_func():
#     return ['monarch', 'Touch', 'officiaL', 'DangerouS', 'breathe']
#
# print(my_func())
# Sample Output 1:
#
# ['MONARCH', 'TOUCH', 'OFFICIAL', 'DANGEROUS', 'BREATHE']
# Sample Input 2:
#
# @uppercase_elements
# def my_func(name, surname):
#     return ['temple', 'store', name, surname, *[1, 2, 3]]
#
# print(my_func('Gerard', 'Pique'))
# Sample Output 2:
#
# ['TEMPLE', 'STORE', 'GERARD', 'PIQUE', 1, 2, 3]
# Sample Input 3:
#
# @uppercase_elements
# def my_func(**kwargs):
#     return {1: 'one', 2: 'store', 'three': 3, 'four': 4} | kwargs
#
# print(my_func(**{'Five': 5, 'sIx': 6}))
# Sample Output 3:
#
# {1: 'one', 2: 'store', 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6}

def uppercase_elements(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return type_definition(res)

    def type_definition(res):
        if isinstance(res, list):
            return create_list(res)
        elif isinstance(res, tuple):
            return create_tuple(res)
        elif isinstance(res, set):
            return create_set(res)
        elif isinstance(res, dict):
            return create_dict(res)

    def create_list(res):
        lst = [i.upper() if isinstance(i, str) else i for i in res]
        return lst

    def create_tuple(res):
        lst = [i.upper() if isinstance(i, str) else i for i in res]
        return tuple(lst)

    def create_set(res):
        lst = [i.upper() if isinstance(i, str) else i for i in res]
        return set(lst)

    def create_dict(res):
        dict_res = {}
        dict_res = {k.upper() if isinstance(k, str) else k: v for k, v in res.items()}
        return dict_res

    return wrapper


@uppercase_elements
def my_func(**kwargs):
    return {1: 'one', 2: 'store', 'three': 3, 'four': 4} | kwargs


print(my_func(**{'Five': 5, 'sIx': 6}))

# print(isinstance(my_func(), list))
