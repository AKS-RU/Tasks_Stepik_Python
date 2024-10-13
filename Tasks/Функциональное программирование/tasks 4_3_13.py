# Перепишите функцию rotate так, чтобы она стала работать не со списками, а с кортежами. Для этого выполните следующие
# шаги:
#
#     1️⃣ переименовать параметр lst - в tpl. Теперь функция будет принимать не список, а кортеж целых или
# вещественных чисел
#
#     2️⃣ изменится тип возвращаемого значения. Вместо списка функция rotate теперь должна возвращать кортеж.
# Остальная логика программы не меняется
#
#     3️⃣ док строку изменить на «Функция выполняет циклический сдвиг кортежа на shift позиций вправо
# (shift>0) или влево (shift<0)»
#
# Sample Input 1:
#
# print(rotate.__doc__)
# print(rotate.__annotations__)
# print(rotate((1, 2, 3, 4, 5, 6, 7), 2))
# Sample Output 1:
#
# Функция выполняет циклический сдвиг кортежа на shift позиций вправо (shift>0) или влево (shift<0)
# {'tpl': tuple[int | float, ...], 'shift': <class 'int'>, 'return': tuple[int | float, ...]}
# (6, 7, 1, 2, 3, 4, 5)
# Sample Input 2:
#
# print(rotate.__doc__)
# print(rotate.__annotations__)
# print(rotate((1, 2, 3, 4, 5, 6, 7), -3))
# Sample Output 2:
#
# Функция выполняет циклический сдвиг кортежа на shift позиций вправо (shift>0) или влево (shift<0)
# {'tpl': tuple[int | float, ...], 'shift': <class 'int'>, 'return': tuple[int | float, ...]}
# (4, 5, 6, 7, 1, 2, 3)
# Sample Input 3:
#
# print(rotate((1, 2, 3, 4, 5, 6, 7), -10))
# Sample Output 3:
#
# (4, 5, 6, 7, 1, 2, 3)
# Sample Input 4:
#
# print(rotate((1, 2, 3, 4, 5, 6, 7), 21))
# Sample Output 4:
#
# (1, 2, 3, 4, 5, 6, 7)

def rotate(tpl: tuple[int | float, ...], shift: int = 1) -> tuple[int | float, ...]:
    'Функция выполняет циклический сдвиг кортежа на shift позиций вправо (shift>0) или влево (shift<0)'
    lng = len(tpl)  # содержит длину передаваемого кортежа
    sh = abs(shift) % lng  # содержит сдвиг приведенный к длине кортежа
    result = list(tpl)
    for _ in range(sh):
        ind, val = ((lng, result.pop(0)) if shift < 0 else (0, result.pop()))
        result.insert(ind, val)
    result=tuple(result)

    return result


print(rotate.__doc__)
print(rotate.__annotations__)
print(rotate((1, 2, 3, 4, 5, 6, 7), 2))