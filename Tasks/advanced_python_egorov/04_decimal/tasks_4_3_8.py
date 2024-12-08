# Распечатайте значение числа
# sqrt(2)
# где количество знаков после запятой изменяется от 2 до 50 включительно.

# Каждое значение необходимо вывести на отдельной строке

from decimal import Decimal, Context, getcontext

const = Decimal(2)
my_context = getcontext()
my_context.prec = 3
result = ''

while len(str(result)) <= 51:
    result = const.sqrt()
    print(result)
    my_context.prec += 1
