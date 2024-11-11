# Создайте дескриптор MaxLengthAttribute, который возвращает имя самого длинного атрибута в
# экземпляре.
#
# Если несколько атрибутов имеют одинаковую длину, необходимо вернуть значение, стоящее
# последним по лексикографическому порядку без учета регистра букв.
#
# Если у экземпляра отсутствуют свои собственные атрибуты, необходимо вернуть None.
#
# Ваша задача написать только определение класса MaxLengthAttribute


class MaxLengthAttribute:

    def __get__(self, instance, owner):
        if instance.__dict__:
            return sorted(obj.__dict__, key=lambda x: (len(x), x.lower()))[-1]
        return


class MyClass:
    max_length_attribute = MaxLengthAttribute()


obj = MyClass()
print(obj.max_length_attribute)
print(sorted(obj.__dict__, key=lambda x: (len(x), x.lower())))
