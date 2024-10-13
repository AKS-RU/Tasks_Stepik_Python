# Напишите функцию is_only_one_positive, которая принимает произвольное количество числовых аргументов и возвращает True,
# когда из всех переданных значений только одно положительное, в противном случае верните False
#
# Вам необходимо написать только определение функции is_only_one_positive
#
# Sample Input 1:
#
# print(is_only_one_positive())
# Sample Output 1:
#
# False
# Sample Input 2:
#
# print(is_only_one_positive(1))
# Sample Output 2:
#
# True
# Sample Input 3:
#
# print(is_only_one_positive(-1, 2))
# Sample Output 3:
#
# True
# Sample Input 4:
#
# print(is_only_one_positive(-1, -2, -3, -4))
# Sample Output 4:
#
# False
# Sample Input 5:
#
# print(is_only_one_positive(-1, -2, -3, 4,-5))
# Sample Output 5:
#
# True


def is_only_one_positive(*args):
    if len(args) >= 1:
        if len(args) == 1:
            return args[0] > 0
        else:
            return sorted(args)[-1] > 0 and sorted(args)[-2] <= 0
    else:
        return 1 < 0


print(is_only_one_positive(-1, -2, -3, 4,-5))
