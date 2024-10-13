# Напишите функцию register_check, которая проверяет сколько человек успешно прошло регистрацию на мероприятие.
# Функция принимает словарь в качестве параметра, состоящий из имен людей(ключи) и результатов
# регистрации(значения ключа).
#
# Если человек успешно прошел регистрацию, то в словаре напротив его имени хранится значение «yes», иначе «no».
#
# Функция register_check должна возвращать количество только тех людей, кто успешно зарегистрировался.
#
# Sample Input 1:
#
# people = {'Igor': 'yes', 'Stas': 'no', 'Peter': 'no', 'Mary': 'yes'}
# print(register_check(people))
# Sample Output 1:
#
# 2
# Sample Input 2:
#
# people = {'Igor': 'no', 'Vasya': 'no', 'Peter': 'no', 'Mary': 'no'}
# print(register_check(people))
# Sample Output 2:
#
# 0
# Sample Input 3:
#
# people = {'Igor': 'yes', 'Vasya': 'yes', 'Peter': 'yes',
#           'Mary': 'no', 'Alex': 'yes', 'Marina': 'yes'}
# print(register_check(people))
# Sample Output 3:
#
# 5

def register_check(dct: dict):
    return [*dct.values()].count('yes')


people = {'Igor': 'yes', 'Vasya': 'yes', 'Peter': 'yes',
          'Mary': 'no', 'Alex': 'yes', 'Marina': 'yes'}
print(register_check(people))