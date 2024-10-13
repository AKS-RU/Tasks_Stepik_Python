# Шифр цезаря
# На основании функции rotate_letter из предыдущего задания мы с вами можем реализовать знаменитый шифр Цезаря.
# Этот шифр берет каждую букву исходной фразы и смещает ее на значение ключа. Под ключом здесь подразумевается
# значение сдвига shift. В пределах кодирования одной фразы значение сдвига всегда постоянно.
#
# И так, ваша задача создать функцию caesar_cipher, которая имеет два обязательных параметра:
#
#      1️⃣ phrase входной текст для шифрования
#
#      2️⃣ key значение ключа шифра, он же сдвиг.
#
# Внутри функции caesar_cipher  необходимо последовательно пройтись по каждому символу и преобразовать его по
# следующим правилам:
#
# если символ является знаком пунктуации, оставляем его как есть
# если это буква, то сместить ее при помощи ранее написанной функции rotate_letter  на значение ключа
# Закодированный текст необходимо вернуть в качестве ответа. Вот пример работы
#
# caesar_cipher('leave out all the rest', -1) => 'kdzud nts zkk sgd qdrs'
# caesar_cipher('one more light', 3) => 'rqh pruh oljkw'
# Для успешного решения напишите реализацию функции caesar_cipher, которая использует функцию rotate_letter.
# (нужно продублировать определение функции rotate_letter из предыдущего урока).
#
# Дополнительно нужно :
#
#      ✔️  сделать аннотацию параметров и возвращаемого значения всех функций
#
#      ✔️  сделать док-строку для функции caesar_cipher со значением «Шифр Цезаря»
#
# Sample Input 1:
#
# print(caesar_cipher.__annotations__)
# print(caesar_cipher.__doc__)
# print(caesar_cipher('lost in the echo', 1))
# Sample Output 1:
#
# {'phrase': <class 'str'>, 'key': <class 'int'>, 'return': <class 'str'>}
# Шифр Цезаря
# mptu jo uif fdip
# Sample Input 2:
#
# print(caesar_cipher.__annotations__)
# print(caesar_cipher.__doc__)
# print(caesar_cipher('from the inside', 10))
# Sample Output 2:
#
# {'phrase': <class 'str'>, 'key': <class 'int'>, 'return': <class 'str'>}
# Шифр Цезаря
# pbyw dro sxcsno
# Sample Input 3:
#
# print(caesar_cipher('leave out all the rest', -4))
# Sample Output 3:
#
# hawra kqp whh pda naop
# Sample Input 4:
#
# print(caesar_cipher('one more light', -3))
# Sample Output 4:
#
# lkb jlob ifdeq
# Sample Input 5:
#
# print(caesar_cipher('lost in the echo', -120))
# Sample Output 5:
#
# vycd sx dro omry


def rotate_letter(letter: str, shift: int = 1) -> str:
    'Функция сдвигает символ letter на shift позиций'
    let_ord = ord(letter)
    start = ord('a')  # ascii соответствует символу 'a'
    end = ord('z')  # ascii соответствует символу 'z'
    sh = abs(shift) % 26
    if shift > 0:
        result = let_ord + sh
        if result > end:
            result = (result - end - 1) + start
    else:
        result = let_ord - sh
        if result < start:
            result = end - (start - result - 1)
    return chr(result)


def caesar_cipher(phrase: str, key: int) -> str:
    'Шифр Цезаря'
    return ''.join([rotate_letter(i, key) if i.isalpha() else i for i in phrase])


print(caesar_cipher.__annotations__)
print(caesar_cipher.__doc__)
print(caesar_cipher('lost in the echo', -120))
print(dir())
print('*'*30)
print(globals())
