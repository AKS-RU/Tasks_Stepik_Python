# Создайте базовый класс Person, у которого есть:

# метод __init__, принимающий имя и возраст человека. Их необходимо сохранить в атрибуты
# экземпляра nameи age соответственно

# метод display_person_info , который печатает информацию в следующем виде:
# Person: {name}, {age}


# Затем создайте класс Company , у которого есть:

# метод __init__, принимающий название компании и город ее основания. Их необходимо сохранить в
# атрибуты экземпляра company_name  и location соответственно

# метод display_company_info , который печатает информацию в следующем виде:
# Company: {company_name}, {location}


# И в конце создайте класс Employee , который:

# унаследован от классов Person и Company

# имеет метод __init__, принимающий имя человека, его возраст, название компании и город основания.
# Необходимо делегировать создание атрибутов nameи age  классу Person , а атрибуты company_name
# location должен создать класс Company
# После множественного наследования у экземпляров класса Employee  будут доступны методы
# родительских классов

# emp = Employee('Jessica', 28, 'Google', 'Atlanta')
# emp.display_person_info()
# emp.display_company_info()
# Sample Input:

# Sample Output:

# Person: Ivan, 32
# Company: Zara, Prague
# Person: Jessica, 28
# Company: Google, Atlanta
# Person: Kolya, 11
# Company: Facebook, Seatle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Person: {self.name}, {self.age}")


class Company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        print(f"Company: {self.company_name}, {self.location}")


class Employee(Person, Company):
    def __init__(self, name, age, company_name, location):
        super().__init__(name, age)
        Company.__init__(self, company_name, location)


a = Person("Ivan", 32)
a.display_person_info()

a = Company("Zara", "Prague")
a.display_company_info()

emp = Employee("Jessica", 28, "Google", "Atlanta")
emp.display_person_info()
emp.display_company_info()

emp2 = Employee("Kolya", 11, "Facebook", "Seatle")
emp2.display_person_info()
emp2.display_company_info()
