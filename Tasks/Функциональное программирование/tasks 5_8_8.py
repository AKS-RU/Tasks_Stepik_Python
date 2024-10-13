# Замыкание-аккумулятор
# Ваша задача создать функцию-замыкание create_accumulator, которая должна накапливать (суммировать) внутри себя
# все значения, которые ей будут переданы. При создании замыкания стартовая сумма должна быть равна нулю.
# Посмотрите пример ниже:
#
# summator_1 = create_accumulator()
# print(summator_1(1)) # печатает 1
# print(summator_1(5)) # печатает 6
# print(summator_1(2)) # печатает 8
#
# summator_2 = create_accumulator()
# print(summator_2(3)) # печатает 3
# print(summator_2(4)) # печатает 7
# При каждом вызове должна возвращаться накопленная сумма, которая хранится в замыкании.
#
# Обратите внимание, что объекты из примера summator_1 и summator_2 хранят и накапливают свои собственные суммы.
#
# Необходимо только определить функцию-замыкание create_accumulator, остальное мы сделаем за вас
#
# Sample Input 1:
#
# summator_1 = create_accumulator()
# print(summator_1(5))
# print(summator_1(7))
# print(summator_1(2))
#
# summator_2 = create_accumulator()
# print(summator_2(3))
# print(summator_2(6))
# Sample Output 1:
#
# 5
# 12
# 14
# 3
# 9
# Sample Input 2:
#
# closure = create_accumulator()
#
# print(closure(4))
# print(closure(400))
# print(closure(4.5))
# print(closure(0.5))
#
# closure_2 = create_accumulator()
#
# print(closure_2(0))
# print(closure_2(1))
# print(closure_2(3))
# print(closure_2(7))
# Sample Output 2:
#
# 4
# 404
# 408.5
# 409.0
# 0
# 1
# 4
# 11



def create_accumulator(result=0):
    def accumulator (x):
        nonlocal result
        result+=x
        return result
    return accumulator




closure = create_accumulator(300)

print(closure(4))
print(closure(400))
print(closure(4.5))
print(closure(0.5))

closure_2 = create_accumulator()

print(closure_2(0))
print(closure_2(1))
print(closure_2(3))
print(closure_2(7))