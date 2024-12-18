# В HTML используются специальные теги для определения заголовков в веб-странице.
#
# Всего существует шесть тегов заголовков HTML:
#
# <h1> - заголовок первого уровня;
# <h2> - заголовок второго уровня;
# <h3> - заголовок третьего уровня;
# <h4> - заголовок четвертого уровня;
# <h5> - заголовок пятого уровня;
# <h6> - заголовок шестого уровня.
# Разница между заголовками только в размере, на картинке можно наглядно это увидеть
#
# Ваша задача создать функцию make_header, которая принимает два параметра:
#
# text - строка, которую нужно обернуть в тег заголовка;
# level - целое число, обозначающее уровень заголовка.
# Функция make_header должна возвращать переданную строку в обернутый тег заголовка определенного уровня
#
# Ваша задача написать только определение функции make_header
#
# Sample Input 1:
#
# print(make_header('Нет', 1))
# Sample Output 1:
#
# <h1>Нет</h1>
# Sample Input 2:
#
# print(make_header('Bella Ciao', 4))
# Sample Output 2:
#
# <h4>Bella Ciao</h4>
# Sample Input 3:
#
# print(make_header(text='Go little rock star', level=6))
# Sample Output 3:
#
# <h6>Go little rock star</h6>
# Sample Input 4:
#
# print(make_header(level=2, text='Девальвации не будет. Твердо и четко'))
# Sample Output 4:
#
# <h2>Девальвации не будет. Твердо и четко</h2>


def make_header(text: str, level: int)->str:
    return f'<h{level}>{text}</h{level}>'


print(make_header(level=2, text='Девальвации не будет. Твердо и четко'))