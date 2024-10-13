# Напишите функцию repeat_phrase_n_times, которая имеет два параметра: phrase и n. Функция repeat_phrase_n_times
# должна вывести n раз текст, который был передан в параметр phrase
#
# Ваша задача только написать определение функции repeat_phrase_n_times
#
# Sample Input:
#
# repeat_phrase_n_times('Белье надевают под одежду', 4)
# Sample Output:
#
# Белье надевают под одежду
# Белье надевают под одежду
# Белье надевают под одежду
# Белье надевают под одежду

def repeat_phrase_n_times(phrase, n):
    for _ in range(n):
        print(phrase)

repeat_phrase_n_times('gjhgjhgjhgj', 5)