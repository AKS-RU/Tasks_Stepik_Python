# Напишите функцию rotate , которая имеет следующие параметры
#
#     ✔️  lst - список чисел (целых или вещественных)
#
#     ✔️  shift - целое число, обозначающее сдвиг. По умолчанию равен 1
#
# Функция rotate должна выполнить циклический сдвиг элементов списка на shift позиций и вернуть в качестве ответа новый
# со смещенными значениями. Если значение shift положительно, сдвиг необходимо производить вправо,
# если отрицательно — влево.
#
# На картинке ниже показан результат циклического сдвига элементов списка на единицу влево (источник картинки)
#
#
#
# Дополнительные условия для задания:
#
#     1️⃣ Функция rotate  должна быть чистой
#
#     2️⃣ необходимо проаннотировать параметры функции rotate  и ее возврат без использования модуля typing.
# Для тестов важен порядок следования типов
#
#     3️⃣ добавьте док-строку с содержанием «Функция выполняет циклический сдвиг списка на shift позиций
# вправо(shift>0) или влево(shift<0)»
#
# Sample Input 1:
#
# nums = [1, 2, 3, 4]
# new_nums = rotate(nums)
# print(nums)
# print(new_nums)
# Sample Output 1:
#
# [1, 2, 3, 4]
# [4, 1, 2, 3]
# Sample Input 2:
#
# print(rotate.__doc__)
# print(rotate.__annotations__)
# print(rotate([1, 2, 3, 4, 5, 6], 2))
# Sample Output 2:
#
# Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)
# {'lst': list[int | float], 'shift': <class 'int'>, 'return': list[int | float]}
# [5, 6, 1, 2, 3, 4]
# Sample Input 3:
#
# print(rotate.__doc__)
# print(rotate.__annotations__)
# print(rotate([1, 2, 3, 4, 5, 6], -3))
# Sample Output 3:
#
# Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)
# {'lst': list[int | float], 'shift': <class 'int'>, 'return': list[int | float]}
# [4, 5, 6, 1, 2, 3]
# Sample Input 4:
#
# print(rotate([1, 2, 3, 4, 5, 6], -10))
# Sample Output 4:
#
# [5, 6, 1, 2, 3, 4]
# Sample Input 5:
#
# print(rotate([1, 2, 3, 4, 5, 6, 7], 21))
# Sample Output 5:
#
# [1, 2, 3, 4, 5, 6, 7]


def rotate(lst: list[int | float], shift: int = 1) -> list[int | float]:
    'Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)'
    lng = len(lst)  # содержит длину передаваемого списка
    sh = abs(shift) % lng  # содержит сдвиг приведенный к длине списка
    result = lst.copy()
    for _ in range(sh):
        ind, val = ((lng, result.pop(0)) if shift < 0 else (0, result.pop()))
        result.insert(ind, val)

    return result


nums = [1, 2, 3, 4]
new_nums = rotate(nums, -1)
print(nums)
print(new_nums)
