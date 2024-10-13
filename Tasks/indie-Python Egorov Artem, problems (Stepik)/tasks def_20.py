# Ваша задача написать функцию get_domain_name, которая принимает строку url, извлекает из нее доменное имя
# и возвращает его в качестве строки
#
# get_domain_name("http://google.com") => "google"
# get_domain_name("http://google.co.jp") => "google"
# get_domain_name("www.xakep.ru") => "xakep"
# get_domain_name("https://youtube.com") => "youtube"
# get_domain_name("https://www.asos.com") => "asos"
# get_domain_name("http://www.lenovo.com") => "lenovo"
# Строка url может начинаться с протоколов http://  https:// или с www. URL, начинающиеся с протоколов
# http://  https://, могут также содержать www.
#
# Ваша задача написать только определение функции get_domain_name
#
# Про инструкцию assert можно прочитать здесь
#
# Sample Input:
#
# Sample Output:
#
# Проверки пройдены


def get_domain_name(url: str):
    url = url.replace('http://', '').replace('https://', '').replace('www.', '',1)
    lst = url.split('.')

    return lst[0]


print(get_domain_name("http://www.zombie-bites.com"))
