#                   Генератор факториалов - 2
# Измените генератор-функцию gen_factorial так, чтобы он стал выдавать бесконечную последовательность факториалов
#
# Sample Input 1:
#
# count = 1
# for value in gen_factorial():
#     print(value)
#     count += 1
#     if count > 10:
#         break
# Sample Output 1:
#
# 1
# 2
# 6
# 24
# 120
# 720
# 5040
# 40320
# 362880
# 3628800
# Sample Input 2:
#
# count = 15
# for value in gen_factorial():
#     print(value)
#     count -= 1
#     if count == 0:
#         break
# Sample Output 2:
#
# 1
# 2
# 6
# 24
# 120
# 720
# 5040
# 40320
# 362880
# 3628800
# 39916800
# 479001600
# 6227020800
# 87178291200
# 1307674368000


def gen_factorial():
    result = 1
    cnt = 1
    while True:
        yield result
        cnt += 1
        result *= cnt


count = 15
for value in gen_factorial():
    print(value)
    count -= 1
    if count == 0:
        break
