# Декоратор cache_result
# Кэширование – это способ оптимизации работы приложения, при котором повторно запрашиваемые данные сохраняются и далее
# используются для обслуживания последующих запросов. Кешом называется место, куда будут сохраняться данные после
# первого вызова.
#
# Ваша задача написать декоратор cache_result, который оптимизирует производительность за счет сохранения и извлечения
# результатов функций, устраняя избыточные вычисления для повторяющихся входных данных и улучшая скорость отклика
# приложения, особенно для длительных вычислений.
#
# Взгляните на пример ниже
#
# @cache_result
# def multiply(a, b):
#     return f"Product = {a * b}"
#
# print(multiply(4, 5))  # Вызываем 1й раз функцию с аргументами 4 и 5. Идет сохранение результата
#
# print(multiply(4, 5))  # При повторном вызове достаем из кеша
#
# print(multiply(5, 8))  # Впервые вызывает с аргументами 5 и 8
# print(multiply(5, 8))  # Достаем из кеша результат вызова multiply(5, 8)
# print(multiply(5, 8))  # Вновь достаем из кеша
#
# print(multiply(-3, 7))  # Впервые вычисляем результат вызова multiply(-3, 7), сохраняем в кеше
# print(multiply(-3, 7))  # Достаем из кеша multiply(-3, 7)
# Декоратор cache_result должен сохранять результат вызова оригинальной функции с учетом передаваемых аргументов.
#
# При повторном вызове функции с теми же аргументами, результат должен возвращаться из кеша, предварительно
# сопроводив выводом следующего текста на экран
#
# [FROM CACHE] Вызов {имя_функции} = {результат_из_кеша}
# Ваша задача написать только функцию-декоратор cache_result
#
# Sample Input 1:
#
# @cache_result
# def multiply(a, b):
#     return a * b
#
#
# print(multiply(4, 5))
# print(multiply(4, 5))
# print(multiply(4, 5))
# print(multiply(5, 4))
# print(multiply.__name__)
# Sample Output 1:
#
# 20
# [FROM CACHE] Вызов multiply = 20
# 20
# [FROM CACHE] Вызов multiply = 20
# 20
# 20
# multiply
# Sample Input 2:
#
# @cache_result
# def add(a, b):
#     return a + b
#
# print(add(4, 4)) # 1й раз с такими атрибутами
# print(add(4, 5)) # 1й раз с такими атрибутами
# print(add(4, 6)) # 1й раз с такими атрибутами
# print(add(4, 5)) # достаем из кеша
# print(add(5, 4)) # 1й раз с такими атрибутами
# print(add(6, 3)) # 1й раз с такими атрибутами
# print(add(a=6, b=3)) # 1й раз с такими атрибутами: позицицинные!=именованные
# print(add(a=6, b=3)) # достаем из кеша
# Sample Output 2:
#
# 8
# 9
# 10
# [FROM CACHE] Вызов add = 9
# 9
# 9
# 9
# 9
# [FROM CACHE] Вызов add = 9
# 9


from functools import wraps


def cache_result(func):
    args_dict = {}
    kwargs_dict = {}
    @wraps(func)
    def dec_cache_result(*args, **kwargs):
        if len(args):
            if args in args_dict:
                print(f'[FROM CACHE] Вызов {func.__name__} = {args_dict.get(args)}')
                return args_dict.get(args)
            else:
                args_dict.setdefault(args, func(*args, **kwargs))
                return func(*args, **kwargs)
        elif len(kwargs):
            kwargs_key=tuple(v for v in kwargs.values())
            if kwargs_key in kwargs_dict:
                print(f'[FROM CACHE] Вызов {func.__name__} = {kwargs_dict.get(kwargs_key)}')
                return kwargs_dict.get(kwargs_key)
            else:
                kwargs_dict.setdefault(kwargs_key, func(*args, **kwargs))
                return func(*args, **kwargs)
    return dec_cache_result


@cache_result
def add(a, b):
    return a + b


print(add(4, 4))  # 1й раз с такими атрибутами
print(add(4, 5))  # 1й раз с такими атрибутами
print(add(4, 6))  # 1й раз с такими атрибутами
print(add(4, 5))  # достаем из кеша
print(add(5, 4))  # 1й раз с такими атрибутами
print(add(6, 3))  # 1й раз с такими атрибутами
print(add(a=6, b=3))  # 1й раз с такими атрибутами: позицицинные!=именованные
print(add(a=6, b=3))  # достаем из кеша
