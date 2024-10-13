# Напишите функцию info_kwargs, которая принимает произвольное количество именованных аргументов.
#
# Функция info_kwargs должна распечатать именованные аргументы (каждый на новой строке) в виде пар «ключ = значение», где ключи должны следовать в алфавитном порядке.
#
# Вам необходимо написать только определение функции info_kwargs
#
# Sample Input 1:
#
# info_kwargs(first_name="John", last_name="Doe", age=33)
# Sample Output 1:
#
# age = 33
# first_name = John
# last_name = Doe
# Sample Input 2:
#
# info_kwargs(c=43, b= 32, a=32)
# Sample Output 2:
#
# a = 32
# b = 32
# c = 43
# Sample Input 3:
#
# info_kwargs(b=3,c=2,a=1)
# Sample Output 3:
#
# a = 1
# b = 3
# c = 2
# Sample Input 4:
#
# info_kwargs(cool='hello')
# Sample Output 4:
#
# cool = hello


def info_kwargs(**kwargs):
    print(*(f'{key} = {kwargs[key]}' for key in sorted(kwargs)), sep='\n')


info_kwargs(cool='hello')

