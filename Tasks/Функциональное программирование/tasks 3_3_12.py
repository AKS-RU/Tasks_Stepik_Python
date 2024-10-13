# Rövarspråket (со шведского переводится как «язык разбойника») - шведская языковая игра. Она стала популярной
# после книг Астрид Линдгрен о Билле Бергсоне, где дети используют ее в качестве кода, как в игре, так и при
# раскрытии настоящих преступлений.
#
# Формула кодирования проста: каждая согласная удваивается, а между ними вставляется буква o. Гласные остаются
# нетронутыми.
#
# Тогда согласно этим правилам слово
#
# stubborn
#
# превратится в
#
# sostotubobboborornon
#
# Ваша задача написать функцию translate_to_robber_lang(), которая будет переводить текст на «язык разбойника»
# (по-шведски ).
# Все символы, которые не являются буквами, должны оставаться без изменения.
#
# Гласными будем считать буквы ['a','e', 'i', 'o', 'u']
#
# Sample Input 1:
#
# print(translate_to_robber_lang("This is kinda fun"))
# Sample Output 1:
#
# ToThohisos isos kokinondoda fofunon
# Sample Input 2:
#
# print(translate_to_robber_lang("I Think YoU Might BE righT!"))
# Sample Output 2:
#
# I ToThohinonkok YoYoU MoMigoghohtot BoBE rorigoghohToT!

a = ['a', 'e', 'i', 'o', 'u']


def translate_to_robber_lang(phrase: str):
    result = ''
    for i in phrase:
        for j in i:
            if j.lower() not in a and j.isalpha():
                result += j + 'o' + j
            else:
                result += j
    return result

print(translate_to_robber_lang("This is kinda fun"))
