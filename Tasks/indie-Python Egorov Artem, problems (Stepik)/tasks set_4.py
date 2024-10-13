# Слово или предложение на некотором языке называется панграммой, если в нем встречаются все символы алфавита
# этого языка хотя бы один раз. Панграммы часто используют в типографии для демонстрации шрифтов или тестирования
# средств вывода различных устройств.
#
# Вам дана строка, состоящая из маленьких и больших латинских букв. Проверьте, является ли эта строка панграммой.
# Считается, что строка содержит букву латинского алфавита, если эта буква встречается в верхнем или нижнем регистре.
#
# Входные данные
# Программа получает на вход строку, содержащую исключительно строчные и заглавные латинские буквы.
#
# Выходные данные
# Выведите «YES», если строка является панграммой, и «NO» в противном случае.
#
# Sample Input 1:
#
# toosmallword
# Sample Output 1:
#
# NO
# Sample Input 2:
#
# TheQuickBrownFoxJumpsOverTheLazyDog
# Sample Output 2:
#
# YES

print('YES' if len(set(input().lower())) == 26 else 'NO')
