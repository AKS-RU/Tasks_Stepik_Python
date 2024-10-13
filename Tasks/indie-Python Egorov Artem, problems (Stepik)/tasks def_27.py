# Ваша задача создать функцию create_matrix, которая принимает
#
# необязательный числовой параметр size - размер квадратной матрицы, по умолчанию принимает значение 3;
# необязательный числовой параметр up_fill - значение заполнителя элементов, находящихся выше главной диагонали. По умолчанию равен 0;
# необязательный числовой параметр down_fill - значение заполнителя элементов, находящихся ниже главной диагонали.
# По умолчанию равен 0;
# Функция create_matrix должна возвращать квадратную матрицу размером size х size, на диагонали которой располагаются
# числа от 1 до size. Все остальные элементы заполнены согласно параметрам up_fill и down_fill.
#
# create_matrix() => [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
# create_matrix(4) => [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]
#
# create_matrix(up_fill=7) => [[1, 7, 7],
#                              [0, 2, 7],
#                              [0, 0, 3]]
#
# create_matrix(up_fill=7, down_fill=9) => [[1, 7, 7],
#                                           [9, 2, 7],
#                                           [9, 9, 3]]
#
#
# create_matrix(size=4, up_fill=7, down_fill=9) => [[1, 7, 7, 7],
#                                                   [9, 2, 7, 7],
#                                                   [9, 9, 3, 7],
#                                                   [9, 9, 9, 4]]
# Ваша задача дописать только тело функции create_matrix
import pprint
import math
def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0):
    #res = [[0]*size for i in range(size)]
    # for ln in range(size):
    #     for cl in range(size):
    #         if cl == ln:
    #             res[ln][cl]=ln+1
    #         elif ln<cl:
    #             res[ln][cl] = up_fill
    #         else:
    #             res[ln][cl] = down_fill
    # return res#print(*(i for i in res), sep='\n')
    return [[ln+1 if ln==cl else up_fill if ln<cl else down_fill for cl in range(size)] for ln in range(size)]

#print(create_matrix(size=4, up_fill=7, down_fill=9))

#pprint.pprint(locals())
print(math.factorial(10))
print(dir(math))