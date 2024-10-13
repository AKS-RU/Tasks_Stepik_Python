# Определите функцию get_reverse, которая принимает строку, разворачивает ее и возвращает полученный результат
# строки.
#
# Ваша задача написать только определение функции get_reverse
#
# Sample Input 1:
#
# print(get_reverse("I am testing string"))
# Sample Output 1:
#
# gnirts gnitset ma I
# Sample Input 2:
#
# print(get_reverse("It's cool, isn't it?"))
# Sample Output 2:
#
# ?ti t'nsi ,looc s'tI
# Sample Input 3:
#
# print(get_reverse("Hello, my friend"))
# Sample Output 3:
#
# dneirf ym ,olleH

def get_reverse(st: str):
    return st[::-1]

print(get_reverse('aaasssddd'))