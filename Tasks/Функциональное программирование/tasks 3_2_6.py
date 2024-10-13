# Напишите функцию is_member, которая принимает некое значение value и список значений lst. Функция is_member должна
# True, если значение value присутствует в списке lst, и False в противном случае.
#
# Гарантируется, что список lst не будет вложенным
#
# Sample Input:
#
# print(is_member("e", ['a', 'e', 'i', 'o', 'u']))
# Sample Output:
#
# True

def is_member(st: str, lst: list):
    return st in lst

print(is_member("e", ['a', 'e', 'i', 'o', 'u']))