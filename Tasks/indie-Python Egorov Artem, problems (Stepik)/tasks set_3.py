# Конь Валера собрался с друзьями на вечеринку. Он давно следит за тенденциями моды и поэтому знает,
# что сейчас очень популярно носить все подковы разного цвета. С прошлого года у Валеры остались четыре подковы,
# но, возможно, некоторые из них имеют одинаковый цвет. В этом случае, чтобы не ударить в грязь лицом перед своими
# стильными товарищами, ему нужно сходить в магазин и купить дополнительно несколько каких-нибудь подков.
#
# К счастью в магазине продаются подковы всех возможных цветов, и у Валеры имеется достаточно денег, чтобы купить
# любые четыре. Однако в целях экономии он хотел бы потратить как можно меньше денег, поэтому вам нужно помочь Валере
# и определить, какое минимальное количество подков нужно купить, чтобы он смог надеть на вечеринку четыре подковы
# различного цвета.
#
# Входные данные
# В первой строке через пробел записаны четыре целых числа s1,s2,s3,s4 (1≤s1,s2,s3,s4≤109) — цвета подков, имеющихся
# у Валеры.
#
# Считайте, что все возможные цвета пронумерованы целыми числами.
#
# Выходные данные
# Выведите единственное целое число — минимальное количество подков, которое нужно купить.
#
# Sample Input 1:
#
# 1 7 3 3
# Sample Output 1:
#
# 1
# Sample Input 2:
#
# 7 7 7 7
# Sample Output 2:
#
# 3

print(4 - len(set(map(int,input().split()))))