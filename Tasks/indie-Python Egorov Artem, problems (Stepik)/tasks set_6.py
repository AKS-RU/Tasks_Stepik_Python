# В первой и единственной строке задано описание множества букв. Длина строки не превышает 1000. Гарантируется, что строка начинается с открывающейся фигурной скобки, а заканчивается закрывающейся. Между ними через запятую перечислены маленькие латинские буквы. После каждой запятой следует пробел.
#
# Выходные данные
# Выведите единственное число — количество различных букв в множестве Антона.
#
# Sample Input 1:
#
# {a, b, c}
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# {b, a, b, a}
# Sample Output 2:
#
# 2
# Sample Input 3:
#
# {}
# Sample Output 3:
#
# 0
# Sample Input 4:
#
# {a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a,
#  a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a,
#  a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a}
# Sample Output 4:
#
# 1


res = set([i for i in input() if i.isalpha()])
print(len(set([i for i in input() if i.isalpha()])))
