# В этой задаче вам необходимо воспользоваться уже готовой функцией factorial, которая принимает неотрицательное число,
# и возвращает значение факториала данного числа.
#
# Ваша задача создать функцию trailing_zeros, которая принимает неотрицательное число, находит его факториал и возвращает
# сколько нулей на конце этого факториала .
#
# trailing_zeros(6) =>  1, потому что 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720
# trailing_zeros(10) => 2, потому что 10! = 3 628 800
# trailing_zeros(20) => 4, потому что 20! = 2 432 902 008 176 640 000
#
# Нужно написать только определение функций trailing_zeros и factorial

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

def trailing_zeros(n):
    # a = str(factorial(n))
    # res = 0
    # for i in a[::-1]:
    #     if int(i) == 0:
    #         res+=1
    #     else:
    #         break
    # return res

    return len(a:= str(factorial(n))) - len(a.rstrip('0'))

print(trailing_zeros(20))

