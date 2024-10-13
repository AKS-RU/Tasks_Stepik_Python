# Напишите функцию concatenate(), которая принимает произвольное число именованных аргументов и объединяет их в одну
# большую строку без разделителей.
#
# Вам необходимо написать только определение функции concatenate
#
# Обратите внимание, что передаваемые значения могут быть различных типов данных
#
# Sample Input 1:
#
# print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))
# Sample Output 1:
#
# ЯВыучуЭтотПитон!
# Sample Input 2:
#
# print(concatenate(first='i got ', second=5, third=" stars"))
# Sample Output 2:
#
# i got 5 stars
# Sample Input 3:
#
# print(concatenate(t='Happy', y="Meal", w="Cost", m=10, b='Buks'))
# Sample Output 3:
#
# HappyMealCost10Buks
# Sample Input 4:
#
# print(concatenate(q='iHave', w="next", e="Coins", r=[10, 5, 10, 7]))
# Sample Output 4:
#
# iHavenextCoins[10, 5, 10, 7]

def concatenate(**kwargs):
    phrase = [f'{value}'for value in kwargs.values()]
    phrase = ''.join(phrase)
    return phrase


print(concatenate(q='iHave', w="next", e="Coins", r=[10, 5, 10, 7]))