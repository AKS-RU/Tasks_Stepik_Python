# Напишите функцию sum_digits, которая находит сумму всех цифр переданного натурального числа n
#
# Ваша задача только написать определение функции sum_digits
#
# Sample Input 1:
#
# print(sum_digits(345))
# Sample Output 1:
#
# 12
# Sample Input 2:
#
# print(sum_digits(45))
# Sample Output 2:
#
# 9
# Sample Input 3:
#
# print(sum_digits(5))
# Sample Output 3:
#
# 5



def sum_digits(n: int)->int:
    s=str(n)
    if len(s)==1:
        return s[0]
    a = sum_digits(int(s[1:]))
    return int(a) + int(s[0])


print(sum_digits(5))