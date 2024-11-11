# В вашем распоряжении дескриптор StringValidation, который мы создали в процессе урока.
#
# Ваша задача доработать его таким образом, чтобы он мог:
#
# проверять не только минимальную, но и на максимальную возможную длину строки. Если символов больше, чем должно быть, необходимо вызвать исключение
# ValueError("Длина атрибута <attribute_name> должна быть не больше <max_length> символов")
# проверять на наличие недопустимых символов. Если хотя бы один такой символ встречается в строке, необходимо вызвать исключение
#
# ValueError("Имеются недопустимые символы в атрибуте <название атрибута>")
#
# проверять, что все символы имеют одинаковый регистр
# (все только заглавные или только все строчные).
# Если проверка не выполняется, необходимо вызвать исключение
#
# ValueError("Все буквы должны быть в одном регистре в атрибуте <название атрибута>")
#
#
# Перечисленные проверки являются необязательными. Их необходимо выполнять, только если будут
# переданы значения в соответствующие атрибуты:
#
# min_length принимает числовое значение, которое ставит условие на минимальную допустимую длину.
# По умолчанию None
#
# max_length принимает числовое значение, которое ставит условие на максимальную допустимую длину.
# По умолчанию None
#
# exclude_chars принимает строковое значение, символы которого недопустимы в новом значении.
# умолчанию None
#
# is_same_register принимает булево значение. По умолчанию False. Если будет передано
# значение True, необходимо выполнять проверку на регистр букв.


class StringValidation:
    def __init__(self, min_length=None, max_length=None, exclude_chars=None,
                 is_same_register=False):
        self.min_length = min_length
        self.max_length = max_length
        self.exclude_chars = exclude_chars
        self.is_same_register = is_same_register

    def __set_name__(self, owner_class, attribute_name):
        self.attribute_name = attribute_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'В атрибут {self.attribute_name} можно сохранять только строки')
        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError(f'Длина атрибута {self.attribute_name} должна '
                             f'быть не меньше {self.min_length} символов')
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f'Длина атрибута {self.attribute_name} должна '
                             f'быть не больше {self.max_length} символов')
        if self.exclude_chars is not None and any([i in self.exclude_chars for i in value]):
            raise ValueError(f'Имеются недопустимые символы в атрибуте {self.attribute_name}')
        if self.is_same_register and not (value.isupper() or value.islower()):
            raise ValueError(f'Все буквы должны быть в одном регистре в '
                             f'атрибуте {self.attribute_name}')
        instance.__dict__[self.attribute_name] = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            print(f'calling __get__ for {self.attribute_name}')
            return instance.__dict__.get(self.attribute_name, None)


class Person:
    name = StringValidation()
    last_name = StringValidation()


p = Person()
p.name = 'Michail'
p.last_name = 'Lermontov'
print(p.name, p.last_name)
