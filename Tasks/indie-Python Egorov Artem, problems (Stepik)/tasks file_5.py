# Напишите функцию find_lines_len_more_6, которая принимает имя файла и находит количество строк,
# превышающее 6 символов. Не забывайте исключать знак переноса на новую строку, стоящий в конце строки.
#
# Функция find_lines_len_more_6 должна возвращать найденное количество строк
#
# Ваша задача написать только определение функции find_lines_len_more_6

def find_lines_len_more_6(file_name:str):
    with open(file_name) as file:
        result = 0
        for i in file:
            if len(i.rstrip())>6:
                result+=1
    return result





print(find_lines_len_more_6('test.txt'))