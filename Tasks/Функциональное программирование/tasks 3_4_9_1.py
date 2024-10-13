# Заменяем символы
# Напишите функцию replace, которая принимает три параметра:
#
# обязательный строковый параметр text - текст, в котором необходимо выполнить замены;
# обязательный строковый параметр old - строка поиска для замены;
# необязательный строковый параметр new - значение замены для найденного значения old. По умолчанию равен пустой
# строке.
# Функция replace должна возвращать новую строку, в которой все символы old были заменены на new. При замене регистр
# букв должен учитываться
#
# replace('Нет', 'т') => 'Не'
# replace('Bella Ciao', 'a') => 'Bell Cio'
# replace('nobody; i myself farewell analysis', 'l', 'z') => 'nobody; i mysezf farewezz anazysis'
# replace('commend me to my kind lord meaning', 'M', 'w') => 'commend me to my kind lord meaning'
# Ваша задача дописать только тело функции replace
#
# Sample Input 1:
#
# print(replace('Нет', 'т'))
# Sample Output 1:
#
# Не
# Sample Input 2:
#
# print(replace('Bella Ciao', 'a'))
# Sample Output 2:
#
# Bell Cio
# Sample Input 3:
#
# print(replace('nobody; i myself farewell analysis', 'l', 'z'))
# Sample Output 3:
#
# nobody; i mysezf farewezz anazysis


def replace(text: str, old: str, new: str = '') -> str:
    return text.replace(old, new)


print(replace('Bella Ciao', 'a'))
