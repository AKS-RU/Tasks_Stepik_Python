# Перед вами частично реализованная функция double_odd_numbers, которая принимает список чисел и возвращает в качестве
# результата новый список, составленный из нечетных чисел, увеличенных в два раза.
#
# Внутри себя double_odd_numbers использует две функции:
#
# double, увеличивающая число в два раза;
#
# is_odd, проверяющая на нечетность
# Ваша задача реализовать эти функции внутри  double_odd_numbers
#
# Sample Input 1:
#
# print(double_odd_numbers([1, 2, 3, 4, 5]))
# Sample Output 1:
#
# [2, 6, 10]
# Sample Input 2:
#
# print(double_odd_numbers([6, 8, 10, 2]))
# Sample Output 2:
#
# []
# Sample Input 3:
#
# print(double_odd_numbers([-43, 91, 932, 9201, 32, 93]))
# Sample Output 3:
#
# [-86, 182, 18402, 186]


def double_odd_numbers(numbers):
    def double(n):
        return n*2


    def is_odd(n):
        if n%2:
            return n
        return None

    return [double(num) for num in numbers if is_odd(num)]

print(double_odd_numbers([-43, 91, 932, 9201, 32, 93]))