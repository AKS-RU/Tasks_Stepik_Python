# В вашем распоряжении имеется два списка: suits хранит в себе масти карт, а в ranks содержит
# номинал карт.

# Ваша задача сгенерировать всю колоду карт при помощи itertools.product и вывести информацию о
# каждой карте на экран в определенном формате (см. пример вывода). В итоге у вас должно
# получиться 52 карты

# В suits хранятся юникод символы, при выводе на экран они будут преобразованы в  ♣ ♥ ♦ ♠

import itertools


suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
ranks = ['2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'J', 'Q', 'K', 'A']

for i in itertools.product(ranks, suits):
    print(f'{i[0]} of {i[1]}')
