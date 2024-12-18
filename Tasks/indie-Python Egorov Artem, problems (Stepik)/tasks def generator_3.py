# Ваша задача создать функцию-генератор my_range_gen, которая копирует работу range.
#
# my_range_gen можно запускать, передав ей один параметр stop
# my_range_gen(stop)
# и она должна генерировать последовательность от 0 до stop не включительно
# for i in my_range_gen(5):
#     print(i)
#
# # Будет напечатано
# # 0
# # 1
# # 2
# # 3
# # 4
#  my_range_gen можно запускать, передав ей два параметра start и stop
#
# my_range_gen(start, stop)
# и она должна генерировать последовательность от start включительно до stop не включительно
#
# for i in my_range_gen(4, 8):
#     print(i)
#
# # Будет напечатано
# # 4
# # 5
# # 6
# # 7
#  my_range_gen можно запускать, передав ей три параметра start, stop и step
#
# my_range_gen(start, stop, step)
# и она должна генерировать последовательность от start включительно до stop не включительно c шагом step
#
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
# предусмотрите вариант запуска my_range_gen со значением step=0. При таком варианте вызова, функция не должна
# генерировать ни одной последовательности и закончить свою работу. Такое же поведение должно быть если переданы
# нелогичные значения start, stop и step(см. примеры)
# for i in my_range_gen(4, 8, 0):
#     print(i)
# # Ничего не печатает
#
# for i in my_range_gen(20, 10, 3):
#     print(i)
# # Ничего не печатает, потому что нельзя пройти от 20 до 10 с шагом 3
#
#
# for i in my_range_gen(1, 10, -2):
#     print(i)
# # Ничего не печатает, потому что нельзя пройти от 1 до 10 с шагом -2
#
# Ваша задача написать только определение функции my_range_gen
#
# И да, функцией range пользоваться нельзя, можете конечно попробовать, но у вас ничего не получится

def my_range_gen(a=0, b=0, step=1):
    # return a, b, step
    if a > b and b == 0:
        start = b
        stop = a
    elif a < b or a > b and b != 0:
        start = a
        stop = b
    elif a > b and b != 0:
        start = a
        stop = b
    if start < stop and step > 0:
        while start < stop:
            yield start
            start += step
    elif start > stop and step < 0:
        while start > stop:
            yield start
            start += step


for i in my_range_gen(3,1, -1 ):
    print(i)
