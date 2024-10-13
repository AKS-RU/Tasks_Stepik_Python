# Генератор квадратов
# Ваша задача создать функцию-генератор gen_squares, которая принимает аргумент n и генерирует квадраты чисел от 1 до n
# включительно. Ниже несколько вариантов использования:
#
# Ваша задача написать только определение функции gen_squares
#
# Sample Input 1:
#
# for i in gen_squares(5):
#     print(i)
# Sample Output 1:
#
# 1
# 4
# 9
# 16
# 25
# Sample Input 2:
#
# for i in gen_squares(9):
#     print(i)
# Sample Output 2:
#
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81


def gen_squares(n: int):
    cnt = 1
    while cnt <= n:
        yield cnt ** 2
        cnt += 1

for i in gen_squares(9):
    print(i)
