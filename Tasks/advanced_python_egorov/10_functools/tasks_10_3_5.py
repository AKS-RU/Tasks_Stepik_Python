# Ваша задача создать общую функцию  convert, которая выполняет преобразование различных типов.
# Она должна уметь обрабатывать следующие  str, int, float, Path, date и datetime. Эти функции
# должны выполнять соответствующие преобразования для каждого типа данных:

# типы str, int, float должны остаться такими же

# тип Path должен конвертироваться в строку

# типы date и datetime должны конвертироваться в строку определенного формата. Формат зависит от
# атрибута is_need_time: если он принимает значение True, в формате нужно выводить время
# "dd.mm.yyyy hh:mm:ss". Если в is_need_time передали ложь, формат должен иметь вид "dd.mm.yyyy".
# По умолчанию is_need_time принимает значение True. Для типа date проставлять часы,
# минуты и секунды нулевыми значениями

# Для остальных типов функция convert должна вызывать исключение
# TypeError(f"Cannot convert {value}")

from functools import singledispatch
from datetime import date, datetime
from pathlib import Path
from os import path


@singledispatch
def convert(*args):
    raise TypeError(f'Cannot convert {args}')


@convert.register(str)
def _(value):
    return value


@convert.register(int)
def _(value):
    return value


@convert.register(float)
def _(value):
    return value


@convert.register(Path)
def _(value):
    return str(value)


@convert.register(datetime)
def _(value, is_need_time=True):
    if is_need_time:
        return value.strftime('%d.%m.%Y %H:%M:%S')
    return value.strftime('%d.%m.%Y')


@convert.register(date)
def _(value, is_need_time=True):
    if is_need_time:
        return datetime.combine(value, datetime.min.time()).strftime('%d.%m.%Y %H:%M:%S')
    return value.strftime('%d.%m.%Y')


assert convert("Hello, World") == "Hello, World"
assert convert(42) == 42
assert convert(3.14) == 3.14

assert convert(Path("tmp/hello.txt")) == path.join('tmp', 'hello.txt')
assert convert(Path("some/path/to/file.txt")
               ) == path.join('some', 'path', 'to', 'file.txt')

assert convert(datetime(2023, 10, 29, 5, 6)) == '29.10.2023 05:06:00'
assert convert(datetime(2021, 8, 12, 12, 8, 58),
               is_need_time=True) == '12.08.2021 12:08:58'
assert convert(datetime(1999, 9, 29, 5, 6), is_need_time=False) == '29.09.1999'

assert convert(date(2023, 10, 29), is_need_time=True) == '29.10.2023 00:00:00'
assert convert(date(2009, 12, 31)) == '31.12.2009 00:00:00'
assert convert(date(2023, 7, 11), is_need_time=False) == '11.07.2023'

try:
    print(convert([1, 2, 3]))
except TypeError:
    pass

try:
    print(convert({1: 2, 3: 4}))
except TypeError:
    pass

print('Good')
