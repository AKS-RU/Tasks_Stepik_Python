# Функция aggregation
# Реализуйте функцию aggregation, которая принимает на вход функцию func и коллекцию элементов sequence.
#
# Функция func будет принимать только два элемента.
#
# Задача функции aggregation уметь накапливать результат вычисления функции func путем последовательного применения
# ее ко всем элементам. Но так как функция func умеет работать только с двумя значениями, вам необходимо передавать
# элементы последовательно парами. В результате у вас должен получиться список, в котором копятся результаты работы
# функции aggregation
#
# Пример, в качестве func возьмем функцию
#
# def get_add(x, y):
#     return x + y
# Коллекцией у нас будет следующий список
#
# numbers = [5, 2, 4, 3, 5]
# Применяя func к первым элементам коллекции 5 и 2, получим сумму 7. Это первое наше агрегированное значение
#
# Далее берем уже накопленное значение 7 и следующий необработанный элемент 4, суммируем и получаем новую агрегацию 11.
#
# Затем суммируем нашу агрегацию 11 со значением 3, получаем 14. И в конце добавляем последний элемент и готово
# итоговое значение 19. В итоге в процессе применения функции func мы нашли следующие значения [7, 11, 14, 19].
# Данный список и нужно будет вернуть в качестве ответа.
#
# Sample Input 1:
#
# def get_add(x, y):
#     return x + y
#
#
# print(aggregation(get_add, [5, 2, 4, 3, 5]))
# Sample Output 1:
#
# [7, 11, 14, 19]
# Sample Input 2:
#
# def get_max(x, y):
#     return max(x, y)
#
# # агрегируем нахождение максимума
# print(aggregation(get_max, [1, 4, 5, 7, 6, 5, 8, 10]))
# Sample Output 2:
#
# [4, 5, 7, 7, 7, 8, 10]
# Sample Input 3:
#
# def get_min(x, y):
#     return min(x, y)
#
# # агрегируем нахождение минимума
# print(aggregation(get_min, [9, 6, 7, 8, 5, 1, 2, 4]))
# Sample Output 3:
#
# [6, 6, 6, 5, 1, 1, 1]
# Sample Input 4:
#
# def get_product(x, y):
#     return x * y
#
# print(aggregation(get_product, [2, 6, 5, 10, 5, 1, 2]))
# Sample Output 4:
#
# [12, 60, 600, 3000, 3000, 6000]
# Sample Input 5:
#
# def get_add(x, y):
#     return x + y
#
# print(aggregation(get_add, [11, 4, 5, 7, 8, 10]))
# Sample Output 5:
#
# [15, 20, 27, 35, 45]



def aggregation(func, data: list|tuple):
    result = []
    result.append(func(data[0], data[1]))
    for i in range(2,len(data)):
        result.append(func(result[-1], data[i]))
    return result

def get_add(x, y):
    return x + y

print(aggregation(get_add, [11, 4, 5, 7, 8, 10]))