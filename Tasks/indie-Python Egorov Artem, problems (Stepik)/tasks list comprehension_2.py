# result = []
# for x in range(15):
#     if x % 2 == 0:
#         result.append(x * x)
# print(result)
# [0, 4, 16, 36, 64, 100, 144, 196]
result = [x * x for x in range(15) if x % 2 == 0]
print(result)
