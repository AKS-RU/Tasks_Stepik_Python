# Вашей программе будут поступать на вход N списков, содержащих целые числа
#
# Для каждого введенного списка определите, сколько в нем встречается различных чисел.
#
# Входные данные
#
# Сперва поступает натуральное число N - количество списков
#
# В следующих N строк вводятся значения каждого списка, разделенные через пробел
#
# Выходные данные
#
# Вывести на отдельной строке количество различных чисел каждого введенного списка в том же порядке,
# в котором вводились списки
#
# Sample Input 1:
#
# 2
# 1 2 3 2 1
# 2 2 2 2 2 2
# Sample Output 1:
#
# 3
# 1
# Sample Input 2:
#
# 5
# 1
# 1 2 3
# 1 2 3 4 4 4 3 4 1 2
# 123 1000 800 123
# 98 832 32 4 343 242 42 432
# Sample Output 2:
#
# 1
# 3
# 4
# 3
# 8
# Sample Input 3:
#
# 6
# 4 3 534 2 3
# 3 4 42 3 4 32 3
# 4 4 4 4 4
# 32 43 2 432 5 32 32
# 43 53 32 5 465 7 86 532 4324 64
# 32 54 353 5 4324 234 5535  53 453 321
# Sample Output 3:
#
# 4
# 4
# 1
# 5
# 10
# 10

# print(*(len(set(map(int,input().split()))) for _ in range(int(input()))), sep='\n')
for i in range(int(input())):
    print(len(set(map(int,input().split()))))
    # print(len(c))

