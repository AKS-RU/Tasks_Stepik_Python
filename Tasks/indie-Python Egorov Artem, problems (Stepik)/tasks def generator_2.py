# Ваша задача создать функцию-генератор gen_fibonacci_numbers, которая принимает аргумент n и генерирует n-ое
# количество чисел Фибоначчи.
#
# Будем считать, что последовательность Фибоначчи такая: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
#  Ниже несколько вариантов использования:
#
# for i in gen_fibonacci_numbers(5):
#     print(i)
#
# # Будет напечатано
# # 1
# # 1
# # 2
# # 3
# # 5
# for i in gen_fibonacci_numbers(10):
#     print(i)
#
# # Будет напечатано
# # 1
# # 1
# # 2
# # 3
# # 5
# # 8
# # 13
# # 21
# # 34
# # 55
# Ваша задача написать только определение функции gen_fibonacci_numbers

def gen_fibonacci_numbers(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b


for i in gen_fibonacci_numbers(10):
    print(i)
