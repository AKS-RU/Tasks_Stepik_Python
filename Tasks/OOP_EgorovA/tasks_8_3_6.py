# Студенты
# Ваша задача дописать класс Student так, чтобы в нем появились
#
# атрибут guid - уникальная случайно сгенерированная строка длиной 15 символов. Для этого
# воспользуйтесь заготовленной функций generate_guid. Атрибут не должен участвовать в
# инициализации и в методе __repr__
#
# поле email - строковое значение, которое назначает университет студенту. Формируется из имени и
# фамилии в нижнем регистре следующим образом
# {first_name}.{last_name}@uni.edu
# В инициализации не участвует
#
# поле tuition необязательный атрибут, обозначающий стоимость за обучение. По умолчанию студент
# учится бесплатно, значит его tuition равно нулю. Для платников значение передается при
# инициализации.   В __repr__ не участвует
# Также необходимо сортировать всех студентов сперва по стоимости обучения
# (кто учится бесплатно должны быть первыми), а затем по фамилии и имени.


import random
import string
from dataclasses import dataclass, field

alphabet = string.ascii_uppercase + string.digits


def generate_guid():
    guid = ''.join(random.choices(alphabet, k=15))
    return guid


@dataclass(order=True)
class Student:
    sort_index: str = field(init=False, repr=False, compare=True)
    first_name: str
    last_name: str
    email: str = field(init=False)
    tuition: float | int = field(default=0, repr=False)

    def __post_init__(self):
        self.guid = generate_guid()
        self.email = f'{self.first_name.lower()}.{self.last_name.lower()}@uni.edu'
        self.sort_index = (self.tuition, self.last_name, self.first_name)


jane = Student('Jane', 'Lee')
julia = Student('Julia', 'Doe')
jake = Student('Jake', 'Langdon')
joy = Student('Joy', 'Smith')
print(*sorted([jane, julia, jake, joy]), sep='\n')
