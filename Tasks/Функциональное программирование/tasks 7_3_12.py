# В вашем распоряжении имеется глобальная переменная DICTIONARY, представляющая собой словарь, где ключами являются
# английские буквы, а значениями - слова, начинающиеся с буквы ключа. Начальное заполнение DICTIONARY имеет следующий
# вид:
#
# DICTIONARY = {
#     'a': 'apple',
#     'b': 'banana',
#     'c': 'cat',
#     'd': 'dog',
#     ...
# }
# Ваша задача — написать сопрограмму alphabet, в которую передаются буквы, а в ответ она генерирует слова, закрепленные
# переданной буквой из словаря DICTIONARY.
#
# Гарантируется, что в alphabet будут поступать значения, которые имеются в ключах словаря DICTIONARY.
#
# Сама переменная DICTIONARY вам в редакторе кода невидно, но вы можете обращаться к ней внутри сопрограммы alphabet.
#
# Sample Input 1:
#
# coro = alphabet()
# next(coro)
# print(coro.send('a'))
# print(coro.send('b'))
# print(coro.send('c'))
# Sample Output 1:
#
# apple
# banana
# cat
# Sample Input 2:
#
# coro = alphabet()
# next(coro)
# for letter in 'qwerty':
#     print(coro.send(letter))
# Sample Output 2:
#
# quail
# walrus
# elephant
# rabbit
# tiger
# yak


DICTIONARY = {
    'a': 'apple',
    'b': 'banana',
    'c': 'cat',
    'd': 'dog',
    'q': 'quail',
    'w': 'walrus',
    'e':'elephant',
    'r':'rabbit',
    't':'tiger',
    'y':'yak'
}


def alphabet():
    a = yield
    while True:
        try:
            if a in DICTIONARY.keys() or a == 'default':
                a = yield DICTIONARY.get(a)
            else:
                raise KeyError
        except KeyError:
            a = yield 'default'


coro = alphabet()
next(coro)
print(coro.send('apple'))
print(coro.send('banana'))
print(coro.throw(KeyError))
print(coro.send('dog'))
print(coro.send('d'))
