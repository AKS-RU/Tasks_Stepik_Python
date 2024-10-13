#               Декоратор-повторитель
# Напишите декоратор repeater, который трижды вызывает декорированную функцию
#
# Ваша задача написать только определение функции декоратора repeater
#
# Sample Input 1:
#
# @repeater
# def multiply(num1, num2):
#     print(num1 * num2)
#
# multiply(9, 4)
# Sample Output 1:
#
# 36
# 36
# 36
# Sample Input 2:
#
# @repeater
# def some_func(a, b, c):
#     print(a ** b + c)
#
# some_func(4, 5, 4)
# some_func(14, 51, 34)
# Sample Output 2:
#
# 1028
# 1028
# 1028
# 28348482735670119891662708120846966066539436858445098123298
# 28348482735670119891662708120846966066539436858445098123298
# 28348482735670119891662708120846966066539436858445098123298



def repeater(func):
    def rep(*args, **kwargs):
        func(*args,**kwargs)
        func(*args, **kwargs)
        func(*args, **kwargs)

    return rep


@repeater
def some_func(a, b, c):
    print(a ** b + c)


some_func(4, 5, 4)
some_func(14, 51, 34)