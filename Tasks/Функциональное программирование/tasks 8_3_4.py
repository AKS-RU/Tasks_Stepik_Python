# Возведение в степень
# Перед вами функция power, которая при помощи итерации возводит параметр a в степень n
#
# def power(a: int, n: int) -> int:
#     total = 1
#     for i in range(n):
#         total *= a
#     return total
# Перепишите реализацию функции power с итерации на рекурсию. Названии функции и параметры не должны меняться
#
# Sample Input 1:
#
# print(power(2, 5))
# Sample Output 1:
#
# 32
# Sample Input 2:
#
# print(power(3, 4))
# Sample Output 2:
#
# 81
# Sample Input 3:
#
# print(power(2, 10))
# Sample Output 3:
#
# 1024


def power(a: int, n: int) -> int:
    if n== 0:
        return 1
    return a * power(a, n-1)

print(power(2, 5))