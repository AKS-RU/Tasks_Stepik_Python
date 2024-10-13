# Напишите функцию words_length, которая по входному списку слов создает список целых чисел, составленный из длины
# соответствующих слов и возвращает его в качестве результата.
#
# Sample Input 1:
#
# print(words_length(['Hello', 'world!']))
# Sample Output 1:
#
# [5, 6]
# Sample Input 2:
#
# print(words_length(['Python', 'is', 'awesome!']))
# Sample Output 2:
#
# [6, 2, 8]
# Sample Input 3:
#
# print(words_length(['You', 'should', 'learn', 'it!']))
# Sample Output 3:
#
# [3, 6, 5, 3]

def words_length(lst: list):
    return list(map(len,lst))


print(words_length(['You', 'should', 'learn', 'it!']))