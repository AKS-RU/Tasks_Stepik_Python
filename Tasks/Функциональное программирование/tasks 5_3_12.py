# В переменную check_word присвойте lambda функцию, которая принимает строку и возвращает
# True, если переданная строка начинается с букв «Q» или «R» и заканчивается любой из гласных
# «A», «E», «I», «U» или «O». Регистр во время проверок не должен иметь значения
#
# Во всех остальных случаях нужно возвращать False
#
# Ничего кроме создания переменной check_word делать не нужно
#
# Sample Input 1:
#
# print(check_word.__name__)
# print(check_word('radio'))
# Sample Output 1:
#
# <lambda>
# True
# Sample Input 2:
#
# print(check_word('raid'))
# print(check_word.__name__)
# Sample Output 2:
#
# False
# <lambda>
# Sample Input 3:
#
# print(check_word('revenge'))
# Sample Output 3:
#
# True


check_word = lambda x: x[0].lower() in 'qr' and x[-1].lower() in 'aeiuo'


print(check_word('revenge'))
