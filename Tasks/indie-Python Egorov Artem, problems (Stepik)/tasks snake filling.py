# Заполнение змейкой
# Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой (см. пример).
#
# Входные данные
# Программа получает на вход два числа n и m.
#
# Выходные данные
# Программа должна вывести  полученный массив, при этом между числами может быть любое количество пробелов.
#
# Sample Input 1:
#
# 4 10
# Sample Output 1:
#
# 0  1  2  3  4  5  6  7  8  9
# 19 18 17 16 15 14 13 12 11 10
# 20 21 22 23 24 25 26 27 28 29
# 39 38 37 36 35 34 33 32 31 30
# Sample Input 2:
#
# 3 4
# Sample Output 2:
#
# 0 1 2 3
# 7 6 5 4
# 8 9 10 11
# Sample Input 3:
#
# 10 2
# Sample Output 3:
#
# 0 1
# 3 2
# 4 5
# 7 6
# 8 9
# 11 10
# 12 13
# 15 14
# 16 17
# 19 18
# Sample Input 4:
#
# 5 5
# Sample Output 4:
#
# 0 1 2 3 4
# 9 8 7 6 5
# 10 11 12 13 14
# 19 18 17 16 15
# 20 21 22 23 24
# Sample Input 5:
#
# 1 1
# Sample Output 5:
#
# 0

a, b = map(int, input().split())  # 4, 10
cnt = 0

for ln in range(a):
    m_t = []
    for cl in range(b):
        m_t.append(cnt)
        cnt += 1
    # m.append(m_t)
    if ln % 2:
        m_t.reverse()
        # m.append(m_t)
    print(*m_t)
# for ln in range(a):
#     for cl in range(b):
#         print(m[ln][cl], end=' ')
#     print()
