# Ваша задача написать функцию find_duplicate, которая принимает один аргумент - список чисел. Функция должна
# возвращать список из дублей, каждый дубль нужно брать только один раз в том порядке, в котором они встречаются
# в исходном списке. Под дублем будем подразумевать число, которое присутствовало в списке несколько раз.
#
# find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) => [1, 2]
# find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) => [2, 1]
# find_duplicate([1, 2, 3, 4]) => []
# find_duplicate([1, 2, 3, 4, 3]) => [3]
# Ваша задача написать только определение функции find_duplicate

def find_duplicate(lst):
    res = []
    for i in lst:
        if i not in res and lst.count(i) > 1:
            res.append(i)
    return res

print(find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]))
