# Функция make_repeater
# Ваша задача создать функцию-замыкание make_repeater, которая должна дублировать переданную в нее строку N раз.
# При создании замыкания передается число N - количество для повторения.
#
# Sample Input 1:
#
# repeat_5 = make_repeater(5)
# print(repeat_5('Hello'))
# print(repeat_5('World'))
#
# repeat_2 = make_repeater(2)
# print(repeat_2('Pizza'))
# print(repeat_2('Pasta'))
# Sample Output 1:
#
# HelloHelloHelloHelloHello
# WorldWorldWorldWorldWorld
# PizzaPizza
# PastaPasta
# Sample Input 2:
#
# repeat_3 = make_repeater(3)
# print(repeat_3('Soup'))
# print(repeat_3('Frank'))
#
# repeat_4 = make_repeater(4)
# print(repeat_4('Gusi'))
# print(repeat_4('GagaGa'))
# Sample Output 2:
#
# SoupSoupSoup
# FrankFrankFrank
# GusiGusiGusiGusi
# GagaGaGagaGaGagaGaGagaGa



def make_repeater(n):
    def text_repeater(text):
        return text*n
    return text_repeater



repeat_3 = make_repeater(3)
print(repeat_3('Soup'))
print(repeat_3('Frank'))

repeat_4 = make_repeater(4)
print(repeat_4('Gusi'))
print(repeat_4('GagaGa'))