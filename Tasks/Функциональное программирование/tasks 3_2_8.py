# Напишите функцию find_longest_word_len, которая принимает список слов и возвращает длину самого длинного из них.
#
# Sample Input 1:
#
# print(find_longest_word_len(['hello', 'world', 'Python', 'reserve']))
# Sample Output 1:
#
# 7
# Sample Input 2:
#
# print(find_longest_word_len(['default', 'ghostwriter', 'bother', 'applaud', 'skate', 'way']))
# Sample Output 2:
#
# 11
# Sample Input 3:
#
# print(find_longest_word_len(['brain', 'candle', 'rare', 'shy']))
# Sample Output 3:
#
#

def find_longest_word_len(lst: list):
    return max(map(len,lst))

print(find_longest_word_len(['hello', 'world', 'Python', 'reserve']))