# Конвертер валют
# Ваша задача — разработать программу-конвертер валют, которая позволяет пользователям переводить
# из USD в EUR на основе текущего обменного курса. Ваша программа должна запросить следующие данные:

# Обменный курс между долларом и евро
# Исходная сумма в долларах - сумма денег, которую пользователь хочет конвертировать.
# Программа должна затем вычислить и вывести на экран эквивалентную сумму в евро.


from decimal import Decimal


rate = Decimal(input())
quant_eur = Decimal(input())

print(rate*quant_eur)
