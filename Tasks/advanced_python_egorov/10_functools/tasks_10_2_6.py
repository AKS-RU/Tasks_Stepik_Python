# Напишите функцию get_str_from_chars, которая принимает список символов и возвращает строку,
# полученную в результате сцепления элементов списка

# Примечание: используйте для решения функцию reduce

from functools import reduce


def get_str_from_chars(lst_smb: list) -> str:
    return reduce(lambda x, y: x+y, lst_smb)


letters = ['P', 'y', 't', 'h', 'o', 'n']
print(get_str_from_chars(letters))

letters = ['B', 'e', 's', 't', ' ', 'O', 'f',
           ' ', 'T', 'h', 'e', ' ', 'B', 'e', 's', 't']
print(get_str_from_chars(letters))
