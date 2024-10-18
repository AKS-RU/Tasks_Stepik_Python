# Создайте класс Library, который имеет следующие методы:
#
# метод __init__, который принимает список названий книг и сохраняет его в приватном атрибуте __books.
#
# приватный метод check_availability, который принимает название книги и возвращает True, если книга присутствует
# в библиотеке, в противном случае возвращается False.
#
# публичный метод search_book, который ищет книгу в библиотеке при помощи приватного метода check_availability.
# Возвращает True, если нашел,  иначе False.
#
# публичный метод return_book, который принимает название книги, которую нужно вернуть в библиотеку
# (добавить в конец атрибута __books), ничего возвращать не нужно.
#
# защищенный метод checkout_book, который принимает на вход название книги. Если книга имеется в наличии,
# ее необходимо выдать читателю и удалить из списка книг. Метод в таком случае должен вернуть True , как знак того,
# что операция выдачи книги прошла успешно. Если книга отсутствовала, необходимо вернуть False.


class Library:

    def __init__(self, books: list):
        self.__books = books

    def __check_availability(self, is_book):
        return is_book in self.__books

    def search_book(self, is_book):
        return self.__check_availability(is_book)

    def return_book(self, return_book):
        self.__books.append(return_book)

    def _checkout_book(self, issue_book):
        if issue_book in self.__books:
            self.__books.remove(issue_book)
            return True
        return False


print('*' * 15, 'ТЕСТЫ', '*' * 15)
library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])

assert library._Library__books == ["War and Peace", "Moby-Dick", "Pride and Prejudice"]
assert library.search_book("Moby-Dick") == True
assert library.search_book("Jane Air") == False

assert library._Library__check_availability("War and Peace") == True
assert library._checkout_book("Moby-Dick") == True
assert library._Library__books == ["War and Peace", "Pride and Prejudice"]

assert library.search_book("Moby-Dick") == False
assert library.return_book("Moby-Dick") is None
assert library._Library__books == ["War and Peace", "Pride and Prejudice", "Moby-Dick"]
assert library.search_book("Moby-Dick") == True
print('Все тесты пройдены успешно!')
