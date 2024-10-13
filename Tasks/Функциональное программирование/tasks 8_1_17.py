# Определите функцию print_from, которая принимает одно натуральное число n и распечатывает на экране убывающую
# последовательность целых чисел от n до 1 включительно. Каждое число необходимо выводить на отдельной строке.
#
# Ваша задача только написать определение функции print_from
#
# Sample Input 1:
#
# print_from(4)
# Sample Output 1:
#
# 4
# 3
# 2
# 1
# Sample Input 2:
#
# print_from(7)
# Sample Output 2:
#
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Sample Input 3:
#
# print_from(2)
# Sample Output 3:
#
# 2
# 1


def print_from(n: int):
    if n>=1:
        print(n)
        print_from(n-1)

print_from(4)