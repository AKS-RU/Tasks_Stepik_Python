# Напишите функцию count_words, которая принимает строку и подсчитывает количество слов в строке. Слова разделяются
# между собой пробелом. Функция count_words должна вернуть найденное количество слов в строке в качестве результата.
#
# В строках могут присутствовать незначащие пробелы с обеих сторон
#
# Sample Input 1:
#
# print(count_words('I like learn python'))
# Sample Output 1:
#
# 4
# Sample Input 2:
#
# print(count_words("Find definitions and references for functions and other symbols in this file by clicking a symbol "
#                   "below or in the code"))
# Sample Output 2:
#
# 21
# Sample Input 3:
#
# print(count_words(' hello   bro  '))
# Sample Output 3:
#
# 2
#
def count_words(st: str):
    st = st.split()
    return len(st)

print(count_words('jhkjhk jh kjh kjh jhk jhk kkkk'))