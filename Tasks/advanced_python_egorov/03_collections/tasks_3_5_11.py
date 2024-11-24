# Напишите функцию find_three_most_common,  которая принимает на вход список и находит три
# наиболее распространенных в нем элемента. Функция find_three_most_commonдолжна вернуть список,
# состоящих из трех самых популярных значений, причем на первом месте должно стоять третье по
# популярности значение, затем - втрое по популярности, и на третьем месте - самое популярное
# значение.

# Если элементов для списка из трех самых популярных не будет хватать, необходимо дополнять
# его значениями None


from collections import Counter


def find_three_most_common(lst: list) -> list:

    result = []

    lst_most = Counter(lst).most_common(3)

    while len(lst_most) < 3:
        lst_most.append(None)

    for i in lst_most:
        if i is not None:
            result.insert(0, i[0])
        else:
            result.insert(0, i)

    return result


# print(find_three_most_common([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
assert find_three_most_common([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [2, 3, 4]
# print(find_three_most_common([1, 1, 1, 1, 1]))
assert find_three_most_common([1, 1, 1, 1, 1]) == [None, None, 1]
# print(find_three_most_common([1, 1, 1, 2, 2]))
assert find_three_most_common([1, 1, 1, 2, 2]) == [None, 2, 1]
assert find_three_most_common([1, 1, 2, 2, 2]) == [None, 1, 2]
assert find_three_most_common([]) == [None, None, None]

print('OK')
