# К вам в руки попал файлик формата json , в котором содержится информация одного автосалона о продажах менеджеров.
# В файле указано для каждого менеджера список проданных им автомобилей, а также проставлена цена продажи каждого
# автомобиля.
#
# Ваша задача скачать файлик и самостоятельно найти самого успешного менеджера по итоговой сумме продаж. В качестве
# ответа нужно через пробел указать сперва его имя, затем фамилию и после общую сумму его продаж.


import json

with open('manager_sales.json') as file:
    my_data = (json.load(file))
first_name = ''
last_name = ''
sum_sale = 0
for i in my_data:
    # print(111111111111111)
    sum_sale_tmp = 0
    for j in i['cars']:
        sum_sale_tmp += j['price']
        # print(i['manager']['first_name'], i['manager']['last_name'], j['price'])
    if sum_sale_tmp > sum_sale:
        sum_sale = sum_sale_tmp
        first_name = i['manager']['first_name']
        last_name = i['manager']['last_name']
print(first_name, last_name, sum_sale)

# print(my_data[0]['manager']['first_name'])
# print(my_data[0].get('manager'))

# print(my_data[0]['manager']['first_name'])
# print(type(my_data),my_data[0]['manager']['first_name'])
