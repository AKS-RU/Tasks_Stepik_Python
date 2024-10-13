# Функция range - 3
# Теперь ваша задача создать полную копию встроенного объекта range. Он может быть вызван от одного,
# двух или трех аргументов.
#
# Если вызов происходит от одного аргумента n, то my_range_gen  генерирует все числа от 0 до n не включительно.
#
# Если вызов происходит от двух аргументов a и b, то my_range_gen  генерирует все числа от a включительно до b
# не включительно.
#
# Если вызов происходит от трех аргументов a , b и step, то my_range_gen  генерирует все числа от a включительно
# до b не включительно c шагом step( может быть отрицательное значение)
# for i in my_range_gen(4, 8, 2):
#     print(i)
#
# # Будет напечатано
# # 4
# # 6
#
# for i in my_range_gen(8, 5, -1):
#     print(i)
#
# # Будет напечатано
# # 8
# # 7
# # 6
#
#
# Предусмотрите вариант запуска my_range_gen со значением step=0. При таком варианте вызова, функция не должна
# генерировать ни одной последовательности и закончить свою работу.
#
# for i in my_range_gen(4, 8, 0):
#     print(i) # Ничего не печатает
# Такое же поведение должно быть, если переданы нелогичные значения start, stop и step (см. примеры)
#
# for i in my_range_gen(20, 10, 3):
#     print(i)
# # Ничего не печатает, потому что нельзя пройти от 20 до 10 с шагом 3
#
#
# for i in my_range_gen(1, 10, -2):
#     print(i)
# # Ничего не печатает, потому что нельзя пройти от 1 до 10 с шагом -2
# Ваша задача написать только определение функции my_range_gen
#
# И да, функцией range пользоваться нельзя; можете, конечно, попробовать, но у вас ничего не получится
#
# Sample Input 1:
#
# for i in my_range_gen(5):
#     print(i)
# Sample Output 1:
#
# 0
# 1
# 2
# 3
# 4
# Sample Input 2:
#
# for i in my_range_gen(10, 20):
#     print(i)
# Sample Output 2:
#
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# Sample Input 3:
#
# for i in my_range_gen(10, 30, 3):
#     print(i)
# Sample Output 3:
#
# 10
# 13
# 16
# 19
# 22
# 25
# 28
# Sample Input 4:
#
# for i in my_range_gen(30, 1, -5):
#     print(i)
# Sample Output 4:
#
# 30
# 25
# 20
# 15
# 10
# 5
# Sample Input 5:
#
# for i in my_range_gen(4, 8, 0):
#     print(i)
# print('End')
# Sample Output 5:
#
# End
# Sample Input 6:
#
# for i in my_range_gen(20, 10, 3):
#     print(i)
# print('End')
# Sample Output 6:
#
# End


def my_range_gen(a: int, b: int = 0, step: int = 1):
    if b == 0 and step>0:
        start, end = b, a
    else:
        start, end = a, b
    if step < 0:
        while start > end:
            yield start
            start += step
    elif step > 0:
        while start < end:
            yield start
            start += step


for num in my_range_gen(10, 0, -1):
    print(num)
