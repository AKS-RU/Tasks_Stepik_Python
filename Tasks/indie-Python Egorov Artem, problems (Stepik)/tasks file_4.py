# В этой задаче вам необходимо скачать файл, в котором записаны натуральные числа. Ваша задача найти
#
# количество трехзначных чисел;
# сумму двухзначных чисел
# В качестве ответа укажите найденные два числа через запятую без других знаков и пробелов. Сперва количество,
# потом сумма

file = open('numbers.txt')
file_lst = file.read().split()
file.close()
res_count = 0
res_summ = 0
for i in file_lst:
    if len(i) == 3:
        res_count += 1
    elif len(i) ==2:
        res_summ+=int(i)
print(f'{res_count},{res_summ}')


