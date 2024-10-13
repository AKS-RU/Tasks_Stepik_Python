# Определите функцию overlapping, которая принимает два списка и возвращает True, если у них есть хотя бы один общий
# элемент, в противном случае — False.
#
# ВЫ можете решать задачу удобным для вас способом, но попробуйте реализовать с использованием функции is_member из
# предыдущего шага.
#
# Sample Input 1:
#
# print(overlapping(['nope', 'nothing', 'in'], ['common']))
# Sample Output 1:
#
# False
# Sample Input 2:
#
# print(overlapping(['this', 'might', 'work'], ['or', 'maybe', 'this']))
# Sample Output 2:
#
# True
# Sample Input 3:
#
# print(overlapping(['I', 'think', 'I am', 19], ['19', 'bananas']))
# Sample Output 3:
#
# False
#
def is_member(st: str, lst: list):
    return st in lst


def overlapping(lst_1: list, lst_2: list):
    if len(lst_2) < len(lst_1):
        lst_t = lst_1[::]
        lst_1 = lst_2[::]
        lst_2 = lst_t[::]
    return any(map(lambda x: is_member(x,lst_2), lst_1))


print(overlapping(['this', 'might', 'work'], ['or', 'maybe', 'this']))
