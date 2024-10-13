# Напишите рекурсивную функцию is_palindrome, которая при помощи рекурсии определяет, является ли переданное слово
# палиндромом. Во время проверок регистр букв не учитывайте.
#
# В тестовых данных используются только символы английского алфавита. Знаки пунктуации и пробелы отсутствуют.
#
# Sample Input 1:
#
# print(is_palindrome('abba'))
# Sample Output 1:
#
# True
# Sample Input 2:
#
# print(is_palindrome('Qwerty'))
# Sample Output 2:
#
# False
# Sample Input 3:
#
# print(is_palindrome('Racecar'))
# Sample Output 3:
#
# True


def is_palindrome(text: str)-> bool:
    norm = text.lower()
    rev = norm[::-1]
    if len(norm)==1:
        return norm[0]== rev[0]
    x = is_palindrome(norm[1:])
    y = is_palindrome(rev[1:])
    if norm[0]!=rev[0]:
        return False
    return True

print(is_palindrome(' '))
