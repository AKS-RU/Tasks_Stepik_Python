# Cтрока S1 называется анаграммой строки S2, если она получается из S2 перестановкой символов.
#
# Программа получает на вход две строки S1 и S2. Если строка S1 является анаграммой строки S2 нужно
# вывести YES, в противном случае - NO
#
# Sample Input 1:
#
# abc
# cba
# Sample Output 1:
#
# YES
# Sample Input 2:
#
# abracadabra
# cadabraabra
# Sample Output 2:
#
# YES
# Sample Input 3:
#
# abb
# bbc
# Sample Output 3:
#
# NO


d_a, d_b = {}, {}

for i in input():
    d_a[i] = d_a.get(i, 0) + 1
for i in input():
    d_b[i] = d_b.get(i, 0) + 1

print('YES' if d_a == d_b else 'NO')
