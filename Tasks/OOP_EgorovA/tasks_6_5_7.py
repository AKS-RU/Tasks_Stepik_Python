# Перед вами имеется часть готового кода. Ваша задача дописать функцию get_user: она должна
# принимать логин пользователя и возвращать имя пользователя из словаря users. Если логин
# отсутствует, необходимо возбуждать исключение UserNotFoundError с текстом User not found
#
# Также не забудьте реализовать класс-исключение UserNotFoundError


class UserNotFoundError(Exception):

    def __str__(self):
        return 'User not found'


users = {
    "alice": {"name": "Alice Smith", "email": "alice@example.com"},
    "bob": {"name": "Bob Johnson", "email": "bob@example.com"},
    "jack": {"name": "Jack Wild", "email": "jack_wild@example.com"}
}


def get_user(username):
    #  напишите реализацию функции
    if username in users:
        return users[username].get('name')
    raise UserNotFoundError


try:
    username = get_user(input())
except UserNotFoundError as e:
    print(e)
else:
    print(username)
