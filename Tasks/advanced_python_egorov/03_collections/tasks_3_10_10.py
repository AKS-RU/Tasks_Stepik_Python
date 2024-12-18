# Выполняй команду
# Ваша задача — выполнить над деком определенный список команд и вывести, что останется от дека

# Входные данные
# На вход вашей программе поступает множество чисел, разделенных пробелом. Данные числа
# являются основой дека

# Далее на вход поступает натуральное число n - количество команд

# Затем в отдельных строках n раз вводятся команды, которые нужно выполнить над деком. Формат
# команды следующий:

# <Действие> <Сторона> [<Значение>]
# Действие - обозначает что именно нужно сделать, может принимать 3 значения:

# A (от слова add) — обозначает добавление элемента;

# D (от слова delete) — обозначает удаление элемента;

# R (от слова rotate) — обозначает смещение дека. Выполнять можно смещение только на единицу
# влево или вправо в зависимости от <Стороны>.
# Сторона - обозначает сторону дека, над которой нужно выполнить действие.
# Может принимать 2 значения:

# L (от слова left) - левая сторона;

# R (от слова right) - правая сторона.
# Значение - необязательный символ, поэтому записана в квадратных скобках. Используется только при
# операции добавления. Отвечает за добавляемое значение

# Пример команды:

# A L 100 - добавить слева значение 100
# D R - удалить элемент справа
# R L - сместить элементы влево
# Выходные данные
# Вывести полученный дек после применения всех команд

from collections import deque


action = {
    'AR': 'append',
    'AL': 'appendleft',
    'DR': 'pop',
    'DL': 'popleft',
    'RR': 'rotate',
    'RL': 'rotate'
}
lst_deq = deque(map(int, input().split()))

for i in range(int(input())):
    tmp_lst = input().split()
    if len(tmp_lst) == 3:
        getattr(lst_deq, action[''.join(tmp_lst[0:2])])(int(tmp_lst[2]))
    else:
        if ''.join(tmp_lst[0:]) == 'RL':
            getattr(lst_deq, action[''.join(tmp_lst[0:])])(-1)
        else:
            getattr(lst_deq, action[''.join(tmp_lst[0:])])()

print(lst_deq)
