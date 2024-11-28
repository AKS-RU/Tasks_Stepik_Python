# Перед вами список кортежей subjects, в котором элемент представляет собой информацию о предмете
# и имени студента

# Напишите программу которая найдет сколько студентов изучает определенный предмет, и выведет
# информацию о каждом предмете в следующем виде

# Предмет1: КоличествоСтудентов
# Предмет2: КоличествоСтудентов
# ....
# Сами предметы должны располагаться в порядке убывания подсчитанного количество студентов.
# Предметы, у которых совпадает количество студентов, необходимо расположить между собой
# в алфавитном порядке


from collections import defaultdict


subjects = [('Mathematics', 'Alice Brown'),
            ('Mathematics', 'Bob Smith'),
            ('Physics', 'Cindy Lee'),
            ('Chemistry', 'David Johnson'),
            ('Biology', 'Eva Martinez'),
            ('English', 'Frank Davis'),
            ('History', 'Gina Rodriguez'),
            ('Biology', 'Henry Wong'),
            ('Mathematics', 'Isabella Torres'),
            ('Physics', 'Jacob Hernandez'),
            ('Chemistry', 'Kevin Davis'),
            ('Biology', 'Liam Johnson'),
            ('English', 'Mia Anderson'),
            ('History', 'Noah Wilson'),
            ('Mathematics', 'Olivia Brown'),
            ('Physics', 'Paula Garcia'),
            ('Chemistry', 'Quincy Jones'),
            ('Biology', 'Robert Lee'),
            ('English', 'Sophia Davis'),
            ('History', 'Thomas Martinez'),
            ('Mathematics', 'Uma Patel'),
            ('Physics', 'Victor Brown'),
            ('Chemistry', 'William Johnson'),
            ('Biology', 'Xander Smith'),
            ('English', 'Yara Gonzalez'),
            ('History', 'Zoe Hernandez'),
            ('Mathematics', 'Aaron Davis'),
            ('Physics', 'Brian Wilson'),
            ('Chemistry', 'Catherine Brown'),
            ('Biology', 'Daniel Hernandez'),
            ('English', 'Emily Johnson'),
            ('History', 'Fiona Lee'),
            ('Mathematics', 'Gabriel Rodriguez'),
            ('Physics', 'Hannah Martinez'),
            ('Chemistry', 'Ian Smith')]


result = defaultdict(int)

for key, value in subjects:
    result[key] += 1

for key, value in sorted(result.items(), key=lambda x: (-x[1], x[0])):
    print(f'{key}: {value}')
