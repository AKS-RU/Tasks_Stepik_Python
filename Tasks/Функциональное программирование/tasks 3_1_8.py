# Определите функцию is_palindrome, которая принимает строку и отвечает на вопрос, является ли она палиндромом или нет
#
# Палиндромами считаются слова, которые читаются одинаково слева направо и справа налево, как например слово «радар»
#
# При проверке не нужно учитывать регистр букв. Это значит, что слова «радар» и «Радар» считаются одинаковыми.
#
# Также во входной строке могут встречаться пробелы, их необходимо исключить из проверки. Остальные знаки пунктуации,
# такие как запятые, точки, дефисы и т.д., во входных данных отсутствуют.
#
# Sample Input 1:
#
# print(is_palindrome("Never Odd or Even"))
# Sample Output 1:
#
# True
# Sample Input 2:
#
# print(is_palindrome("abc"))
# Sample Output 2:
#
# False
# Sample Input 3:
#
# print(is_palindrome("kayak"))
# Sample Output 3:
#
# True
# Sample Input 4:
#
# print(is_palindrome("KayAk"))
# Sample Output 4:
#
# True


def is_palindrome(text: str):
    revers_text = text[::-1]
    return text.replace(' ','').lower() == revers_text.replace(' ','').lower()

print(is_palindrome('Never Odd or Even'))
# is_palindrome('Never Odd or Even')