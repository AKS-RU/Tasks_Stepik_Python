# Вклад в банке
# Ваш друг работает в одном «желтом » банке и попросил вас запрограммировать нахождение
# накопленного капитала для клиента по вкладу. Входными данными для программы будут:

# первоначальная сумма вклада

# ставка вклада в процентах

# срок вклада
# При расчетах используется схема сложных процентов: проценты после каждого года капитализируются,
# то есть добавляются к счету в банке, и со следующего года расчет процентов осуществляется
# от суммы, увеличенной на значение накопленных процентов.

# К примеру, если клиент вложил 1000 под 5% годовых на 4 года, то в конце срока клиент
# получит прибыль 215.50625.

# Ваша программа должна рассчитать и вывести на экран итоговую сумму, которую получит
# вкладчик в конце срока действия вклада. При этом итоговый результат нужно будет округлить
# до 4 знаков после запятой при помощи режима ROUND_UP


from decimal import Decimal, ROUND_UP


deposit, percent, term = Decimal(input()), Decimal(input()), Decimal(input())

while term > 0:
    deposit += deposit * percent / 100
    term -= 1

print(deposit.quantize(Decimal('0.0001'), rounding=ROUND_UP))
