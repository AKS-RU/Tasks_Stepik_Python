#                               Декоратор counting_calls
# Реализуйте декоратор counting_calls, который будет подсчитывать количество вызовов оригинальной функции.
#
# После декорирования при помощи counting_calls у функции должен появиться атрибут call_count, который отслеживает
#  текущее количество вызовов.
#
# Sample Input 1:
#
# @counting_calls
# def add(a: int, b: int) -> int:
#     '''Возвращает сумму двух чисел'''
#     return a + b
#
#
# print(add.__name__)
# print(add.__doc__)
#
# print(add(10, b=20))
# print(add.call_count)
# print(add(30, 5))
# print(add.call_count)
# Sample Output 1:
#
# add
# Возвращает сумму двух чисел
# 30
# 1
# 35
# 2
# Sample Input 2:
#
# @counting_calls
# def add(a: int, b: int) -> int:
#     '''Возвращает сумму двух чисел'''
#     return a + b
#
# print(add(10, b=20))
# print(add(30, 5))
# print(add(3, 5))
# print(add(4, 5))
# print('Количество вызовов =', add.call_count)
# print(add(11, 5))
# print('Количество вызовов =', add.call_count)
# Sample Output 2:
#
# 30
# 35
# 8
# 9
# Количество вызовов = 4
# 16
# Количество вызовов = 5




def counting_calls(func):
    func.call_count = 0
    def dec_counting_calls(*args, **kwargs):
        dec_counting_calls.call_count += 1
        return func(*args, **kwargs)

    dec_counting_calls.__name__ = func.__name__
    dec_counting_calls.__doc__ = func.__doc__
    dec_counting_calls.call_count = func.call_count
    return dec_counting_calls




@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b


print(add.__name__)
print(add.__doc__)

print(add(10, b=20))
print(add.call_count)
print(add(30, 5))
print(add.call_count)
