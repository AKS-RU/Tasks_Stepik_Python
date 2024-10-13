# Определите функцию get_max, которая принимает два числа и возвращает большее из них.
#
#
#
# Ваша задача написать только определение функции get_max
#
# Sample Input 1:
#
# print(get_max(5, 9))
# Sample Output 1:
#
# 9
# Sample Input 2:
#
# print(get_max(295, 34))
# Sample Output 2:
#
# 295
# Sample Input 3:
#
# print(get_max(9, 9))
# Sample Output 3:
#
# 9

def get_max(a: int, b: int):
    return max(a, b)

print(get_max(4,7))