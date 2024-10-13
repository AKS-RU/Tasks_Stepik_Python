# Ваша задача - написать рекурсивную функцию tribonacci, которая принимает на вход целое число n - порядковый номер
# чисел Трибоначчи. Функция по параметру n должна вычислить и вернуть значение, стоящее на n-м месте в ряде чисел
# Трибоначчи
#
#
#
# Ваша задача только написать определение функции tribonacci
#
# Sample Input 1:
#
# print(tribonacci(1))
# Sample Output 1:
#
# 0
# Sample Input 2:
#
# print(tribonacci(8))
# Sample Output 2:
#
# 24
# Sample Input 3:
#
# print(tribonacci(9))
# Sample Output 3:
#
# 44
# Sample Input 4:
#
# print(tribonacci(10))
# Sample Output 4:
#
# 81


def tribonacci(n):
    if n in (0, 1):
        return 0
    if n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


print(tribonacci(9))
