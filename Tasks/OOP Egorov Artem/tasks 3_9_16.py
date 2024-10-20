#                              Настройки приложения
# Очень часто настройки приложения выносят в отдельный файл и при старте приложения подгружают из него значения.
#
# Вам необходимо разработать простой конфигурационный менеджер для вашего приложения. Для этого необходимо реализовать
#                              класс AppConfig, который предоставляет методы для загрузки конфигурации из JSON-файла и
#                              получения значений конкретных параметров.
#
# В классе AppConfig должно быть реализовано следующее:
#
# метод load_config, который загружает конфигурацию из указанного JSON-файла
#
# метод get_config, который принимает ключ и возвращает соответствующее значение из загруженной конфигурации. Если ключ
# не найден, метод должен возвращать None. Также необходимо предоставить возможность
# обращаться к вложенным параметрам через точку.
#
# Вам будет предоставлен файл 'app_config.json', который имеет следующее содержимое
#
# {
#   "database": {
#     "host": "127.0.0.1",
#     "port": 5432,
#     "database_name": "postgres_db",
#     "user": "owner",
#     "password": "ya_vorona_ya_vorona"
#   },
#   "api_key": "hUFHu834837248jhoiHF89",
#   "log_level": "debug",
#   "max_connections": 10
# }
# Необходимо реализовать возможность вызова перечисленных методов как через класс, так и через экземпляр.
# Также необходимо обеспечить распространение значений параметров на все экземпляры класса AppConfig. Это значит,
# что все экземпляры AppConfig должны иметь одинаковые значения конфигурации приложения.
#
# Выбор реализации данной задачи остается за вами.

import json


class AppConfig:

    @classmethod
    def load_config(cls, name_file):
        with open(name_file, 'r') as file:
            cls.config = json.load(file)

    @staticmethod
    def find_key(dct, keys):
        if len(keys) == 1:
            return dct.get(keys[0])
        else:
            if keys[0] in dct:
                return dct[keys[0]].get(keys[-1])

    @classmethod
    def get_config(cls, key):
        lst = key.split('.')
        return cls.find_key(cls.config, lst)


AppConfig.load_config('app_config.json')

assert AppConfig.get_config('database') == {
    'host': '127.0.0.1', 'port': 5432,
    'database_name': 'postgres_db',
    'user': 'owner',
    'password': 'ya_vorona_ya_vorona'}
assert AppConfig.get_config('database.user') == 'owner'
assert AppConfig.get_config('database.password') == 'ya_vorona_ya_vorona'
assert AppConfig.get_config('database.pass') is None
assert AppConfig.get_config('password.database') is None

config = AppConfig()
assert config.get_config('max_connections') == 10
assert config.get_config('min_connections') is None

conf = AppConfig()
assert conf.get_config('max_connections') == 10
assert conf.get_config('database.user') == 'owner'
assert conf.get_config('database.host') == '127.0.0.1'
assert conf.get_config('host') is None

print('Good')
