# Ваша задача создать функцию-генератор gen_squares, которая принимает аргумент n и генерирует квадраты чисел от 1
# до n включительно. Ниже несколько вариантов использования:
#
# for i in gen_squares(5):
#     print(i)
#
# # Будет напечатано
# # 1
# # 4
# # 9
# # 16
# # 25
# for i in gen_squares(3):
#     print(i)
#
# # Будет напечатано
# # 1
# # 4
# # 9
# Ваша задача написать только определение функции gen_squares


def gen_squares(n: int):
    for i in range(1, n+1):
        sq=i**2
        yield sq

for i in gen_squares(5):
    print(i)
