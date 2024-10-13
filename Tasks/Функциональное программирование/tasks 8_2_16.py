# Числа Фибоначчи
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где число, стоящее на n-ой
# позиции можно вычислить по формуле:
#
#
#
# Требуется найти N-е число Фибоначчи при помощи рекурсивной функции fibonacci
#
# Функция должна принимать порядковый номер N и возвращать N-ое число Фибоначчи
#
# Ваша задача только написать определение функции fibonacci
#
# Sample Input 1:
#
# print(fibonacci(7))
# Sample Output 1:
#
# 13
# Sample Input 2:
#
# print(fibonacci(10))
# Sample Output 2:
#
# 55




def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))