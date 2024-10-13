# Напишите функцию is_leap, которая проверяет является ли переданный год високосным или нет.
#
# Високосным является год, номер которого делится на 4, но не делится на 100, или же номер которого делится на 400.
#
# Напишите только определение функции is_leap
#
# Sample Input 1:
#
# print(is_leap(1900))
# Sample Output 1:
#
# False
# Sample Input 2:
#
# print(is_leap(2000))
# Sample Output 2:
#
# True
# Sample Input 3:
#
# print(is_leap(2004))
# Sample Output 3:
#
# True
# Sample Input 4:
#
# print(is_leap(2005))
# Sample Output 4:
#
# False
# Sample Input 5:
#
# print(is_leap(2100))
# Sample Output 5:
#
# False
# Sample Input 6:
#
# print(is_leap(2400))
# Sample Output 6:
#
#

def is_leap(year: int):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


print(is_leap(2400))
