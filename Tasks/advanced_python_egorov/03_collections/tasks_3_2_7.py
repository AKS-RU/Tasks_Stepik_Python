# Контактная книга
# Ваша задача разработать программу для управления контактами. Вам необходимо создать класс
# ContactBook, который наследует функциональность базового словаря через UserDict, чтобы обеспечить
# удобное добавление, обновление, удаление и отображение контактов.
#
# Класс ContactBook должен иметь следующие дополнительные методы:
#
# add_contact(name, phone_number) метод для добавления контакта в контактную книгу, если указанному
# имени в телефонной книге не существовало. В случае успешного добавления печатает сообщение
# «Контакт {name} создан». Если контакт с таким именем уже существует, то метод выводит
# сообщение «Контакт {name} уже существует».
#
# update_contact(name, new_phone_number) метод для обновления номера телефона существующего контакта.
# Принимает имя контакта и новый номер телефона. Если контакт с указанным именем существует,
# обновляет его номер телефона. Если контакт не найден, выводит сообщение «Контакт {name} не найден»
#
# delete_contact(name) метод для удаления контакта по имени. Если контакт с указанным именем
# существует, удаляет его из контактной книги и выводит сообщение «Контакт {name} успешно удален».
# Если контакт не найден, выводит сообщение «Контакт {name} не найден»
#
# display_contacts() метод для отображения всех контактов в контактной книге. Если контактов нет,
# выводит сообщение «Телефонный список пуст» В противном случае, выводит список всех контактов в
# формате "Имя: Номер телефона" в порядке добавления
#
# Вы должны создать класс ContactBook, наследующий функциональность базового словаря UserDict, и
# реализовать описанные методы для управления контактами.


from collections import UserDict


class ContactBook(UserDict):

    def add_contact(self, name, phone_number):
        if not self.is_name_dict(name):
            self.data[name] = phone_number
            print(f'Контакт {name} создан')
        else:
            print(f'Контакт {name} уже существует')

    def update_contact(self, name, new_phone_number):
        if self.is_name_dict(name):
            self.data[name] = new_phone_number
        else:
            print(f'Контакт {name} не найден')

    def delete_contact(self, name):
        if self.is_name_dict(name):
            self.data.pop(name)
            print(f'Контакт {name} успешно удален')
        else:
            print(f'Контакт {name} не найден')

    def display_contacts(self):
        print(*(f'{k}: {v}' for k, v in self.data.items()), sep='\n')

    def is_name_dict(self, name):
        return name in self.data


contact_book = ContactBook()
contact_book.add_contact("John", "123-456-7890")
assert contact_book.data['John'] == "123-456-7890"
contact_book.add_contact("John", "345-666")  # Печатает Контакт John уже существует.
contact_book.add_contact("Alice", "987-654-3210")
assert contact_book.data['Alice'] == "987-654-3210"
contact_book.display_contacts()

contact_book.update_contact("John", "111-222-3333")
assert contact_book.data['John'] == "111-222-3333"
contact_book.display_contacts()

contact_book.delete_contact("Alice")
assert 'Alice' not in contact_book.data
contact_book.display_contacts()
print('OK')
