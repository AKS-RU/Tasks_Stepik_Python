# Декомпрессия строки
# В этом задании нужно написать алгоритм обратного преобразования. Вам будет дана уже сжатая
# строка, # состоящая из символов латинского алфавита и цифр. Необходимо реализовать алгоритм
# декомпрессии:
#     преобразовать строку из сжатого вида в несжатый, все символы алфавита при этом нужно
#     сделать строчными.

# Для этого вам необходимо реализовать функцию decompress_string, которая принимает в качестве
# аргумента сжатую строку и возвращает строку декомпрессии.

# Примечания:

# В результате, который возвращает функция decompress_string, все символы должны быть преобразованы
# к нижнему регистру
import re


def decompress_string(compressed: str) -> str:

    lower_compr = compressed.lower()

    if lower_compr.isalpha() or lower_compr == '':
        return lower_compr

    matches = re.findall(r"([a-zA-Z])(\d+)", lower_compr)
    result = "".join(x * int(y) for x, y in matches)

    return result


# Тестовые случаи
assert decompress_string("a4b3c1") == "aaaabbbc"
assert decompress_string("a1b5d1") == "abbbbbd"
assert decompress_string("w7") == "wwwwwww"
assert decompress_string("") == ""
assert decompress_string("aabbccddeeffgghh") == "aabbccddeeffgghh"
assert decompress_string("abcd") == "abcd"
assert decompress_string("xyz") == "xyz"

assert decompress_string("a6") == "aaaaaa"
assert decompress_string("a5") == "aaaaa"

assert decompress_string("AaBbCc") == "aabbcc"
assert decompress_string("a4b2c1a2") == "aaaabbcaa"
assert decompress_string("a4b3c2") == "aaaabbbcc"
assert decompress_string("a1000000") == "a" * 1000000
assert decompress_string("a1000000b500") == "a" * 1000000 + 'b' * 500
assert decompress_string(
    "a1b1c1d1e1f1g1h1i1j1k1w10000") == "abcdefghijk" + "w" * 10000

print('Тесты - ОК')
