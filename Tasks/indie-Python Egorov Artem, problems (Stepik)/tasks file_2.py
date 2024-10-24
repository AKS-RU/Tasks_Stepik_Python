# Напишите функцию create_file_with_numbers, которая принимает на вход одно целое положительное число - n.
#
# Функция должна создать файл с название "range_<number>.txt" и наполнить его целыми числами от 1 до n включительно,
# причем каждое число записывается  в отдельной строке
#
# Пример: функция create_file_with_numbers(5) должна создать файл range_5.txt с содержимым
#
# 1
# 2
# 3
# 4
# 5

def create_file_with_numbers(n: int):
    file = open(f'range_{n}.txt','w')
    for i in range(n):
        file.write(f'{str(i+1)}\n')
    file.close()

create_file_with_numbers(5)