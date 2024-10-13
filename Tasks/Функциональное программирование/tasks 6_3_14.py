# Напишите функцию filter_words, которая принимает список строк и возвращает новый список, который состоит из строк,
# длина которых четыре символа, или начинающихся на заглавную букву S.
#
# Sample Input 1:
#
# days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six',
#         'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
# print(filter_words(days))
# Sample Output 1:
#
# ['Four', 'Five', 'Six', 'Seven', 'Nine']
# Sample Input 2:
#
# words = ['scheme', 'hypnothize', 'exposure', 'Syndrome',
#          'Save', 'speculate', 'cane', 'welfare', 'blame', 'core']
# print(filter_words(words))
# Sample Output 2:
#
# ['Syndrome', 'Save', 'cane', 'core']


def filter_words(lst: list[str]) -> list[str]:
    return list(filter(lambda x: len(x) == 4 or x[0] == 'S', lst))


words = ['scheme', 'hypnothize', 'exposure', 'Syndrome',
         'Save', 'speculate', 'cane', 'welfare', 'blame', 'core']
print(filter_words(words))