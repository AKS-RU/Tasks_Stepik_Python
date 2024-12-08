# Перед вами имеется функция basic, принимающая 4 аргумента

# def basic(a, b, c, d):
#     return 1000 * a + 100 * b + 10 * c + d
# Допишите функцию curry так, чтобы она выполняла каррирование функции basic


def basic(a, b, c, d):
    return 1000 * a + 100 * b + 10 * c + d


def curry(a):
    def inner_1(b):
        def inner_2(c):
            def inner_3(d):
                return 1000 * a + 100 * b + 10 * c + d
            return inner_3
        return inner_2
    return inner_1


print(curry(2)(3)(4)(5))
assert curry(2)(3)(4)(5) == 2345
assert curry(6)(1)(0)(5) == 6105
