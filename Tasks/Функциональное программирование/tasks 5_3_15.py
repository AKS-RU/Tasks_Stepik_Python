# Хорошо постарались с прошлой задачей! Однако мы забыли, что скидка должна быть только для
# тех товаров, стоимость которых больше 50. Вам стоит внести это изменение в прошлый код
#
# Ваша задача только переопределить переменную sale_lambda
#
# Sample Input 1:
#
# print(sale_lambda.__name__)
# print(sale_lambda(50.0))
# Sample Output 1:
#
# <lambda>
# 50.0
# Sample Input 2:
#
# print(sale_lambda(60.0))
# print(sale_lambda.__name__)
# Sample Output 2:
#
# 54.0
# <lambda>
# Sample Input 3:
#
# print(sale_lambda(12.33))
# Sample Output 3:
#
# 12.33


sale_lambda = lambda x: x * 0.9 if x > 50 else x


print(sale_lambda(12.33))