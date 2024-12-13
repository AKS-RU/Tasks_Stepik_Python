# Получение K-ой перестановки
# Пользуемся генерацией перестановок из предыдущего задания, что получить значение k-ой по
# алфавитному порядку перестановки.

# Ваша программа получает на вход в первой строке число N (N <= 26) – количество первых букв в
# перестановке, во второй – число K (1 <= K <= N!) – номер перестановки.

# Ваша задача вывести на экран значение искомой перестановки

from itertools import permutations
from string import ascii_uppercase

number_chars = int(input())
number_permut = int(input())
for count, value in enumerate(permutations(ascii_uppercase[:number_chars])):
    if count+1 == number_permut:
        print(' '.join(map(str, value)))
        break
