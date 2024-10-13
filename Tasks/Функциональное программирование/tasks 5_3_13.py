# Помните задачу «Проверка на високосность»?
# Високосным является год, номер которого делится на 4, но не делится
# на 100, или же номер которого делится на 400.
# Ваша задача реализовать данную функцию при помощи lambda оператора
#
# Полученную функцию сохраните в переменную is_leap
#
# Sample Input 1:
#
# print(is_leap(1900))
# print(is_leap.__name__)
# Sample Output 1:
#
# False
# <lambda>
# Sample Input 2:
#
# print(is_leap.__name__)
# print(is_leap(2000))
# Sample Output 2:
#
# <lambda>
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


is_leap = lambda x: (x % 4 == 0 and x % 100 != 0) or x % 400 == 0

print(is_leap(2400))
