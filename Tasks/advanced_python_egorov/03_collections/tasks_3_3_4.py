# Создайте класс StringWithSort, унаследованный отUserString и предоставляющий дополнительно
# метод sort
#
# sort(self, *, key=None, reverse=False)
# Данный метод должен возвращать новую отсортированную строку согласно ключу сортировки key.
# Также метод sort может принимать два необязательных аргумента:
#
# key - ключ сортировки, по умолчанию None. Обозначает способ сортировки. Если передано None ,
# отсортированную в лексикографическом порядке
# reverse обозначает порядок сортировки. False значит сортировать по возрастанию, True - в
# порядке убывания. По умолчанию принимает значение False
# В целом аргументы key и reverse выполняют ровно такую же функцию, как в функции sorted и в
# методе у списков .sort()


from collections import UserString


class StringWithSort(UserString):

    def sort(self, key=None, reverse=False):
        return ''.join(sorted(self.data, key=key, reverse=reverse))


s = StringWithSort("Golden retriver")
assert s.sort() == ' Gdeeeilnorrrtv'
assert s.data == 'Golden retriver'

assert s.sort(reverse=True) == 'vtrrronlieeedG '

new_s = StringWithSort('HelloMyFriend')
# При обычной сортироки сперва идут заглавные буквы потом строчные
assert new_s.sort() == 'FHMdeeillnory'
# Сортировка с ключом lower, который во время сравнения все буквы делает строчными
assert new_s.sort(key=str.lower) == 'deeFHillMnory'

print('OK')
