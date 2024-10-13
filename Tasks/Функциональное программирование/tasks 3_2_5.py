# Напишите функцию filter_long_words, которая принимает список слов и целое число N и возвращает список слов,
# длина которых больше чем число N
#
# Sample Input 1:
#
# print(filter_long_words(['sister', 'arena', 'formal', 'arena', 'spill'], 5))
# Sample Output 1:
#
# ['sister', 'formal']
# Sample Input 2:
#
# print(filter_long_words(['Python', 'stole', 'my', 'heart'], 4))
# Sample Output 2:
#
# ['Python', 'stole', 'heart']
# Sample Input 3:
#
# print(filter_long_words(['ex', 'care', 'room', 'law'], 3))
# Sample Output 3:
#
# ['care', 'room']

def filter_long_words(lst: list, n):
    return [i for i in lst if len(i)>n]

print(filter_long_words(['Python', 'stole', 'my', 'heart'], 4))