# Декоратор convert_to
# Напишите декоратор convert_to, который позволяет автоматически преобразовать возвращаемое значение в указанный тип
# данных. Функция-декоратор convert_to имеет обязательный параметр type_, в который необходимо передать тип данных
# для дальнейшего преобразования.
#
# Sample Input 1:
#
# @convert_to(int)
# def add_values(a, b):
#     return a + b
#
#
# result = add_values(10, 20)
# print(f"Результат: {result}, тип результата {type(result)}")
# Sample Output 1:
#
# Результат: 30, тип результата <class 'int'>
# Sample Input 2:
#
# @convert_to(str)
# def add_values(a, b):
#     return a + b
#
#
# result = add_values(10, 20)
# print(f"Результат: {result}, тип результата {type(result)}")
# Sample Output 2:
#
# Результат: 30, тип результата <class 'str'>
# Sample Input 3:
#
# @convert_to(list)
# def add_values(a, b):
#     return a + b
#
#
# result = add_values('hello', 'world')
# print(f"Результат: {result}, тип результата {type(result)}")
# Sample Output 3:
#
# Результат: ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd'], тип результата <class 'list'>


from functools import wraps


def convert_to(type: str):
    def decorator(func):

        @wraps(func)
        def dec_inner(*args, **kwargs):
            return type(func(*args, **kwargs))
        return dec_inner
    return decorator


@convert_to(list)
def add_values(a, b):
    return a + b


result = add_values('hello', 'world')
print(f"Результат: {result}, тип результата {type(result)}")