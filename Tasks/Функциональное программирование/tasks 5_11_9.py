# Декоратор no_side_effects_decorator
# Напишите декоратор no_side_effects_decorator, который защищает от побочных действий функций
#
# Sample Input 1:
#
# @no_side_effects_decorator
# def add_element(data, element):
#     data.append(element)
#     return data
#
#
# my_list = [1, 2, 3]
# print('Результат вызова =', add_element(my_list, 4))
# print('Результат вызова =', add_element(my_list, 5))
# print(my_list)
# print(add_element.__name__)
# Sample Output 1:
#
# Результат вызова = [1, 2, 3, 4]
# Результат вызова = [1, 2, 3, 5]
# [1, 2, 3]
# add_element
# Sample Input 2:
#
# @no_side_effects_decorator
# def add_element(data, key, value=None):
#     data[key] = value
#     return data
#
#
# my_dict = {1: 'Hello', 2: 'World'}
# print('Результат вызова =', add_element(my_dict, 3))
# print('Результат вызова =', add_element(my_dict, 4, 'four'))
# print(my_dict)
# print(add_element.__name__)
# Sample Output 2:
#
# Результат вызова = {1: 'Hello', 2: 'World', 3: None}
# Результат вызова = {1: 'Hello', 2: 'World', 4: 'four'}
# {1: 'Hello', 2: 'World'}
# add_element


from functools import wraps

def no_side_effects_decorator(func):
    @wraps(func)
    def inner_no_effect(*args, **kwargs):
        lst=args[0].copy()
        param = args[1:]
        return func(lst,*param, **kwargs)
    return inner_no_effect


@no_side_effects_decorator
def add_element(data, key, value=None):
    data[key] = value
    return data


my_dict = {1: 'Hello', 2: 'World'}
print('Результат вызова =', add_element(my_dict, 3))
print('Результат вызова =', add_element(my_dict, 4, 'four'))
print(my_dict)
print(add_element.__name__)

