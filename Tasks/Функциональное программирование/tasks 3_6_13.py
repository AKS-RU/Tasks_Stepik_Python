# Напишите функцию multiply, которая принимает произвольное количество числовых аргументов. Данная функция должна
# находить произведение всех переданных значений и возвращать его в качестве результата
#
# При вызове multiply без параметров должен возвращаться результат 1.
#
# Вам необходимо написать только определение функции multiply
#
# Sample Input 1:
#
# print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10))
# Sample Output 1:
#
# 0
# Sample Input 2:
#
# print(multiply(1, 2, 3, 4, 5, 6))
# Sample Output 2:
#
# 720
# Sample Input 3:
#
# print(multiply())
# Sample Output 3:
#
# 1
# Sample Input 4:
#
# print(multiply(1))
# Sample Output 4:
#
# 1


def multiply(*args):
    result=1
    for i in args:
        result*=i
    return result

print(multiply())