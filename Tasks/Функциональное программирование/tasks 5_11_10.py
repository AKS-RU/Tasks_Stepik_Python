#                               Декоратор add_args
# Напишите декоратор add_args, который добавляет к переданным аргументам еще два значения: строку «begin» в начало
# аргументов, строку «end» в конец. Также декоратор должен сохранить первоначальное имя декорируемой функции и ее
# строку документации
#
# Sample Input 1:
#
# @add_args
# def concatenate(*args):
#     """
#     Возвращает конкатенацию переданных строк
#     """
#     return ', '.join(args)
#
#
# print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
# print(concatenate('my', 'name is', 'Artem'))
# print(concatenate.__name__)
# print(concatenate.__doc__.strip())
# Sample Output 1:
#
# begin, hello, world, my, name is, Artem, end
# begin, my, name is, Artem, end
# concatenate
# Возвращает конкатенацию переданных строк
# Sample Input 2:
#
# @add_args
# def find_max_word(*args):
#     """
#     Возвращает слово максимальной длины
#     """
#     return max(args, key=len)
#
# print(find_max_word('my'))
# print(find_max_word('my', 'how'))
# print(find_max_word('my', 'how', 'maximum'))
# print(find_max_word.__name__)
# print(find_max_word.__doc__.strip())
# Sample Output 2:
#
# begin
# begin
# maximum
# find_max_word
# Возвращает слово максимальной длины


from functools import wraps


def add_args(func):
    @wraps(func)
    def inner_add_args(*args):
        args = [i for i in args]
        args.insert(0, 'begin')
        args.append('end')
        return func(*args)
    return inner_add_args


@add_args
def concatenate(*args):
    """
    Возвращает конкатенацию переданных строк
    """
    return ', '.join(args)


@add_args
def find_max_word(*args):
    """
    Возвращает слово максимальной длины
    """
    return max(args, key=len)

print(find_max_word('my'))
print(find_max_word('my', 'how'))
print(find_max_word('my', 'how', 'maximum'))
print(find_max_word.__name__)
print(find_max_word.__doc__.strip())