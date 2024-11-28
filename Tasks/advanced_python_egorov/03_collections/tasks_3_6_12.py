# Перед вами список кортежей subjects, в котором элемент представляет собой информацию о
# предмете и имени студента

# Напишите программу которая сгруппирует имена студентов по предметам, которые они изучают,
# и выведет информацию в следующем виде

# Предмет1: Студент1,Студент2,Студент3
# Предмет2: Студент4,Студент5
# Сами предметы должны располагаться в алфавитном порядке, и имена студентов в пределах одного
# предмета тоже необходимо отсортировать по алфавиту


from collections import defaultdict


subjects = [('Mathematics', 'Alice Brown'),
            ('Mathematics', 'Bob Smith'),
            ('Physics', 'Cindy Lee'),
            ('Chemistry', 'David Johnson'),
            ('Biology', 'Eva Martinez'),
            ('English', 'Frank Davis'),
            ('History', 'Gina Rodriguez'),
            ('Mathematics', 'Hannah Kim'),
            ('Mathematics', 'Ian Chen'),
            ('Physics', 'Jackie Lee'),
            ('Chemistry', 'Kevin Wang'),
            ('Biology', 'Lucy Wong'),
            ('English', 'Michael Johnson'),
            ('History', 'Nadia Ali'),
            ('Mathematics', 'Olivia Taylor'),
            ('Mathematics', 'Peter Wong'),
            ('Physics', 'Quinn Jackson'),
            ('Chemistry', 'Rachel Chen'),
            ('Biology', 'Sarah Kim'),
            ('English', 'Thomas Smith'),
            ('History', 'Uma Patel'),
            ('Mathematics', 'Vivian Liu'),
            ('Mathematics', 'William Zhang'),
            ('Physics', 'Xavier Lee'),
            ('Chemistry', 'Yara Ahmed'),
            ('Biology', 'Zoe Chen'),
            ('English', 'Alan Davis'),
            ('History', 'Beth Lee'),
            ('Mathematics', 'Charlie Brown'),
            ('Mathematics', 'Diana Smith'),
            ('Physics', 'Emily Johnson')]

result = defaultdict(list)
for key, value in subjects:
    result[key].append(value)

print(*(f"{k}: {','.join(sorted(v))}" for k, v in sorted(result.items(),
      key=lambda x: x[0])), sep='\n')
