# Проверка на вхождение через рекурсию
# Перепишите реализацию функции is_member через рекурсию. Напоминаю, функция is_member  должна проверять, есть ли
# значение value в линейном списке lst.
#
# Функция is_member должна вернуть True, если значение value присутствует в списке lst, и False в противном случае.
#
# Гарантируется, что список lst не будет вложенным
#
# Sample Input 1:
#
# print(is_member("e", ['a', 'e', 'i', 'o', 'u']))
# Sample Output 1:
#
# True
# Sample Input 2:
#
# print(is_member(10, [1, 23, 3, 43, 10, 35]))
# Sample Output 2:
#
# True
# Sample Input 3:
#
# print(is_member('might', ['or', 'maybe', 'this']))
# Sample Output 3:
#
# False


result=[]
def is_member(value: int|str|float, lst: list)->bool:
    if len(lst)==0:
        return False
    result.append(lst[0] is value)
    a = is_member(value, lst[1:])
    return any(result)


print(is_member("e", []))
