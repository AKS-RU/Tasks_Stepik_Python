# Определите функцию generate_n_chars, которая имеет два параметра: целое число n и символ s. Функция должна
# вернуть строку длиной n символов, состоящую только из символов s. Например, вызов
#
# generate_n_chars(5, "x")
# должен возвращать строку «xxxxx».
#
# Ваша задача написать только определение функции generate_n_chars
#
# Sample Input 1:
#
# print(generate_n_chars(5, "x"))
# Sample Output 1:
#
# xxxxx
# Sample Input 2:
#
# print(generate_n_chars(10, "*"))
# Sample Output 2:
#
# **********
# Sample Input 3:
#
# print(generate_n_chars(2, "!"))
# Sample Output 3:
#
# !!

def generate_n_chars(n: int, s: str):
    return s*n

print(generate_n_chars(5, 'v'))