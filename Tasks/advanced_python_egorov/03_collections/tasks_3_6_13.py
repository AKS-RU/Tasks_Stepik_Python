# В вашем распоряжении имеется строка magic. Ваша задача накопить для каждой буквы в виде списка
# индексы, где данная буква встречается в слове. Результат агрегирования всех букв должен быть ,
# хранящийся в переменной statistics

# Например, если бы строка magic имела значение hello, то результат был бы следующий defaultdict

# defaultdict(<class 'list'>, {'h': [0], 'e': [1], 'l': [2, 3], 'o': [4]})
# Ваша задача создать значение переменной statistics и правильно ее наполнить.


from collections import defaultdict


# magic = 'hello'
magic = 'abracadabraabracadabraabracadabra'
statistics = defaultdict(list)

for i, k in enumerate(magic):
    statistics[k].append(i)

print(statistics)
