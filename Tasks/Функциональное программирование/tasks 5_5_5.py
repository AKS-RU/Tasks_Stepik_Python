# Напишите функцию create_attrs, которая принимает объект obj и список кортежей. Каждый кортеж состоит из пары
# значений: имя атрибута в виде строки и его будущее значение.
#
# Задача функции create_attrs — создать на основании внутренних кортежей списка новые атрибуты к переданному объекту.
#
# Для проверки работоспособности программы скопируйте реализацию функции check_exist_attrs из предыдущего задания
#
# Sample Input 1:
#
# def print_goods(lst):
#     pass
#
# create_attrs(print_goods, [('house', 1), ('level', 3), ('cost', 1000000)])
# print(print_goods.house)
# print(print_goods.level)
# print(print_goods.cost)
# Sample Output 1:
#
# 1
# 3
# 1000000
# Sample Input 2:
#
# def print_goods(lst):
#     pass
#
# create_attrs(print_goods, [('is_working', False), ('days', 10), ('status', 'Not ready')])
#
# print(check_exist_attrs(print_goods, ['sort', 'is_working', 'days', 'status', 'upper']))
# Sample Output 2:
#
# {'sort': False, 'is_working': True, 'days': True, 'status': True, 'upper': False}


def check_exist_attrs(func, lst: list):
    return {i:hasattr(func, i) for i in lst}

def create_attrs(func, lst: list[tuple[str,int]]):
    for i, j in lst:
        setattr(func,i,j)


def print_goods(lst):
    pass

create_attrs(print_goods, [('is_working', False), ('days', 10), ('status', 'Not ready')])

print(check_exist_attrs(print_goods, ['sort', 'is_working', 'days', 'status', 'upper']))

