# Двойной факториал
# Необходимо написать рекурсивную функцию double_fact, которая принимает на вход целое число и вычисляет значение двойного факториала по формуле:
#
#
#
# Ваша задача только написать определение функции double_fact
#
# Sample Input 1:
#
# print(double_fact(6))
# Sample Output 1:
#
# 48
# Sample Input 2:
#
# print(double_fact(5))
# Sample Output 2:
#
# 15
# Sample Input 3:
#
# print(double_fact(2))
# Sample Output 3:
#
# 2
# Sample Input 4:
#
# print(double_fact(4))
# Sample Output 4:
#
# 8


def double_fact(n: int) -> int:
    if n in (1, 2):
        return n
    a = double_fact(n - 2)
    return n * a


print(double_fact(4))
