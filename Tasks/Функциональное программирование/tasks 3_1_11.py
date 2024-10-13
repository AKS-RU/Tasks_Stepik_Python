# Определите функцию create_palindrome, которая принимает строку  и возвращает результат в зависимости от
# следующих условий
#
# Если переданная строка уже является палиндромом вне зависимости от регистра букв, вернуть ее, преобразовав все
# символы к нижнему регистру, иначе идем к следующему пункту
#
# Создать палиндром по следующему формату
# {str}_i_{reverse_str}
# где str - переданная строка, а reverse_str ее перевернутое значение. Верните вновь созданный палиндром в качестве
# ответа, преобразовав все символы к нижнему регистру
#
# Sample Input 1:
#
# print(create_palindrome('Rotator'))
# Sample Output 1:
#
# rotator
# Sample Input 2:
#
# print(create_palindrome('Hello'))
# Sample Output 2:
#
# hello_i_olleh

def create_palindrome(text: str):
    reverse_text = text[::-1].lower()
    text = text.lower()
    if text == reverse_text:
        return text
    return f'{text}_i_{reverse_text}'

print(create_palindrome('Hello'))


