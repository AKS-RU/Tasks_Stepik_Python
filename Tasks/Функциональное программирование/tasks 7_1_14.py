#                        Генератор факториалов
# Напишите генератор-функцию gen_factorial, которая принимает натуральное число n и генерирует факториалы чисел
# от 1! до n!
#
# Sample Input:
#
# for value in gen_factorial(5):
#     print(value)
# Sample Output:
#
# 1
# 2
# 6
# 24
# 120

def gen_factorial(n: int):
    result = 1
    for i in range(1, n+1):
        result*=i
        yield result


for value in gen_factorial(5):
    print(value)