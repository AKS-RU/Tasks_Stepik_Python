# Создайте бесконечный итератор в переменной math_progression, генерирующих арифметическую
# прогрессию, которая начинается с 100 с шагом 13

# От вас требуется только определить переменную math_progression

import itertools


math_progression = itertools.count(100, 13)

for i in range(10):
    print(next(math_progression))
