# Расчет значений
# По вводимому значению переменной x найдите, чему будет равно значение следующей формулы:

# f(x)=e**sqr(x)/2

# Здесь переменная e представляет собой  основание натурального логарифма, или ее еще называют
# числом Эйлера. В качестве значения e возьмите 2.71828.

# В качестве ответа распечатайте найденное значение


from decimal import Decimal


x = Decimal(input())
e = Decimal('2.71828')

result = e**(x.sqrt()/2)

print(result)
