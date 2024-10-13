# Напишите функцию count_args, которая принимает произвольное количество аргументов. Данная функция должна
#
# возвращать количество переданных ей на вход аргументов
#
# Вам необходимо написать только определение функции count_args
#
# Sample Input 1:
#
# print(count_args(1, 2, 3, 4, 5))
# Sample Output 1:
#
# 5
# Sample Input 2:
#
# print(count_args())
# Sample Output 2:
#
# 0
# Sample Input 3:
#
# print(count_args(1, 2, 3))
# Sample Output 3:
#
# 3


def count_args(*args):
    return len(args)

print(count_args(1, 2, 3, 4, 5))