# Вам дан английский текст. Закодируйте его с помощью азбуки Морзе.Каждая буква заменяется на последовательность
# точек и тире. В качестве тире используйте обычный дефис: «-», а в качестве точки — точку «.». Например, буква «g»
# превратится в трёхсимвольную строку «--.». Ниже в переменной morze для вашего удобства хранится словарь соответствия
# английских букв коду Морзе.
#
# Формат ввода
# Весь текст записан в единственной строке. Текст состоит из английских букв и пробелов, других символов в тексте нет.
# В тексте не может быть двух или более пробелов подряд.
#
# Формат вывода
# Выведите каждое слово исходного текста, закодированное азбукой Морзе, на отдельной строке. Количество строк в ответе
# должно совпадать с количеством слов в исходном тексте. Между закодированными буквами нужно ставить ровно один пробел.
# Например, слово «Help» превратится в «.... . .-.. .--.». Обратите внимание, что строчные и заглавные буквы кодируются
# одинаково.
#
# Sample Input:
#
# Houston we have a problem
# Sample Output:
#
# •••• ——— ••— ••• — ——— —•
# •—— •
# •••• •— •••— •
# •—
# •——• •—• ——— —••• •—•• • ——

morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}



for i in input().lower():
    if i.isspace():
        print()
    else:
        print(morze.get(i), end=' ')
