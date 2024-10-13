# Определите функцию print_histogram, которая принимает список целых чисел и выводит гистограмму на экран.
#
# Например, вызов
#
# print_histogram([4, 9, 6])
#
# должен вывести на экран следующее:
#
# ****
# *********
# ******
# Ваша задача написать только определение функции print_histogram
#
# Sample Input:
#
# print_histogram([4, 9, 7])
# Sample Output:
#
# ****
# *********
# *******

def print_histogram(lst: list):
    for i in lst:
        print('*'*i)

print_histogram([4, 9, 7])