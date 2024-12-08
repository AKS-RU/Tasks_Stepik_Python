# Напишите функцию get_reverse_str_from_chars, которая принимает список символов и возвращает
# перевернутую строку, полученную из этих символов.

# Примечание: используйте для решения функцию reduce

from functools import reduce


def get_reverse_str_from_chars(lst_str: list) -> str:
    return reduce(lambda x, y: x+y, reversed(lst_str))


letters = ['P', 'y', 't', 'h', 'o', 'n']
print(get_reverse_str_from_chars(letters))

letters = ['B', 'e', 's', 't', ' ', 'O', 'f',
           ' ', 'T', 'h', 'e', ' ', 'B', 'e', 's', 't']
print(get_reverse_str_from_chars(letters))
