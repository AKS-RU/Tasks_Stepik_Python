# Нахождение среднего арифметического
# Ваша задача — создать корутину get_average, которая накапливает среднее арифметическое переданных в нее чисел.
#
# Числа поступают в корутину при помощи метода send, корутина должна порождать текущее накопленное значение среднего арифметического.
#
# Вам необходимо написать только определение функции-корутины get_average.
#
# Sample Input:
#
# coro = get_average()
# next(coro)
# print(coro.send(10))
# print(coro.send(20))
# print(coro.send(6))
# Sample Output:
#
# 10.0
# 15.0
# 12.0


def get_average():
    cnt, sum_average = 0, 0
    numbers = yield
    while True:
        sum_average += numbers
        cnt += 1
        numbers = yield sum_average / cnt




coro = get_average()
next(coro)
print(coro.send(10))
print(coro.send(20))
print(coro.send(6))
# coro.send(10)
# coro.send(20)
# coro.send(6)