# Имеется функция wrap_increment, которая должна принимать значение и увеличивать его на 1. Увеличение на один должно
# выполняться за счет вложенной функции _inc.
#
# Ваша задача дописать в теле wrap_increment определение функции _inc, которая принимает значение и увеличивает его.
#
#
# Sample Input:
#
# print(wrap_increment(41))
# Sample Output:
#
# 42

def wrap_increment(value):
    # определите вложенную функцию _inc
    def _inc(value):
        value+=1
        return value
    return _inc(value)


print(wrap_increment(41))