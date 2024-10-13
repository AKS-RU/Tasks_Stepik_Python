# Напишите функцию calculate_high_low_avg, которая принимает произвольное количество позиционных аргументов в виде
# целых чисел. Функция находит среднее арифметическое самого большого и самого маленького из аргументов и возвращает
# в качестве ответа.
#
# К тому же, если в calculate_high_low_avg передать необязательный именованный аргумент log_to_console со значением
# True, то дополнительно функция должна вывести на экран информацию в следующем формате:
#
# high={max}, low={min}, avg={average}
# где max - принимает значение самого большого аргумента, min - принимает значение самого маленького аргумента,
# average - принимает среднее арифметическое самого большого и самого маленького из аргументов.  Напомню, что return
# сразу же производит выход из функции.
#
# Sample Input 1:
#
# avg = calculate_high_low_avg(1, 2, 3, 4, 5)
# print(avg)
# Sample Output 1:
#
# 3.0
# Sample Input 2:
#
# avg = calculate_high_low_avg(1, 2, 3, 4, 5, log_to_console=True)
# print(avg)
# Sample Output 2:
#
# high=5, low=1, avg=3.0
# 3.0
# Sample Input 3:
#
# avg = calculate_high_low_avg(5, 4, 10, 5, 7, 8, log_to_console=True)
# print(avg)
# Sample Output 3:
#
# high=10, low=4, avg=7.0
# 7.0


def calculate_high_low_avg(*args, log_to_console=False):
    if log_to_console:
        print(f'high={max(args)}, low={min(args)}, avg={(max(args)+min(args))/2}')
    return (max(args)+min(args))/2


avg = calculate_high_low_avg(5, 4, 10, 5, 7, 8, log_to_console=True)
print(avg)