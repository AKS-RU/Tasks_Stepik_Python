# Напишите функцию print_goods, которая принимает список словарей. В самих словарях хранится информация о товарах:
# имя, модель и цвет. Задача функции print_goods вывести на экран информацию о товарах  в следующем формате
#
# Производитель: <make>, модель: <model>, цвет: <color>
# при этом товары должны быть отсортированы по цвету в лексикографическом порядке (по алфавиту) без учета регистра
# и по убыванию модели (второй критерий сортировки)
#
# Sample Input 1:
#
# models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#           {'make': 'Apple', 'model': 10, 'color': 'Silver'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
#           {'make': 'Honor', 'model': 3, 'color': 'Black'}]
# print_goods(models)
# Sample Output 1:
#
# Производитель: Nokia, модель: 216, цвет: Black
# Производитель: Honor, модель: 3, цвет: Black
# Производитель: Samsung, модель: 7, цвет: Blue
# Производитель: Mi Max, модель: 2, цвет: Gold
# Производитель: Huawei, модель: 4, цвет: Grey
# Производитель: Oppo, модель: 9, цвет: Red
# Производитель: Apple, модель: 10, цвет: Silver
# Sample Input 2:
#
# models = [{'make': 'Nokia', 'model': 2, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 3, 'color': 'red'},
#           {'make': 'Samsung', 'model': 5, 'color': 'Yellow'},
#           {'make': 'Apple', 'model': 10, 'color': 'RED'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'BLACK'},
#           {'make': 'Honor', 'model': 3, 'color': 'black'},
#           {'make': 'Nothing Phone', 'model': 7, 'color': 'Yellow'}]
# print_goods(models)
# Sample Output 2:
#
# Производитель: Huawei, модель: 4, цвет: BLACK
# Производитель: Honor, модель: 3, цвет: black
# Производитель: Nokia, модель: 2, цвет: Black
# Производитель: Apple, модель: 10, цвет: RED
# Производитель: Oppo, модель: 9, цвет: Red
# Производитель: Mi Max, модель: 3, цвет: red
# Производитель: Nothing Phone, модель: 7, цвет: Yellow
# Производитель: Samsung, модель: 5, цвет: Yellow


def print_goods(lst: list):
    for i in sorted(models, key=lambda x: (x['color'].upper(), -x['model'])):
        print(f"Производитель: {i['make']}, модель: {i['model']}, цвет: {i['color']}")



models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
          {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
          {'make': 'Apple', 'model': 10, 'color': 'Silver'},
          {'make': 'Oppo', 'model': 9, 'color': 'Red'},
          {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
          {'make': 'Honor', 'model': 3, 'color': 'Black'}]
print_goods(models)