# Генератор последовательности Фибоначчи
# Ваша задача создать функцию-генератор gen_fibonacci_numbers, которая принимает аргумент n и генерирует n-ое
# количество чисел Фибоначчи.
#
# Будем считать, что последовательность Фибоначчи такая: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Ваша задача написать только определение функции gen_fibonacci_numbers
#
# Sample Input 1:
#
# for i in gen_fibonacci_numbers(5):
#     print(i)
# Sample Output 1:
#
# 1
# 1
# 2
# 3
# 5
# Sample Input 2:
#
# for i in gen_fibonacci_numbers(11):
#     print(i)
# Sample Output 2:
#
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89


def gen_fibonacci_numbers(n: int):
    a, b = 0, 1
    for i in range(n):
        yield b
        a, b = b, a + b


for i in gen_fibonacci_numbers(11):
    print(i)
