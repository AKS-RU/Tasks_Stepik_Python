# Ваша задача сохранить все дни в хронологическом порядке, которые были в ноябре 2001 года, в
# переменную sweet_november
#
# Выводить ничего не требуется, только создать список из дат


from datetime import date

sweet_november = [date(2001, 11, i) for i in range(1, 31)]
print(sweet_november)
