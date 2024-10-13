# Перепишите программу ниже при помощи генератора списков
#
# Sample Input:
#
# Sample Output:
#
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4)]

# result = []
# for i in range(1, 4):
#     for j in range(1, 5):
#         result.append((i, j))
# print(result)

print([(i, j) for i in range(1, 4) for j in range(1, 5)])
