# В переменную adding_10 присвойте lambda функцию, которая принимает одно число и увеличивает его на 10.
#
# Ничего кроме создания переменной adding_10 делать не нужно
#
# Sample Input 1:
#
# print(adding_10.__name__)
# print(adding_10(4))
# Sample Output 1:
#
# <lambda>
# 14
# Sample Input 2:
#
# print(adding_10.__name__)
# print(adding_10(400))
# Sample Output 2:
#
# <lambda>
# 410
# Sample Input 3:
#
# print(adding_10.__name__)
# print(adding_10(-56))
# Sample Output 3:
#
# <lambda>
# -46

adding_10 = lambda x: x+10

print(adding_10.__name__)
print(adding_10(400))