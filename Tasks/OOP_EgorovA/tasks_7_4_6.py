# Сперва четные индексы, потом все остальные
# Усложним задачу про SequenceIterable
#
# Теперь нужно создать итератор SequenceIterator, который принимает контейнер данных в виде списка
# в момент инициализации и сохраняет его в атрибуте ЭК
#
# SequenceIterable([1, 5, 4, 6, 43, True, 'hello'])
# При итерации объект SequenceIterator должен  сперва выдать все элементы, находящиеся на четных
# индексах (0, 2, 4 и т.д), а затем элементы, имеющие нечетные индексы (1, 3, 5 и т.д.)


class SequenceIterator:

    def __init__(self, iterable):
        self.iterable = iterable[::2] + iterable[1::2]

    def __iter__(self):
        return iter(self.iterable)


container = SequenceIterator([43, 42, 5, 90])
for i in container:
    print(i)
