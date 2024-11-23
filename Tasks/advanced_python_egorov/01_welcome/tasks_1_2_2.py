# Slugify
# Напишите функцию slugify , которая должна принимать на вход строку и возвращать ее в формате,
# пригодном для использования в URL. Функция должна выполнить следующие преобразования
# входной строки:
#
# Привести все символы строки к нижнему регистру
#
# Удалить все незначащие символы пробелов слева и справа
#
# Удалить все символы пунктуации из набора !@#$%^&*()_+={}[]|\:;'<>,.?/~`
#
# Оставшиеся пробелы заменить на дефисы «-»
#
# Удалить все повторяющиеся дефисы


def slugify(url: str) -> str:
    exception = r"!@#$%^&*()_+={}[]|\;:'<>,.?/~`"
    url = '-'.join(url.lower().strip().replace('-', ' ').split())
    url = ''.join([i for i in url if i not in exception])
    return url


assert slugify("Hello World") == "hello-world"
assert slugify("Hello, World!") == "hello-world"
assert slugify("The 20th Century") == "the-20th-century"
assert slugify("    Hello      World     ") == "hello-world"
assert slugify("Hello World   ") == "hello-world"
assert slugify("") == ""
assert slugify("!@#$%^&*()_+={}[]|\:;'<>,.?/~`") == ""
assert slugify('hello----world') == 'hello-world'

print(slugify("What is My Name?"))
print(slugify("    Hello      World     "))
