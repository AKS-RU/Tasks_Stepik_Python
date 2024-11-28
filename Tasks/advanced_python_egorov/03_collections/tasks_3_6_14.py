# Перед вами список кортежей sales, в котором элемент представляет собой информацию о
# товаре и значении его продажи

# Напишите программу которая агрегирует сумму продаж по каждому отдельному товара и выведет
# название товара-бестселлера и найденное общее его значение продаж в формате

# Название товара - ИтоговаяСумма
# Например, если в нашем распоряжении имеется такой список sales

# sales = [('Clothing', 5.0),
#          ('Clothing', 6.0),
#          ('Outdoor', 7.0),
#          ('Grocery', 2.0),
#          ('Grocery', 3.0),
#          ('Grocery', 2.0)]
# то ответом была бы следующая строка

# Clothing - 11.0

from collections import defaultdict


sales = [('Office Supplies', 1800.0),
         ('Clothing', 4200.32),
         ('Outdoor', 3800.0),
         ('Grocery', 2000.0),
         ('Grocery', 2500.0),
         ('Automotive', 4800.53),
         ('Tools', 4500.0),
         ('Tools', 3900.0),
         ('Home Appliances', 6900.0),
         ('Office Supplies', 2100.0),
         ('Jewelry', 3200.0),
         ('Office Supplies', 2500.0),
         ('Books', 1800.5),
         ('Sporting Goods', 3100.5),
         ('Jewelry', 3800.0),
         ('Sporting Goods', 3200.6),
         ('Jewelry', 2700.5),
         ('Outdoor', 4200.0),
         ('Outdoor', 2900.0),
         ('Toys', 2500.0),
         ('Clothing', 5100.0),
         ('Clothing', 5000.8),
         ('Sporting Goods', 3800.24),
         ('Grocery', 1800.25),
         ('Electronics', 4200.0),
         ('Outdoor', 4800.0),
         ('Toys', 1600.0),
         ('Sporting Goods', 2700.0),
         ('Electronics', 3100.0),
         ('Home Appliances', 8300.0),
         ('Books', 1500.0),
         ('Electronics', 4800.0),
         ('Tools', 5200.0),
         ('Sporting Goods', 4300.0),
         ('Home Appliances', 7500.3),
         ('Automotive', 4100.05),
         ('Home Appliances', 6400.0),
         ('Toys', 1900.0),
         ('Electronics', 3500.24),
         ('Tools', 4800.0),
         ('Electronics', 2900.43),
         ('Grocery', 1500.43),
         ('Jewelry', 3000.0),
         ('Tools', 5800.5),
         ('Automotive', 5400.53),
         ('Toys', 1850.0),
         ('Outdoor', 3500.32),
         ('Books', 2500.0),
         ('Jewelry', 2400.0),
         ('Books', 2700.4),
         ('Clothing', 6300.0),
         ('Clothing', 4800.3),
         ('Home Appliances', 7900.3),
         ('Books', 2000.7),
         ('Automotive', 5000.07),
         ('Automotive', 3900.0),
         ('Office Supplies', 2700.5),
         ('Grocery', 1200.0),
         ('Toys', 2200.5),
         ('Office Supplies', 2200.0)]


result = defaultdict(int)

for key, value in sales:
    result[key] += value

result = sorted(result.items(), key=lambda x: (-x[1], x[0]))[0]

print(f'{result[0]} - {result[1]}')
