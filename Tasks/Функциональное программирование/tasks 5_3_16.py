# Напишите lambda функцию, которая принимает произвольное количество числовых аргументов и выводит их
# среднее арифметическое.
# Для проверки решения присвойте вашу lambda функцию переменной average.
#
# Вводить и выводить ничего не нужно, только определить переменную average
#
# Sample Input 1:
#
# print(average.__name__)
# print(average(4, 5, 6))
# Sample Output 1:
#
# <lambda>
# 5.0
# Sample Input 2:
#
# print(average(2, 6))
# print(average.__name__)
# Sample Output 2:
#
# 4.0
# <lambda>
# Sample Input 3:
#
# print(average(10, 6, 5, 4, 3, 7, 9, 15))
# Sample Output 3:
#
# 7.375


average = lambda *args: sum(args)/len(args)


print(average(10, 6, 5, 4, 3, 7, 9, 15))