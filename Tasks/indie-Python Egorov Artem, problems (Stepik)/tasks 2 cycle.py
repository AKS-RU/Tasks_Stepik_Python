# Ваша задача найти сумму всех четырехзначных натуральных чисел, сумма цифр которых равна 20.
#
# Примерами таких чисел являются 9065, 8129, 7355 и тд. У каждого из указанных чисел сумма цифр равна 20


res = [] # создаем список для внесения туда чисел сумма цифр которых равна 20
res_sum = 0
for i in range(1000,10000):
    s = 0 # Обнуляем суммирование цифр перед запуском while
    c = i # Сохраняем i в промежуточную переменную
    while i > 0:
        a = i % 10
        s += a
        i = i // 10
    if s == 20:
        res.append(c)
        res_sum += c
print(sum(res), res_sum)
print(res)
