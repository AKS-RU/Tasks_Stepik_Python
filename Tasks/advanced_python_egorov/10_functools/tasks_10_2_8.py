# Перед встречей с друзьями у вас было 15000р, после осталось только 950р. В этот вечер вы отлично
# провели с ними время в кафе. Договорились, что за все оплачиваете вы, а
# затем они отправят вам свою часть счета.

# Посчитайте, сколько денег вы потратили в итоге, после того как все друзья отправят деньги.

# На вход программе поступают целые числа через пробел в одну строку - переводы от друзей за
# свою часть счета.

# Ваша вывести на экран сколько вы потратили

# Примечание: используйте для решения функцию reduce

from functools import reduce

friend = reduce(lambda x, y: x+y, list(map(int, input().split())))
print(15000 - 950 - friend)
