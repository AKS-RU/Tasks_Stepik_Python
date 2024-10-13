#                     Напишите простой интерпретатор математического выражения.
#
# На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором:
# a operator b
# a operator b, где вместо operator могут использоваться следующие слова:
# plus, minus, multiply, divide для, соответственно, сложения,
# вычитания, умножения и целочисленного деления.
#
# Формат ввода:
# Одна строка, содержащая выражение вида a operator 0≤a,b≤1000. Оператор может быть plus, minus, multiply, divide.
#
# Формат вывода:
# Строка, содержащая целое число
# −
# − результат вычисления.
# -------------------------------------------------------------------------------------------------------------------


def calculator(a, operator, b):
    calc_dic = {
        'plus': lambda a, b: a + b,
        'minus': lambda a, b: a - b,
        'multiply': lambda a, b: a * b,
        'divide': lambda a, b: a // b if b != 0 else 'На ноль делить нельзя'
    }
    return calc_dic[operator](a, b)


def inp(lst):
    a, operator, b = tuple(lst)
    a, b = int(a), int(b)
    return calculator(a, operator, b)


print(inp(input().split()))

if __name__ == '__main__':
    assert calculator(45, 'plus', 8) == 53
    assert calculator(12, 'minus', 42) == -30
    assert calculator(451, 'multiply', 2) == 902
    assert calculator(13, 'divide', 3) == 4
    assert calculator(45, 'divide', 0) == 'На ноль делить нельзя'
    print('Всё успешно!')
