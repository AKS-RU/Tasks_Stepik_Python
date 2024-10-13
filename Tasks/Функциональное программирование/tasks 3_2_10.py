# Напишите функцию create_tuples, которая принимает два списка одинаковой длины и объединяет их в список кортежей.
#
# Элемент кортежа получается путем соединения элемента первого и второго списков, стоящих на одинаковых позициях
#
# Sample Input:
#
# print(create_tuples([1, 2, 3, 4], [5, 6, 7, 8]))
# Sample Output:
#
# [(1, 5), (2, 6), (3, 7), (4, 8)]

def create_tuples(lst_1: list, lst_2: list):
    return list(map(lambda x,y: (x,y), lst_1,lst_2))

print(create_tuples([1, 2, 3, 4], [5, 6, 7, 8]))