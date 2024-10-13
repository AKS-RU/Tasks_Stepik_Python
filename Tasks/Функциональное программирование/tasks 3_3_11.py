# Панграмма — это предложение, которое содержит все буквы алфавита хотя бы один раз. В нашем задании мы будем
# рассматривать в качестве алфавита буквы английского языка. Тогда одним из примеров панграммы будет фраза
# «The quick brown fox jumps over the lazy dog».
#
# Ваша задача здесь — написать функцию is_pangram для проверки предложения на предмет того, является ли оно панграммой
# или нет. Для проверок внутри функции вы можете пользоваться глобальной переменной alpha. Символы, которые не являются
# буквами, необходимо игнорировать.
#
# Sample Input 1:
#
# print(is_pangram("The quick brown fox jumps over the lazy dog."))
# Sample Output 1:
#
# True
# Sample Input 2:
#
# print(is_pangram("Obviously not a pangram"))
# Sample Output 2:
#
# False
# Sample Input 3:
#
# print(is_pangram("How quickly daft jumping zebras vex!"))
# Sample Output 3:
#
#
alpha = 'abcdefghijklmnopqrstuvwxyz'
def is_pangram(text: str):
    return all(map(lambda x: x in text.lower(),alpha))

print(is_pangram('How quickly daft jumping zebras vex!'))
