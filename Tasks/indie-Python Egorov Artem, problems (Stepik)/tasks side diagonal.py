# Дана матрица размером NxN, требуется найти максимальное значение среди элементов, расположенных на побочной диагонали.
#
# Под побочной диагональю матрицы подразумевается диагональ, проведённая из правого верхнего угла до левого нижнего угла.
#
#
#
# Входные данные
# Программа сперва принимает на вход число N (N<=15) - количество строк и столбцов в списке, а затем в N строках записаны
# элементы списка.
#
# Выходные данные
# Вывести самой большой элемент на побочной диагонали
#
# Sample Input 1:
#
# 2
# 1 2
# 3 4
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Sample Output 2:
#
# 7
# Sample Input 3:
#
# 5
# 100 2 3 90 100
# 1 54 3 90 100
# 1 2 5 90 100
# 1 2 3 2 100
# 1 2 3 90 100
# Sample Output 3:
#
# 100

# a = int(input()) # 3
# x = a
# m = []#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(a):
#     m.append(list(map(int,input().split())))
# res = []
# m_max = 0
#
# for ln in range(a):
#     res_tmp = []
#     for cl in range(x):
#         # print(m[ln][cl], end=" ")
#         res_tmp.append(m[ln][cl])
#     res.append(res_tmp)
#     x -= 1
# #     print()
# # print(res)
# for ln in range(a):
#     # print(res[ln][-1])
#     if res[ln][-1] > m_max:
#         m_max = res[ln][-1]
# print(m_max)


a = int(input())
m = []
d = a - 1
for i in range(a):
    m.append(list(map(int,input().split())))
m_max = 0

for ln in range(a):
    if m[ln][d] > m_max:
        m_max = m[ln][d]
    d -= 1
print(m_max)
