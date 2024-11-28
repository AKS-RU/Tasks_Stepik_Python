# Напишите функцию is_palindrome, которая определяет, является ли заданная строка палиндромом,
# используя deque для сравнения символов с начала и конца строки.

# Палиндро́м - слово или фраза, которые одинаково читаются слева направо и справа налево.

# Знаки пунктуации нужно исключать при проверке. Также регистр букв учитывать не нужно

# Функция is_palindrome должна вернуть True, если фраза является палиндромом, или False
# в противном случае.


from collections import deque


def is_palindrome(s: str) -> bool:
    queue = deque(list(filter(lambda x: x.isalpha(), s.lower())))
    queue_2 = queue.copy()
    queue_2.reverse()
    return queue == queue_2


print(is_palindrome("hello"))
