# В вашем распоряжении есть файл currencies.json, который находиться в текущем рабочем каталоге

# Если хотите увидеть содержимое JSON файла в удобочитаемом виде, можете воспользоваться
# сервисом jsonformatter

# В нем все данные сохранены в одной большой неформатированной строке, в которой трудно
# разобрать данные.

# Ваша задача создать файл в текущем рабочем каталоге с именем new_currencies.txt, в которой
# необходимо записать все содержимое currencies.json в красивом виде с помощью pprint.
# Используйте ширину 80 символов и уровень отступа в 2 пробела

# Также выведите содержимое файла new_currencies.txt на экран.

from pprint import pprint
import json


with open('currencies.json', 'r') as fp:
    data = json.load(fp)

with open('new_currencies.txt', 'w+') as fp:
    pprint(data, indent=2, width=80, stream=fp)
    res = fp.read()

print(res)
