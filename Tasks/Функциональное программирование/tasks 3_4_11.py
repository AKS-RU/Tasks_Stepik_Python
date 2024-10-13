# Напишите функцию show_list, которая выводит список товаров из корзины (глобальная переменная shopping_list).
# У функции show_list есть необязательный логический параметр include_quantities, по умолчанию принимает значение True.
#
# Если include_quantities имеет значение правда, вы должны выводить имя товара и его количество в формате
#
# {количество}x{имя_товара},
#
# иначе выводите только имя.
#
# Напишите только реализацию функции show_list
#
# Sample Input 1:
#
# shopping_list = {'Bread': 13, 'Potato': 5, 'Milk': 2, 'Orange': 5}
# show_list()
# Sample Output 1:
#
# 13xBread
# 5xPotato
# 2xMilk
# 5xOrange
# Sample Input 2:
#
# shopping_list = {'Bread': 13, 'Potato': 5, 'Milk': 2, 'Orange': 5}
# show_list(include_quantities=False)
# Sample Output 2:
#
# Bread
# Potato
# Milk
# Orange
# Sample Input 3:
#
# shopping_list = {'Bread': 1, 'Milk': 2}
# show_list(include_quantities=True)
# Sample Output 3:
#
# 1xBread
# 2xMilk

shopping_list = {'Bread': 13, 'Potato': 5, 'Milk': 2, 'Orange': 5}


def show_list(include_quantities=True):
    print(*(f'{value}x{key}' if include_quantities else key for key, value in shopping_list.items()), sep='\n')


show_list(False)
