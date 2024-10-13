# Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на
# экран результат проверки.
#
# Сложным паролем будет считаться комбинация символов, в которой :
#
# Есть хотя бы 3 цифры
# Есть хотя бы одна заглавная буква
# Есть хотя бы один символ из следующего набора "!@#$%*"
# Общая длина не менее 10 символов
# Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password",
# в противном случае - "Easy peasy"
#
# Вам необходимо написать только определение функции check_password
#
# Разбор Youtube Patreon Boosty
#
# Sample Input 1:
#
# qwerty
# Sample Output 1:
#
# Easy peasy
# Sample Input 2:
#
# Qwerty1357!
# Sample Output 2:
#
# Perfect password
# Sample Input 3:
#
# Qwerty1357)
# Sample Output 3:
#
# Easy peasy
# Sample Input 4:
#
# Qwerty17!
# Sample Output 4:
#
# Easy peasy

def check_password(x):
    cnt_d, cnt_u, cnt_smb = 0, 0, 0
    if len(x) >= 10:
        for i in x:
            if i.isdigit():
                cnt_d += 1
            elif i.isupper():
                cnt_u += 1
            elif i in '!@#$%*':
                cnt_smb += 1
    print('Perfect password' if cnt_d >= 3 and cnt_u > 0 and cnt_smb > 0 else 'Easy peasy')

check_password('Qwerty17!')
