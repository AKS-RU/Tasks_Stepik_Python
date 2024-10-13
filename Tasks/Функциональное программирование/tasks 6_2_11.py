# Напишите функцию get_letters, которая принимает строку и формирует из нее список кортежей. Каждый элемент кортежа будет состоять из двух значений: берется соответствующая буква сперва в верхнем регистре, а затем в нижнем (см. примеры ниже)
#
# Sample Input 1:
#
# print(get_letters('TykPe'))
# Sample Output 1:
#
# [('T', 't'), ('Y', 'y'), ('K', 'k'), ('P', 'p'), ('E', 'e')]
# Sample Input 2:
#
# print(get_letters('MeSsi'))
# Sample Output 2:
#
# [('M', 'm'), ('E', 'e'), ('S', 's'), ('S', 's'), ('I', 'i')]
# Sample Input 3:
#
# print(get_letters('WelLDone'))
# Sample Output 3:
#
# [('W', 'w'), ('E', 'e'), ('L', 'l'), ('L', 'l'), ('D', 'd'), ('O', 'o'), ('N', 'n'), ('E', 'e')]


def get_letters(text: str)->list[tuple]:
    return list(map(lambda x: (x.upper(), x.lower()),text))


print(get_letters('MeSsi'))