# Напишите рекурсивную функцию summa, которая будет суммировать все числа от 1 до N. Число N поступает внутрь функции в
# качестве аргумента
#
# Sample Input 1:
#
# print(summa(4))
# Sample Output 1:
#
# 10
# Sample Input 2:
#
# print(summa(10))
# Sample Output 2:
#
# 55
# Sample Input 3:
#
# print(summa(34))
# Sample Output 3:
#
# 595



def summa(n: int)-> int:
    if n==1:
        return 1
    return summa(n-1)+n


print(summa(34))