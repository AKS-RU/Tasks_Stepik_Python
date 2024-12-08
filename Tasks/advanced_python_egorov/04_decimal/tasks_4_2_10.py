# Создайте в переменной num число 0.000874 типа Decimal на основании кортежа и
# выведите его на экран


from decimal import Decimal


num = Decimal((0, (8, 7, 4), -6))
print(num)
