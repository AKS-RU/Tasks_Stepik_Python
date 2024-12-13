# Перед вами список словарей data, хранящий информацию о посетителях сайта

# Ваша задача красиво вывести всю информацию о пользователях, скрывая их оценки.

# Порядок следования ключей в выводе должен совпадать с порядком определения ключей в словарях

from pprint import pprint


data = [
    {
        "userId": 1,
        "firstName": "Krish",
        "lastName": "Lee",
        "emailAddress": "krish.lee@example.com",
        "marks": [3, 4, 5, 5, 4, 3, 5, 4]
    },
    {
        "userId": 2,
        "firstName": "racks",
        "lastName": "jacson",
        "emailAddress": "racks.jacson@example.com",
        "marks": [3, 3, 5, 2, 4, 2, 5, 4]
    },
    {
        "userId": 3,
        "firstName": "denial",
        "lastName": "roast",
        "emailAddress": "denial.roast@example.com",
        "marks": [5, 4, 5, 5, 4, 4, 3, 4]

    },
    {
        "userId": 4,
        "firstName": "Leanne Graham",
        "lastName": "Bret",
        "emailAddress": "Sincere@april.biz",
        "marks": [3, 4, 5, 5, 4, 3, 5, 4]
    },
    {
        "userId": 5,
        "firstName": "Ervin Howell",
        "lastName": "Antonette",
        "emailAddress": "Shanna@melissa.tv",
        "marks": [3, 4, 5, 5, 4, 3, 5, 4]
    }
]

pprint(data, depth=2, sort_dicts=False)
