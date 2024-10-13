# Ваша задача написать функцию add_item, которая добавляет в корзину (глобальная переменная shopping_list) товар и
# его количество.
#
# Функция add_item обязательно должна принимать имя товара и необязательно - его количество (по умолчанию оно равно 1)
#
# Sample Input 1:
#
# add_item("Bread")
# add_item("Milk", 2)
# print(shopping_list)
# Sample Output 1:
#
# {'Bread': 1, 'Milk': 2}
# Sample Input 2:
#
# add_item("Bread", 10)
# add_item("Potato", 5)
# add_item("Milk")
# add_item("Orange", 3)
# add_item("Orange", 2)
# add_item("Milk")
# add_item("Bread", 3)
#
# print(shopping_list)
# Sample Output 2:
#
# {'Bread': 13, 'Potato': 5, 'Milk': 2, 'Orange': 5}

shopping_list = {}


def add_item(product: str, quantily=1):
    global shopping_list
    shopping_list[product] = shopping_list.setdefault(product, 0) + quantily


add_item("Bread", 10)
add_item("Potato", 5)
add_item("Milk")
add_item("Orange", 3)
add_item("Orange", 2)
add_item("Milk")
add_item("Bread", 3)

print(shopping_list)
