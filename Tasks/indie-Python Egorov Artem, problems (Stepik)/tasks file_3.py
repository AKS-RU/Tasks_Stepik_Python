# Напишите функцию longest_word_in_file, которая принимает имя файла и внутри его содержимого находит самое
# длинное слово и возвращает его в качестве ответа. В случае,  если есть несколько слов с максимальной длиной,
# нужно вернуть слово, которое встречается последнее в тексте.
#
# При этом слова в тексте отделяются друг от друга пробелами, любые другие знаки пунктуации необходимо исключить.
# И также учитывайте, что слова в тестах будут как на русском языке, так и на английском.
#
# Если бы содержимое файла было таким:
#
# He was running, but it was like running through deep water. There were trees all around him,
# trees which tried to stop him. They reached out with their branches.
# And it was behind him. It was coming nearer.
# то ответом было бы слово branches
#
# Все возможные знаки пунктуации можно получить из модуля string
#
# from string import punctuation

def longest_word_in_file(file_name: str):
    from string import punctuation
    file = open(file_name,encoding='utf-8')
    lst = file.read().split()
    result = ''
    for i in lst:
        i = i.strip(punctuation)
        if len(i) >= len(result):
            result = i
    file.close()
    return result

print(longest_word_in_file('test.txt'))