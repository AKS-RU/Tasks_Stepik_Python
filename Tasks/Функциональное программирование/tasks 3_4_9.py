# Напишите функцию product , которая принимает список чисел и находит их произведение. Также данная функция может
# принимать необязательный параметр start , который отвечает за начальное значение произведения (по умолчанию равно 1)
#
# Sample Input 1:
#
# print(product([1, 2, 3]))
# Sample Output 1:
#
# 6
# Sample Input 2:
#
# print(product([1, 2, 3], start=10))
# Sample Output 2:
#
# 60

def product(lst: list, start=1):
    multi = start
    for i in lst:
        multi*=i
    return multi

print(product([1, 2, 3],10))


