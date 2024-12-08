# Компрессия строки
# Дана строка, состоящая из символов латинского алфавита. Необходимо реализовать алгоритм сжатия
# этой строки, заменяя повторяющиеся символы на символ и количество его повторений.

# Для этого вам необходимо реализовать функцию compress_string, которая принимает в качестве
# аргумента исходную строку и возвращает сжатую версию строки.

# Примечания:

# Ваше решение должно быть регистронезависимым, то есть «A» и «a» считаются одним и тем же символом.
# Если сжатая строка не короче исходной, то функция должна вернуть исходную строку без изменений.
# Если возвращается сжатая версия строки, все символы в ней должны быть преобразованы к нижнему
# регистру.

from itertools import groupby


def compress_string(string: str) -> str:
    result = ''.join(f'{key}{len(list(group))}' for key,
                     group in groupby(string.lower()))

    return result if len(result) < len(string) else string


# Тестовые случаи с корректными входными данными
assert compress_string("aaaabbbc") == "a4b3c1"
assert compress_string("abbbbbd") == "a1b5d1"
assert compress_string("wwwwwww") == "w7"
assert compress_string("") == ""
print(f'Тестовые случаи с корректными входными данными - OK')


# # # Тестовые случаи с входными данными, которые не нуждаются в сжатии
assert compress_string("abcd") == "abcd"
assert compress_string("xyz") == "xyz"
assert compress_string("aabbccddeeffgghh") == "aabbccddeeffgghh"
print(f'Тестовые случаи с входными данными, которые не нуждаются в сжатии - OK')

# # # Тестовые случаи с регистронезависимостью
assert compress_string("aaAAaa") == "a6"
assert compress_string("aAaAA") == "a5"
assert compress_string("AaBbCc") == "AaBbCc"
assert compress_string("aaaAbbCaa") == "a4b2c1a2"
assert compress_string("AAAABBBCC") == "a4b3c2"
print(f'Тестовые случаи с регистронезависимостью - OK')

# # # Тестовые случаи с длинной строки
assert compress_string("a" * 1000000) == "a1000000"
print(f'Тестовые случаи с длинной строки 1 - OK')
assert compress_string("a" * 1000000 + 'b' * 500) == "a1000000b500"
print(f'Тестовые случаи с длинной строки 2 - OK')
assert compress_string("abcdefghijk" + "w" *
                       10000) == "a1b1c1d1e1f1g1h1i1j1k1w10000"

print('OK')
