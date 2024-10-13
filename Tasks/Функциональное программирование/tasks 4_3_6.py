# Напишите функцию get_first_repeated_word, которая имеет один параметр words - список, состоящий из нескольких слов.
# Функция должна найти первый элемент, который образует дубль с ранее стоящими элементами, и вернуть его в качестве
# результата. Если передан список, в котором все слова различны, функция get_first_repeated_word должна вернуть None
# Регистр букв при сравнении нужно учитывать
#
# Для функции  get_first_repeated_word  дополнительно нужно добавить
#
#  1️⃣  док-строку  Находит первый дубль в списке
#
#  2️⃣  аннотации при помощи модуля typing
#
# Sample Input 1:
#
# print(get_first_repeated_word.__doc__)
# print(get_first_repeated_word.__annotations__)
# print(get_first_repeated_word(['hello', 'hi', 'hello']))
# Sample Output 1:
#
# Находит первый дубль в списке
# {'words': typing.List[str], 'return': typing.Optional[str]}
# hello
# Sample Input 2:
#
# print(get_first_repeated_word.__doc__)
# print(get_first_repeated_word.__annotations__)
# print(get_first_repeated_word(['hello', 'hi', 'Hello']))
# Sample Output 2:
#
# Находит первый дубль в списке
# {'words': typing.List[str], 'return': typing.Optional[str]}
# None
# Sample Input 3:
#
# print(get_first_repeated_word(['ab', 'ca', 'bc', 'ab']))
# Sample Output 3:
#
# ab
# Sample Input 4:
#
# print(get_first_repeated_word(['ab', 'ca', 'bc', 'Ab', 'cA', 'aB', 'bc']))
# Sample Output 4:
#
# bc
# Sample Input 5:
#
# print(get_first_repeated_word(['ab', 'ca', 'bc', 'ca', 'ab', 'bc']))
# Sample Output 5:
#
# ca

from typing import Optional, List


def get_first_repeated_word(words: List[str]) -> Optional[str]:
    'Находит первый дубль в списке'
    st_r = ''
    for i in words:
        if i in st_r:
            return i
        else:
            st_r += f' {i}'
    return None


print(get_first_repeated_word(['ab', 'ca', 'bc', 'ca', 'ab', 'bc']))
