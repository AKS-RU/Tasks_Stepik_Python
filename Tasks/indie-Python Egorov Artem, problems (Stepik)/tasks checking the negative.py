# Миша и негатив
# Миша уже научился хорошо фотографировать и недавно увлекся программированием. Первая программа, которую он написал,
# позволяет формировать негатив бинарного черно-белого изображения.
#
# Бинарное черно-белое изображение – это прямоугольник, состоящий из пикселей, каждый из которых может быть либо черным,
# либо белым. Негатив такого изображения получается путем замены каждого черного пикселя на белый, а каждого белого пикселя –
# на черный.
#
# Миша, как начинающий программист, написал свою программу с ошибкой, поэтому в результате ее исполнения мог получаться
# некорректный негатив. Для того чтобы оценить уровень несоответствия получаемого негатива исходному изображению, Миша
# начал тестировать свою программу.
#
# В качестве входных данных он использовал исходные изображения. Сформированные программой негативы он начал тщательно
# анализировать, каждый раз определяя число пикселей негатива, которые получены с ошибкой.
#
# Требуется написать программу, которая в качестве входных данных использует исходное бинарное черно-белое изображение
# и полученный Мишиной программой негатив, и на основе этого определяет количество пикселей, в которых допущена ошибка.
#
# Программа сперва считывает числа n и m (1 ≤ n, m ≤ 100) – высоту и ширину исходного изображения (в пикселях). Последующие
# n строк содержат описание исходного изображения. Каждая строка состоит из m символов «B» и «W». Символ «B» соответствует
# черному пикселю, а символ «W» – белому. Далее следует пустая строка, а после нее – описание выведенного Мишиной программой
# изображения в том же формате, что и исходное изображение.
#
# Необходимо вывести на экран число пикселей негатива, которые неправильно сформированы Мишиной программой.
#
# 3 4
# WBBW
# BBBB
# WBBW
#
# BWWW
# WWWB
# BWWB
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# 2 2
# BW
# BB
#
# WW
# BW
# Sample Output 2:
#
# 2


# a, b = map(int, input().split())  # 3, 4
# orig = []  # [['W', 'B', 'B', 'W'], ['B', 'B', 'B', 'B'], ['W', 'B', 'B', 'W']]
# negat = []  # [['B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B'], ['B', 'W', 'W', 'B']]
# for ln in range(a):
#     orig.append(list(input()))
# input()
# for ln in range(a):
#     negat.append(list(input()))
#
# res = []
# err = 0
#
# for ln in range(a):
#     tmp_res = []
#     for cl in range(b):
#         if orig[ln][cl] == 'W':
#             tmp_res.append('B')
#         else:
#             tmp_res.append('W')
#     res.append(tmp_res)
#
# for ln in range(a):
#     for cl in range(b):
#         if negat[ln][cl] != res[ln][cl]:
#             err += 1
# print(err)

# Очень длинный код. На самом деле нужно было понимать, что клетка которая B должна быть негативом B
# получается нам нужно просто проверить равны ли одинаковые индексы. И если да, то это ошибка.
# Вот решение которое подсмотрено с форума решений

a, b = map(int, input().split())  # 3, 4
orig = []  # [['W', 'B', 'B', 'W'], ['B', 'B', 'B', 'B'], ['W', 'B', 'B', 'W']]
negat = []  # [['B', 'W', 'W', 'W'], ['W', 'W', 'W', 'B'], ['B', 'W', 'W', 'B']]

err = 0
for ln in range(a):
    orig.append(list(input()))
input()
for ln in range(a):
    negat.append(list(input()))
for ln in range(a):
    for cl in range(b):
        if orig[ln][cl] == negat[ln][cl]:
            err += 1
print(err)