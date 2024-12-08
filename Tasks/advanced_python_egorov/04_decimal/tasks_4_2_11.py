# Создайте в переменной num число -1230000 типа Decimal на основании кортежа и выведите
# его на экран


from decimal import Decimal


num = Decimal((1, (1, 2, 3), 4))
print(num)
