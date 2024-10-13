# Функция count_calls
# В этом задании вам нужно сделать функцию-замыкание count_calls, которая подсчитывает сколько раз она была вызвана.
# Особенность этого замыкания заключается в том, что количество вызовов должно храниться в атрибуте total_calls.
#
# Sample Input 1:
#
# counter = count_calls()
# counter()
# counter()
# print(counter.total_calls)
# counter()
# print(counter.total_calls)
# Sample Output 1:
#
# 2
# 3
# Sample Input 2:
#
# counter1 = count_calls()
# counter2 = count_calls()
# counter1()
# print(counter1.total_calls, counter2.total_calls)
# counter1()
# counter2()
# print(counter1.total_calls, counter2.total_calls)
# counter2()
# counter2()
# print(counter1.total_calls, counter2.total_calls)
# Sample Output 2:
#
# 1 0
# 2 1
# 2 3

def count_calls():
    def cnt_calls():
        cnt_calls.total_calls += 1
    cnt_calls.total_calls=0
    return cnt_calls



counter1 = count_calls()
counter2 = count_calls()
counter1()
print(counter1.total_calls, counter2.total_calls)
counter1()
counter2()
print(counter1.total_calls, counter2.total_calls)
counter2()
counter2()
print(counter1.total_calls, counter2.total_calls)


