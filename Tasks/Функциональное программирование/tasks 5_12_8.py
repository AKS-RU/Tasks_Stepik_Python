#
#               Декоратор limit_query с параметром
# Ваша задача переписать декоратор limit_query так, чтобы он ограничивал разрешенное количество вызовов оригинальной
# функции по переданному параметру limit. Когда декорируемая функция исчерпает лимит вызовов, необходимо выводить
# на экран фразу
#
#  «Лимит вызовов закончен, все <limit> попытки израсходованы»
#
# Если лимит исчерпан, оригинальная функция не должна быть вызвана, декоратор возвращает None
#
# Sample Input:
#
# @limit_query(3)
# def add(a: int, b: int):
#     return a + b
#
# print(add(4, 5))
# print(add(5, 8))
# print(add(9, 43))
# print(add(10, 33))
# print(add.__name__)
# Sample Output:
#
# 9
# 13
# 52
# Лимит вызовов закончен, все 3 попытки израсходованы
# None
# add



from functools import wraps


def limit_query(n: int):
    def decorator(func):
        cnt=0
        @wraps(func)
        def dec_inner(*args, **kwargs):
            nonlocal cnt
            cnt+=1
            if cnt<=n:
                return func(*args, **kwargs)
            else:
                print(f'Лимит вызовов закончен, все {n} попытки израсходованы')
        return dec_inner
    return decorator




@limit_query(3)
def add(a: int, b: int):
    return a + b

print(add(4, 5))
print(add(5, 8))
print(add(9, 43))
print(add(10, 33))
print(add.__name__)