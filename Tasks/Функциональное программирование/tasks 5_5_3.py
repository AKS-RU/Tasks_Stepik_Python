# Напишите функцию get_info_about_object, которая принимает объект и выводит информацию обо всех его атрибутах и методах
# в следующем формате:
#
# сперва выводится список всех атрибутов и методов
# на следующей строке фраза «Всего у объекта {count} атрибутов и методов»
#
#
# Примечание: тестирование на платформе будет производиться на версии Python 3.10, поэтому не переживайте, если вы
# используете у себя на устройстве другую версию python и у вас не совпадает вывод.
#
# Sample Input 1:
#
# def print_goods(lst):
#     pass
#
# get_info_about_object(print_goods)
# Sample Output 1:
#
# ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__',
#  '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__',
#  '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__',
#  '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__',
#  '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
# Всего у объекта 36 атрибутов и методов
# Sample Input 2:
#
# def print_goods(lst):
#     pass
#
# print_goods.info = 'Функция для вывода информации о товарах'
# print_goods.is_working = False
# print_goods.status = 'Not ready'
#
# get_info_about_object(print_goods)
# Sample Output 2:
#
# ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__',
#  '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__',
#  '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__',
#  '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__',
#  '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'info', 'is_working', 'status']
# Всего у объекта 39 атрибутов и методов
# Sample Input 3:
#
# get_info_about_object(str)
# Sample Output 3:
#
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
#  '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
#  '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode',
#  'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
#  'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
#  'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix',
#  'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
#  'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# Всего у объекта 80 атрибутов и методов


def get_info_about_object(func):
    result = list(dir(func))
    if '__type_params__' in result:
        result.remove('__type_params__')
    if '__getstate__' in result:
        result.remove('__getstate__')
    print(result)
    print(f'Всего у объекта {len(result)} атрибутов и методов')

get_info_about_object(str)