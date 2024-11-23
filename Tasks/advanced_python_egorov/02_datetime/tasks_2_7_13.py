# Напишите программу, которая принимает на вход строку даты в формате mm/dd/yyyy и выводит
# на экран 15 следующих дней в формате dd.mm.yyyy


from datetime import datetime, date, timedelta

current_date = datetime.strptime(input(), '%m/%d/%Y').date()
print(*((current_date + timedelta(days=i)).strftime('%d.%m.%Y') for i in range(1, 16)), sep='\n')
