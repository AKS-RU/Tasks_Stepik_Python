# Замыкание для умножения
# Ваша задача создать функцию multiply, которая принимает один аргумент. Функция должна запомнить это значение и вернуть
# результат умножения этого числа с переданным вновь значением (см. примеры)
#
# f_2 = multiply(2)
# print("Умножение 2 на 5 =", f_2(5)) #10
# print("Умножение 2 на 15 =", f_2(15)) #30
# f_3 = multiply(3)
# print("Умножение 3 на 5 =", f_3(5)) #15
# print("Умножение 3 на 15 =", f_3(15)) #45
# Sample Input 1:
#
# f_2 = multiply(2)
# print("Умножение 2 на 5 =", f_2(5))
# print("Умножение 2 на 15 =", f_2(15))
#
# f_3 = multiply(3)
# print("Умножение 3 на 5 =", f_3(5))
# print("Умножение 3 на 15 =", f_3(15))
# Sample Output 1:
#
# Умножение 2 на 5 = 10
# Умножение 2 на 15 = 30
# Умножение 3 на 5 = 15
# Умножение 3 на 15 = 45
# Sample Input 2:
#
# print(multiply(4)(3))
# print(multiply(400)(5))
# print(multiply(4.5)(2))
# Sample Output 2:
#
# 12
# 2000
# 9.0
# Sample Input 3:
#
# half = multiply(0.5)
# print(half(10))
# print(half(100))
# print(half(1000))
#
# double = multiply(2)
# print(double(10))
# print(double(100))
# print(double(1000))
# Sample Output 3:
#
# 5.0
# 50.0
# 500.0
# 20
# 200
# 2000



def multiply(x):
    def multiply_2(y):
        return x*y
    return multiply_2


print(multiply(4)(3))
print(multiply(400)(5))
print(multiply(4.5)(2))