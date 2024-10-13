# Напишите генератор-функцию gen_odd, которая принимает натуральное число n и генерирует последовательность
# нечетных чисел от 1 до n включительно
#
# Sample Input:
#
# for value in gen_odd(5):
#     print(value)
# Sample Output:
#
# 1
# 3
# 5


def gen_odd(n: int):
    result = filter(lambda x: x % 2 != 0, range(1, n + 1))
    return result


for value in gen_odd(5):
    print(value)