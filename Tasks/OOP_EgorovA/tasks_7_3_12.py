# Создайте  класс SequenceIterable, который принимает контейнер данных в виде списка в момент
# инициализации и сохраняет его в атрибуте ЭК.
#
# SequenceIterable([1, 5, 4, 6, 43, True, 'hello'])
# Вы должны научить класс SequenceIterable создавать итерируемый объект


class SequenceIterable:

    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return iter(self.iterable)


container = SequenceIterable([1, 5, 4, 6, 43, True, 'hello'])
for i in container:
    print(i)
