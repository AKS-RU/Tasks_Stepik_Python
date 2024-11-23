# Напиши программу, которая принимает на вход строку даты в формате dd-mm-yyyy и выводит на экран
# дату на 30 дней раньше введенной даты, затем саму текущую дату и позже текущей даты также
# на 30 дней в следующем формате
#
# 30 days before current date: <30_days_before>
# Current Date: <current_date>
# 30 days after current date: <30_days_after>


from datetime import date, datetime, timedelta

current_date = datetime.strptime(input(), '%d-%m-%Y').date()
step_date = timedelta(days=30)
print(f'30 days before current date: {datetime.strftime(current_date - step_date, '%d.%m.%Y')}')
print(f'Current Date: {datetime.strftime(current_date, '%d.%m.%Y')}')
print(f'30 days after current date: {datetime.strftime(current_date + step_date, '%d.%m.%Y')}')
