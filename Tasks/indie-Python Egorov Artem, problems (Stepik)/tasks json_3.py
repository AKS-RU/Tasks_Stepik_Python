# В json-файле содержится информация о нескольких группах людей, при этом у каждой группы есть свой идентификатор.
#
# Ваша задача скачать файлик и самостоятельно найти идентификатор группы, в которой находится самое большое количество
# женщин, рожденных после 1977 года. В качестве ответа необходимо указать через пробел идентификатор найденной группы и
# сколько в ней было женщин, рожденных после 1977 года.

import json

with open('group_people.json') as file:
    my_file = json.load(file)
id_group = 0
cnt = 0
for i in my_file:
    cnt_tmp=0
    for j in i['people']:
        if j['gender'] == 'Female' and j['year'] > 1977:
            cnt_tmp+=1
            # print(i['id_group'],j)
    if cnt_tmp>cnt:
        cnt = cnt_tmp
        id_group = i['id_group']
print(id_group, cnt)





# print(my_file)
