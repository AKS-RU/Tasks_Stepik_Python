# Напишите функцию sum_num для суммирования всех цифр строки.
# Функция должна принимать строку, суммировать все ее символы, которые являются цифрами,
# и в качестве ответа выводить найденную сумму.
#
# Вам необходимо написать только определение функции sum_num .
#
# Sample Input 1:
#
# 4
# Sample Output 1:
#
# 4
# Sample Input 2:
#
# 123QwertY321
# Sample Output 2:
#
# 12
# Sample Input 3:
#
# -123.78
# Sample Output 3:
#
# 21

def sum_num(x):
    print(sum([int(i) if i.isdigit() else 0 for i in x]))


sum_num()