# Определите функцию print_to, которая принимает одно натуральное число n и распечатывает на экране последовательность
# целых чисел от 1 до n включительно. Каждое число необходимо выводить на отдельной строке.
#
# Ваша задача только написать определение функции print_to
#
# Sample Input 1:
#
# print_to(5)
# Sample Output 1:
#
# 1
# 2
# 3
# 4
# 5
# Sample Input 2:
#
# print_to(3)
# Sample Output 2:
#
# 1
# 2
# 3
# Sample Input 3:
#
# print_to(1)
# Sample Output 3:
#
# 1


def print_to(n: int):
    if n>=1:
        print_to(n-1)
        print(n)

print_to(4)