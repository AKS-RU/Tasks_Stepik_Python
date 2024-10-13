# Ваша задача написать функцию format_name_list, которая принимает список словарей, у каждого словаря в этом
# списке есть только ключ name.
#
# Функция format_name_list должна вернуть строку, в которой все имена из списка разделяются запятой кроме
# последних двух имен, они должны быть разделены союзом "и". Если в списке нет ни одного имени, функция должна
# вернуть пустую строку. Ниже представлены примеры:
#
# format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) => 'Bart, Lisa и Maggie'
#
# format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) => 'Bart и Lisa'
#
# format_name_list([{'name': 'Bart'}]) => 'Bart'
#
# format_name_list([]) => ''
# Ваша задача написать только определение функции format_name_list
#
# Про инструкцию assert можно прочитать здесь
#
# Sample Input:
#
# Sample Output:
#
# Проверки пройдены

def format_name_list(name: list):
    res = ''
    if len(name) >= 2:
        for i in range(len(name) - 2):
            res += str(*name[i].values()) + ', '
        res += str(*name[-2].values()) + ' и ' + str(*name[-1].values())
    else:
        if len(name) == 1:
            res += str(*name[-1].values())
    return res


print(format_name_list([]))
