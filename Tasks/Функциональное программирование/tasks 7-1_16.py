# Напишите функцию-генератор my_enumerate, которая копирует работу встроенной функции enumerate.
#
# Sample Input 1:
#
# lessons = ["Что такое функция", "Возвращаемое значение",
#            "Параметры и аргументы функции",
#            "Чистая функция", "Параметр *args"]
#
# for i, lesson in my_enumerate(lessons):
#     print("Урок {}: {}".format(i, lesson))
# Sample Output 1:
#
# Урок 0: Что такое функция
# Урок 1: Возвращаемое значение
# Урок 2: Параметры и аргументы функции
# Урок 3: Чистая функция
# Урок 4: Параметр *args
# Sample Input 2:
#
# lessons = ["Что такое функция", "Возвращаемое значение",
#            "Параметры и аргументы функции",
#            "Чистая функция", "Параметр *args", "Параметр **kwargs"]
#
# for i, lesson in my_enumerate(lessons, 1):
#     print("Урок {}: {}".format(i, lesson))
# Sample Output 2:
#
# Урок 1: Что такое функция
# Урок 2: Возвращаемое значение
# Урок 3: Параметры и аргументы функции
# Урок 4: Чистая функция
# Урок 5: Параметр *args
# Урок 6: Параметр **kwargs


