# Напишите функцию is_strings_equal, которая принимает две строки в качестве аргументов и сравнивает их между собой.
#
# Строки считаются равными, если они имеют одинаковую длину и одинаковые символы в равном количестве вне зависимости
# от их расположения.
#
# Функция is_strings_equal должна вернуть True, если строки равны, в противном случае - False.
#
# Sample Input 1:
#
# print(is_strings_equal("leto", "etol"))
# Sample Output 1:
#
# True
# Sample Input 2:
#
# print(is_strings_equal("1212", "2131"))
# Sample Output 2:
#
# False
# Sample Input 3:
#
# print(is_strings_equal("qwerty", "rtyewq"))
# Sample Output 3:
#
# True
# Sample Input 4:
#
# print(is_strings_equal("aabc", "bcab"))
# Sample Output 4:
#
# False
# Sample Input 5:
#
# print(is_strings_equal("aabcb", "bcaba"))
# Sample Output 5:
#
# True

def is_strings_equal(word_1: str, word_2: str):
    is_len = [len(word_1) == len(word_2)]
    is_word = list(map(lambda x: word_1.count(x) == word_2.count(x), word_1))
    return False not in is_len and False not in is_word


print(is_strings_equal('aabcb', 'bcaba'))
