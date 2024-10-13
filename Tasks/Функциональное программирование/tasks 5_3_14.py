# Имеется функция sale, которая возвращает цену товара со скидкой 10%.
#
# def sale(x):
#     return x*0.9
# Однако мы изучаем анонимные функции, поэтому на основе данной функции создайте анонимную
# функцию и присвойте её переменной sale_lambda
#
# Sample Input 1:
#
# print(sale_lambda.__name__)
# print(sale_lambda(4))
# Sample Output 1:
#
# <lambda>
# 3.6
# Sample Input 2:
#
# print(sale_lambda.__name__)
# print(sale_lambda(15))
# Sample Output 2:
#
# <lambda>
# 13.5
# Sample Input 3:
#
# print(sale_lambda(100))
# Sample Output 3:
#
# 90.0

sale_lambda = lambda x: x * 0.9

print(sale_lambda.__name__)
print(sale_lambda(15))
