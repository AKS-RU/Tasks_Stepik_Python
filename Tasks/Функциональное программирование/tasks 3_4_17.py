# Помните функцию words_length, которая по входному списку слов создавала список длины соответствующих слов и
# возвращала его в качестве результата? Одна из возможных реализаций этой функции представлена ниже
#
# def words_length(words):
#     return [len(word) for word in words]
# Здесь функция words_length является чистой. Ваша задача переписать ее так, чтобы она начала изменять входной
# список: вместо слов должна подставляться его длина. В качестве результата новая words_length должна вернуть None
#
# Sample Input 1:
#
# words = ['Hello', 'world!']
# words_length(words)
# print(words)
# Sample Output 1:
#
# [5, 6]
# Sample Input 2:
#
# words = ['Python', 'is', 'awesome!']
# words_length(words)
# print(words)
# Sample Output 2:
#
# [6, 2, 8]
# Sample Input 3:
#
# words = ['Python', 'is', 'awesome!']
# result = words_length(words)
# print(words)
# print(result)
# Sample Output 3:
#
# [6, 2, 8]
# None
# Sample Input 4:
#
# words = ['Python', 'is', 'awesome!']
# words = words_length(words)
# print(words)
# Sample Output 4:
#
# None

words = ['Python', 'is', 'awesome!']


def words_length(word):
        global words
        words = [len(i) for i in word]
        return None
# words_length(words)
# print(words)
result = words_length(words)
print(words)
print(result)