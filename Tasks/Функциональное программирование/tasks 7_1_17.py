# Функция-генератор chunker
# Если у вас есть итерируемый объект, который слишком велик для того, чтобы полностью поместиться в памяти
# (например, при работе с большими файлами), возможность дробить его на небольшие фрагменты и затем использовать
# их за раз может быть очень ценной.
#
# С этой задачей должна справиться функция-генератор chunker. Она должна принимать итерируемый объект и выдавать
# фрагмент указанного размера за раз.
#
# Ваша задача написать функцию-генератор chunker
#
# Sample Input 1:
#
# for chunk in chunker(range(25), 4):
#     print(list(chunk))
# Sample Output 1:
#
# [0, 1, 2, 3]
# [4, 5, 6, 7]
# [8, 9, 10, 11]
# [12, 13, 14, 15]
# [16, 17, 18, 19]
# [20, 21, 22, 23]
# [24]
# Sample Input 2:
#
# for chunk in chunker(range(56), 9):
#     print(list(chunk))
# Sample Output 2:
#
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# [9, 10, 11, 12, 13, 14, 15, 16, 17]
# [18, 19, 20, 21, 22, 23, 24, 25, 26]
# [27, 28, 29, 30, 31, 32, 33, 34, 35]
# [36, 37, 38, 39, 40, 41, 42, 43, 44]
# [45, 46, 47, 48, 49, 50, 51, 52, 53]
# [54, 55]
# Sample Input 3:
#
# text = '''Python 3.12 is the latest stable release of the Python programming language, with a mix of changes to
# the language and the standard library.'''
#
# for chunk in chunker(text, 7):
#     print(chunk)
# Sample Output 3:
#
# Python
# 3.12 is
#  the la
# test st
# able re
# lease o
# f the P
# ython p
# rogramm
# ing lan
# guage,
# with a
# mix of
# changes
#  to the
#  langua
# ge and
# the sta
# ndard l
# ibrary.


def chunker(iterables, size: int):
    for i in range(0, len(iterables), size):
        yield iterables[i:i + size]


text = '''Python 3.12 is the latest stable release of the Python programming language, with a mix of changes to the language and the standard library.'''

for chunk in chunker(text, 7):
    print(chunk)
