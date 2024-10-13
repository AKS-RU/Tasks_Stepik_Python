# Генератор бесконечной арифметической прогрессии
# Ваша задача создать функцию-генератор gen_arithmetic_progression, которая при вызове принимает два значения:
#
# первый элемент прогрессии
# разность элементов прогрессии
# Функция-генератор gen_arithmetic_progression должна выдавать элементы бесконечной арифметической прогрессии с
# учетом переданных значений
#
# Ваша задача написать только определение функции-генератора gen_arithmetic_progression
#
# Sample Input 1:
#
# count = 1
# for value in gen_arithmetic_progression(5, 7):
#     print(value)
#     count += 1
#     if count > 5:
#         break
# Sample Output 1:
#
# 5
# 12
# 19
# 26
# 33
# Sample Input 2:
#
# count = 8
# for value in gen_arithmetic_progression(105, -5):
#     print(value)
#     count -= 1
#     if count == 0:
#         break
# Sample Output 2:
#
# 105
# 100
# 95
# 90
# 85
# 80
# 75
# 70


def gen_arithmetic_progression(start: int, step: int):
    result = start
    while True:
        yield result
        result += step


count = 1
for value in gen_arithmetic_progression(5, 7):
    print(value)
    count += 1
    if count > 5:
        break
