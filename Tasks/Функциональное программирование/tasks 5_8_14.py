# Ваша задача — создать функцию-замыкание create_dict. Функция create_dict должна сохранять в себе в виде словаря все
# значения, которые ей будут переданы. Ключами данного словаря должны быть натуральные числа, равные номеру вызова
# данной функции. Посмотрите пример ниже:
#
# f_1 = create_dict()
# print(f_1('hello')) # f_1 возвращает {1: 'hello'}
# print(f_1(100)) # f_1 возвращает {1: 'hello', 2: 100}
# print(f_1([1, 2, 3])) # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}
#
# f_2 = create_dict() # создаем новое замыкание в f_2
# print(f_2('PoweR')) # f_2 возвращает {1: 'PoweR'}
# Вызывая первый раз f_1 мы создали пару 1: 'hello', вызывая второй раз добавилась пара 2: 100. и т.д.
#
# При каждом вызове должен возвращаться словарь, хранящийся в замыкании
#
# Необходимо только определить функцию-замыкание create_dict, остальное мы сделаем за вас
#
# Sample Input:
#
# f_1 = create_dict()
# print(f_1('privet'))
# print(f_1('poka'))
# print(f_1([5, 2, 3]))
#
# f2 = create_dict()
# print(f2(5))
# print(f2(15))
# Sample Output:
#
# {1: 'privet'}
# {1: 'privet', 2: 'poka'}
# {1: 'privet', 2: 'poka', 3: [5, 2, 3]}
# {1: 5}
# {1: 5, 2: 15}


def create_dict():
    dct = {}
    cnt = 0
    def my_dict(value):
        nonlocal cnt
        cnt+=1
        dct.setdefault(cnt, value)
        return dct
    return my_dict


f_1 = create_dict()
print(f_1('privet'))
print(f_1('poka'))
print(f_1([5, 2, 3]))

f2 = create_dict()
print(f2(5))
print(f2(15))






f_1 = create_dict()
print(f_1('privet'))
print(f_1('poka'))
print(f_1([5, 2, 3]))

f2 = create_dict()
print(f2(5))
print(f2(15))




