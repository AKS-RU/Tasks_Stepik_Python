#                    Удваиваем результат
# Напишите декоратор double_it, который возвращает удвоенный результат вызова декорированной функции
#
# Ваша задача написать только определение функции декоратора double_it
#
# Sample Input 1:
#
# @double_it
# def multiply(num1, num2):
#     return num1 * num2
#
# res = multiply(9, 4) # произведение 9*4=36, но декоратор double_it удваивает это значение
# print(res)
# Sample Output 1:
#
# 72
# Sample Input 2:
#
# @double_it
# def get_sum(*args):
#     return sum(args)
#
# res = get_sum(1, 2, 3, 4, 5)
# print(res) # сумму 15 увеличивает в 2 раза
# Sample Output 2:
#
# 30
# Sample Input 3:
#
# @double_it
# def calculate(a, b, c):
#     return a ** b + c
#
# print(calculate(4, 5, 4))
# Sample Output 3:
#
# 2056
# Sample Input 4:
#
# @double_it
# def get_sum_kwargs_values(**kwargs):
#     return sum(kwargs.values())
#
#
# print(get_sum_kwargs_values(a=4, b=5, c=7))
# print(get_sum_kwargs_values(a=4, b=5, d=3, t=6, r=8))
# Sample Output 4:
#
# 32
# 52


def double_it(func):
    def double(*args, **kwargs):
        result = func(*args, **kwargs)
        return result*2
    return double


@double_it
def multiply(num1, num2):
    return num1 * num2


res = multiply(9, 4)  # произведение 9*4=36, но декоратор double_it удваивает это значение
print(res)