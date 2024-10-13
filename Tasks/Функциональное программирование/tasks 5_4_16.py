# Сортировка товаров - 2
# Поставщик скидывает нашему заказчику информацию о товарах, а он хочет взглянуть на нее в отсортированном виде.
# Заказчик хочет видеть вывод, где вверху самые дорогие товары, внизу самые дешевые.
#
# Вот только поставщик предоставляет данные в виде списка строк, где каждая строка хранит информацию о товаре в виде
#
# Название_товара: цена_товара
# Название товара отделено от цены знаком двоеточия :.
#
# Ваша задача написать функцию print_goods , которая принимает список строк. Далее print_goods  должна выводить
# информацию о товарах, сортируя их сперва по цене, а затем по алфавиту без учета регистра. Вывод информации о
# каждом товаре делается в отдельной строке в следующем формате
#
# Цена_товара - Название_товара
# Цена должна выводиться с точностью до двух знаком после запятой
#
# Sample Input 1:
#
# data = [
#     'Sony PlayStation 5: 46000',
#     'Телевизор QLED Samsung QE65Q60TAU: 87090',
#     'Смартфон Samsung Galaxy A11: 10000',
#     'Планшет Samsung Galaxy Tab S6: 26600',
# ]
#
# print_goods(data)
# Sample Output 1:
#
# 87090.00 - Телевизор QLED Samsung QE65Q60TAU
# 46000.00 - Sony PlayStation 5
# 26600.00 - Планшет Samsung Galaxy Tab S6
# 10000.00 - Смартфон Samsung Galaxy A11
# Sample Input 2:
#
# data = [
#     'Sony PlayStation 5: 46000.5',
#     'Телевизор QLED Samsung QE65Q60TAU: 87090',
#     'Samsung Galaxy s23: 46000.5',
#     'siemens eq.6 plus s100: 46000.5',
#     'Samsung Galaxy Tab S6: 46000.5',
# ]
# print_goods(data)
# Sample Output 2:
#
# 87090.00 - Телевизор QLED Samsung QE65Q60TAU
# 46000.50 - Samsung Galaxy s23
# 46000.50 - Samsung Galaxy Tab S6
# 46000.50 - siemens eq.6 plus s100
# 46000.50 - Sony PlayStation 5
# Sample Input 3:
#
# data = [
#     'a: 1',
#     'aa: 2',
#     'aA: 3',
#     'Aa: 4',
#     'Aa: 5',
#     'AA: 5',
#     'aa: 5',
#     'aA: 5',
# ]
# print_goods(data)
# Sample Output 3:
#
# 5.00 - Aa
# 5.00 - AA
# 5.00 - aa
# 5.00 - aA
# 4.00 - Aa
# 3.00 - aA
# 2.00 - aa
# 1.00 - a


def print_goods(lst: list)->list:
    result = [i.split(':') for i in lst]
    [print(f'{float(j):.2f} - {i}') for i,j in sorted(result,key=lambda x: (-float(x[1]), x[0].upper()))]




data = [
    'Sony PlayStation 5: 46000.5',
    'Телевизор QLED Samsung QE65Q60TAU: 87090',
    'Samsung Galaxy s23: 46000.5',
    'siemens eq.6 plus s100: 46000.5',
    'Samsung Galaxy Tab S6: 46000.5',
]
print_goods(data)