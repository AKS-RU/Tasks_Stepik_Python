#                                       Заполнение матрицы
# Ваша задача — создать функцию create_matrix, которая имеет следующие параметры:
#
# необязательный числовой параметр size - размер квадратной матрицы, по умолчанию принимает значение 3;
#
# необязательный числовой параметр up_fill - значение заполнителя элементов, находящихся выше главной диагонали.
# По умолчанию равен 0;
#
# необязательный числовой параметр down_fill - значение заполнителя элементов, находящихся ниже главной диагонали.
# По умолчанию равен 0.
# Функция create_matrix должна возвращать квадратную матрицу размером size х size, на диагонали которой
# располагаются числа от 1 до size. Все остальные элементы заполнены согласно параметрам up_fill и down_fill.
#
# Ваша задача написать только определение функции create_matrix
#
# Sample Input 1:
#
# print(create_matrix())
# Sample Output 1:
#
# [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
# Sample Input 2:
#
# print(create_matrix(1))
# Sample Output 2:
#
# [[1]]
# Sample Input 3:
#
# print(create_matrix(size=2))
# Sample Output 3:
#
# [[1, 0], [0, 2]]
# Sample Input 4:
#
# print(create_matrix(up_fill=7))
# Sample Output 4:
#
# [[1, 7, 7], [0, 2, 7], [0, 0, 3]]
# Sample Input 5:
#
# print(create_matrix(up_fill=7, down_fill=9))
# Sample Output 5:
#
#  [[1, 7, 7], [9, 2, 7], [9, 9, 3]]

# ----------------------------------------------------------------------------------------------------------


def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0) -> list:
    lst = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                lst[i][j] = i + 1
            elif up_fill and j > i:
                lst[i][j] = up_fill
            elif down_fill and j<i:
                lst[i][j] = down_fill

    return lst


if __name__ == '__main__':
    assert create_matrix() == [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
    assert create_matrix(1) == [[1]]
    assert create_matrix(size=2) == [[1, 0], [0, 2]]
    assert create_matrix(up_fill=7) == [[1, 7, 7], [0, 2, 7], [0, 0, 3]]
    assert create_matrix(up_fill=7, down_fill=9) == [[1, 7, 7], [9, 2, 7], [9, 9, 3]]
    print('Всё правильно!')
