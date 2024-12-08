# Перед вами имеется функция mul

# def mul(x, y):
#     return x * y
# которая выполняет умножение двух  чисел

# Создайте на ее основе еще две функции

# double
# triple
# которые выполняют умножение на 2 и на 3 соответственно
from functools import partial


def mul(x, y):
    return x * y


double = partial(mul, 2)
triple = partial(mul, 3)

print(double(8))
print(triple(8))
