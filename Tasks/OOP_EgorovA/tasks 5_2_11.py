# Создайте класс NewInt, который унаследован от целого типа int, то есть мы будем наследовать поведение целых чисел и
# значит экземпляры нашего класса будут поддерживать те же операции, что и целые числа.
#
# Дополнительно в классе NewInt нужно создать:
#
# метод repeat, который принимает одно целое положительное число n (по умолчанию равное 2), обозначающее сколько раз
# нужно продублировать данное число. Метод repeat должен возвращать новое число, продублированное n раз (см пример ниже);
#
# метод to_bin, который возвращает двоичное представление числа в качестве целого числа
# (может пригодиться функция bin или форматирование)


class NewInt(int):

    def repeat(self, factor=2):
        return int(str(self) * factor)

    def to_bin(self):
        return int(bin(self)[2:])


c1 = NewInt(9)
assert isinstance(c1, NewInt)
assert issubclass(NewInt, int)
assert c1 + 9 == 18
assert c1 * 9 == 81

c2 = NewInt(31)
assert c2.repeat() == 3131
assert c2.repeat(4) == 31313131
print(NewInt(16).to_bin())
assert NewInt(16).to_bin() == 10000
assert NewInt(14).to_bin() == 1110

print('Good')
