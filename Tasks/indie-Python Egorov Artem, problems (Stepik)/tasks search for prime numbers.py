# Ваша задача состоит в том, чтобы решить несколько более общую задачу – а именно по числу n найти количество простых чисел p из интервала n < p < 2n.
#
# Напомним, что число называется простым, если оно делится только само на себя и на единицу.
#
# Входные данные
# Программа принимает на вход целое число n (2 ≤ n ≤ 50000).
#
# Выходные данные
# Вам необходимо вывести на экран одно число – количество простых чисел p на интервале  n < p < 2n.

n = int(input())
cnt = 0
for i in range(n + 1, 2 * n):
    res_lst = []
    x = 1
    while x * x <= i:
        if i % x == 0:
            res_lst.append(x)
            if x != i // x:
                res_lst.append(i // x)
        x += 1
    if len(res_lst) == 2:
        cnt += 1

print(cnt)
