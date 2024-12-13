# Снова поработаем с файлом currencies.json. Теперь ваша задача раскидать хранящиеся в нем данные
# по отдельным файлам

# Для этого в текущем рабочем каталоге вам необходимо создать папку currencies, внутри нее
# необходимо создать столько файлов формата txt, сколько валют находиться по ключу Valute

# Имя файла должно совпадать с символьным кодом самой валюты. На рисунке ниже мы видим часть данных,
# хранящихся в файле currencies.json


# Значит внутри currencies должны быть созданы файлы aud.txt, azn.txt, gbr.txt  и т.д.

# Внутри каждого файла необходимо записать только информацию, касающуюся данной валюты. Нужно
# избавиться от кавычек, запятых и скобок. Используйте значение отступа равное 2.

# К примеру, если взять файл aud.txt , то вот такое содержимое должно быть у него внутри

#  CharCode: AUD
#   ID: R01010
#   Name: Австралийский доллар
#   Nominal: 1
#   NumCode: 036
#   Previous: 59.2201
#   Value: 59.4582


from pprint import pprint, pformat, PrettyPrinter
import json
import os


with open('currencies.json', 'r') as fp:
    data = json.load(fp)

if not os.path.isdir('currencies'):
    os.mkdir('currencies')

os.chdir(r'currencies')
chars_to_remove = ['"', "'", ',', '{', '}']
my_print = PrettyPrinter(indent=2)

for i in data['Valute']:
    tmp = my_print.pformat(data['Valute'].get(i))
    for char in chars_to_remove:
        tmp = tmp.replace(char, '')
    with open(f'{i.lower()}.txt', 'w') as fp:
        fp.write(tmp)
