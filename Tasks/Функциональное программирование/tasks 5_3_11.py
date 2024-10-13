# В переменную starts_with присвойте lambda функцию, которая принимает строку и возвращает True, когда переданная
# строка начинается с буквы «W». Во всех остальных случаях нужно возвращать False
#
# Ничего кроме создания переменной starts_with делать не нужно
#
# Sample Input 1:
#
# print(starts_with.__name__)
# print(starts_with('World'))
# Sample Output 1:
#
# <lambda>
# True
# Sample Input 2:
#
# print(starts_with('when'))
# print(starts_with.__name__)
# Sample Output 2:
#
# False
# <lambda>
# Sample Input 3:
#
# print(starts_with('Сурикаты'))
# Sample Output 3:
#
# False


starts_with = lambda x: x[0] == 'W'


print(starts_with('when'))
print(starts_with.__name__)