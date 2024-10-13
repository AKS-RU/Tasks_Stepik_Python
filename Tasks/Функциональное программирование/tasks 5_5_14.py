# Ваша задача написать функцию count_strings, которая принимает произвольное количество аргументов. Функция должна
# среди всех переданных значений найти только строки, найти их количество и  вернуть в качестве результата.
#
# Ваша задача написать только определение функции count_strings
#
# Sample Input 1:
#
# print(count_strings(1, 2, 'hello', True, 't'))
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# print(count_strings('1', '2', 'hello', True, 't'))
# Sample Output 2:
#
# 4
# Sample Input 3:
#
# print(count_strings())
# Sample Output 3:
#
# 0


def count_strings(*args):
    return len([i for i in args if isinstance(i, str)])

print(count_strings('1', '2', 'hello', True, 't'))
