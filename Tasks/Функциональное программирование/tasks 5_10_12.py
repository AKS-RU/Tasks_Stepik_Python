# Перед вами реализация двух функций-декораторов  first_validator и second_validator.
#
# Также имеется функция sum_values.
#
# Вам необходимо сперва проанализировать имеющийся код и разобраться, как он работает.
#
# После этого вашей задачей является:
#
#    ✔️ наложить два декоратора на функцию sum_values в правильной последовательности;
#
#    ✔️ вызвать задекорированную функцию sum_values подобрав аргументы так, чтобы совпал вывод результата.
#
# Код самих функций менять не нужно.
#
# Sample Input:
#
# Sample Output:
#
# Начинаем самую важную проверку
# Начинаем важную проверку
# Получили результат равный 77
# Заканчиваем важную проверку
# Заканчиваем самую важную проверку



def first_validator(func):
    def my_wrapper(*args, **kwargs):
        print(f"Начинаем важную проверку")
        if len(args) == 3:
            func(*args, **kwargs)
        else:
            print(f"Важная проверка не пройдена")
            return None
        print(f"Заканчиваем важную проверку")

    return my_wrapper


def second_validator(func):
    def my_wrapper(*args, **kwargs):
        print(f"Начинаем самую важную проверку")
        if kwargs.get('name') == 'Boris':
            func(*args)
        else:
            print(f"Самая важная проверка не пройдена")
            return None
        print(f"Заканчиваем самую важную проверку")

    return my_wrapper


# используйте декораторы
@second_validator
@first_validator
def sum_values(*args, **kwargs):
    print(f'Получили результат равный {sum(args)}')


sum_values(1,2,74, name='Boris')