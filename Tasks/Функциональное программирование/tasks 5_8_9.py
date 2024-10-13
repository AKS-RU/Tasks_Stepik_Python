# Обратный отсчет
# Напишите функцию-замыкание countdown, которая будет вести обратный отсчёт от переданного числа N до нуля.
# После того как замыкание будет вызвано более N раз, необходимо выводить сообщение
# «Превышен лимит, вы вызвали более N раз»
#
# Sample Input 1:
#
# count = countdown(3)
# count()
# count()
# count()
# count()
# count()
# Sample Output 1:
#
# 3
# 2
# 1
# Превышен лимит, вы вызвали более 3 раз
# Превышен лимит, вы вызвали более 3 раз
# Sample Input 2:
#
# a = countdown(2)
# b = countdown(2)
# a()
# b()
# b()
# b()
# a()
# a()
# Sample Output 2:
#
# 2
# 2
# 1
# Превышен лимит, вы вызвали более 2 раз
# 1
# Превышен лимит, вы вызвали более 2 раз


def countdown(n):
    cnt = n

    def cnt_down():
        nonlocal cnt
        if cnt:
            print(cnt)
            cnt -= 1
        else:
            print(f'Превышен лимит, вы вызвали более {n} раз')

    return cnt_down


a = countdown(2)
b = countdown(2)
a()
b()
b()
b()
a()
a()
