# Программе на вход поступают слова, разделенные пробелом. Ваша задача проверить, во всех ли словах есть английская
# буква A вне зависимости от регистра. В качестве ответа программа должна вывести True или False.
#
# Sample Input 1:
#
# chase enlarge referee cup offense
# Sample Output 1:
#
# False
# Sample Input 2:
#
# acquaintance disAgree
# Sample Output 2:
#
# True

print(all('a' in i for i in input().lower().split()))




