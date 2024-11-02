# Для этого в этой задаче необходимо

# создать класс User, который принимает имя пользователя и пароль при инициализации, и имеет 
# метод get_info(), который возвращает строку в виде 

# Имя пользователя: {self.username}
# Создайте класс Authentication, состоящий из одного метода authenticate(). Данный метод принимает 
# имя пользователя и пароль, и возвращает True, если пользователь аутентифицирован успешно, и False, 
# если аутентификация не удалась.

# Создайте класс AuthenticatedUser, который наследуется от классов Authentication и User. 
# Он не имеет своих методов и все поведение наследуют от родителей


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        
    def get_info(self):
        return f'Имя пользователя: {self.name}'
    
class Authentication(User):
    
    def authenticate(self, name, password):
        return name == self.name and password == self.password
    
class AuthenticatedUser(Authentication, User):
    pass



assert issubclass(AuthenticatedUser, User) is True
assert issubclass(AuthenticatedUser, Authentication) is True

user1 = AuthenticatedUser('user1', 'password1')
assert user1.get_info() == 'Имя пользователя: user1'
assert user1.authenticate('user1', 'password2') is False
assert user1.authenticate('user1', 'password1') is True

ted = AuthenticatedUser('ted_lawyer', 'alligator3')
print(ted.get_info())