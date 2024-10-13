# Наибольший общий делитель
# Перед вами реализация функции gcd, которая находит наибольший общий делитель при помощи итерации
#
# def gcd(a: int, b: int) -> int:
#     while b:
#         a, b = b, a % b
#     return a
# Перепишите данную программу при помощи рекурсии
#
# Sample Input 1:
#
# print(gcd(15, 5))
# Sample Output 1:
#
# 5
# Sample Input 2:
#
# print(gcd(7, 19))
# Sample Output 2:
#
# 1
# Sample Input 3:
#
# print(gcd(26, 65))
# Sample Output 3:
#
# 13


def gcd(a: int, b: int) -> int:
    if b > 0:
        return gcd(b, a % b)
    return a


print(gcd(15, 5))
