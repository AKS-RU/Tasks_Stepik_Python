# Напишите функцию rotate_letter, которая принимает два аргумента:
#
# letter - одна английская буква в нижнем регистре
# shift целое число - значение сдвига буквы (может быть как положительным, так и отрицательным)
# Функция rotate_letter по переданному значению сдвига shift находит новую букву относительно текущей позиции буквы
# letter в алфавите. Сдвиг может быть цикличным в пределах от a до z как в вправо (при положительном значении shift),
# так и влево (при отрицательном значении shift). Ниже представлены примеры работы функции rotate_letter:
#
# rotate_letter('b', 2)=> 'd'
# rotate_letter('d', 1) => 'e'
# rotate_letter('z', 1) => 'a'
# rotate_letter('d', -2) => 'b'
# rotate_letter('d', 26) => 'd'
# rotate_letter('b', -3) => 'y'
# Требования к функции rotate_letter:
#
#      ✔️  должна вернуть новый символ;
#
#      ✔️ параметры и возвращаемое значение должны быть проаннотированы
#
#      ✔️ добавьте doc-строку «Функция сдвигает символ letter на shift позиций»
#
#
#
# Для решения вам поможет таблица ascii кодов английских букв. В ней обратите внимание только на символы в
# нижнем регистре:
#
#
#
# Для преобразования символа в код ascii и наоборот вам потребуются функции ord и chr
#
# Sample Input 1:
#
# print(rotate_letter.__doc__)
# print(rotate_letter.__annotations__)
# print(rotate_letter('a', 3))
# Sample Output 1:
#
# Функция сдвигает символ letter на shift позиций
# {'letter': <class 'str'>, 'shift': <class 'int'>, 'return': <class 'str'>}
# d
# Sample Input 2:
#
# print(rotate_letter.__annotations__)
# print(rotate_letter('d', -2))
# Sample Output 2:
#
# {'letter': <class 'str'>, 'shift': <class 'int'>, 'return': <class 'str'>}
# b
# Sample Input 3:
#
# print(rotate_letter('w', -26))
# Sample Output 3:
#
# w
# Sample Input 4:
#
# print(rotate_letter('w', -27))
# Sample Output 4:
#
# v
# Sample Input 5:
#
# print(rotate_letter('a', 53))
# Sample Output 5:
#
# b

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
            result = end - (start-result + 1)
    return chr(result)


print(rotate_letter.__annotations__)
print(rotate_letter('c', -120))
