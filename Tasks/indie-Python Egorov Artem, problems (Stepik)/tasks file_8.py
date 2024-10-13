# В этой задаче вам необходимо обработать файл с названием words.txt, содержащий множество неуникальных слов.
# Само содержимое файла можно посмотреть здесь. Ваша задача найти в нем все слова, заканчивающиеся на строку ЕЯ, и
# вывести их на экран. При этом нужно:
#
# исключить дубли
# привести все буквы к верхнему регистру
# расположить слова в выводе в порядке двойной сортировки: сперва отсортировать по возрастанию длины слова, а при
# одинаковых значениях длины расположить по алфавиту
# Значит, если бы перед вам был файл с содержимым:
#
# панацея
# газосварщик
# ФЕЯ
# затея
# лапочка
# Гея
# панацея
# богая
# ливрея
# ШЕЯ
# я
# Камыш
# то ответ должен быть таким:
#
# ГЕЯ
# ФЕЯ
# ШЕЯ
# ЗАТЕЯ
# ЛИВРЕЯ
# ПАНАЦЕЯ

with open('words.txt', encoding='UTF-8') as file:
    lst_file = set(file.read().upper().split())
lst = [i for i in lst_file if str(i).endswith('ЕЯ')]
lst.sort()
lst.sort(key=len)
result='\n'.join(lst)

print(result)
# for i in lst_file:
#     if str(i).endswith('ЕЯ'):
#         res_file.add(i)
# res_file = list(res_file)
# cnt = len(min(res_file, key=len))
# result = ''
# lst_tmp = []
# while cnt <= len(max(res_file, key=len))+1:
#     result += ''.join(sorted(lst_tmp))
#     lst_tmp = []
#     for i in res_file:
#         if len(i) == cnt:
#             lst_tmp += [i + '\n']
#     cnt += 1
#
# # print(result)
# res_file.sort(key=len)
# print(res_file)
# res_file.sort()
# print(res_file)
# res_file.sort(key=len)
# print(res_file)
