# Ваша задача из обычного класса Student
#
# class Student:
#     def __init__(self, name, surname, student_id, faculty, specialty):
#         self.student_id = student_id
#         self.name = name
#         self.surname = surname
#         self.faculty = faculty
#         self.specialty = specialty
#
#
# student_1 = Student("Иван", "Иванов", 12345, "Физический", "Математика")
#
# student_2 = Student("Анна", "Смирнова", 67890, "Химический", "Биология")
# сделать дата-класс
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    surname: str
    student_id: int
    faculty: str
    specialty: str


student_1 = Student("Иван", "Иванов", 12345, "Физический", "Математика")
print(student_1)
