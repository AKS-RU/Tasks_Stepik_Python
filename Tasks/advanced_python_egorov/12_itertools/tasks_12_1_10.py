# Усовершенствуем предыдущую функцию infinity_generate, так, чтобы она стала принимать второй необязательный аргумент offset - смещение последовательности, по умолчанию 0. Параметр offset должен влиять на начальное значение, от которого генерируются значения внутри функции infinity_generate.

# Разберем на примере строки ABCDE. При offset=0 генерация будет обычной A->B->C->D->E->A...

# При offset=1 начинать будем с буквы B и тогда получим генерацию B->C->D->E->A->B->...

# При offset=2 начинать будем с буквы C и тогда получим генерацию C->D->E->A->B->C->...

# При offset=5 мы вновь будем начинать с буквы A и тогда получим генерацию A->B->C->D->E->A...

# Значение смещение может быть отрицательным, тогда при offset=-1 начинать будем с последней
# буквы E и получим генерацию E->A->B->C->D->E->...

# При offset=-2 начинать будем с предпоследней буквы D и получим генерацию D->E->A->B->C->D->...

import itertools


def infinity_generate(lst: list, offset=0):
    if not offset:
        return itertools.cycle(lst)
    result = []
    for index in range(len(lst)):
        result.append(lst[(index + offset) % len(lst)])
    return itertools.cycle(result)


count = 0
for i in infinity_generate('ABCDEF', 1):
    print(i)
    count += 1
    if count > 10:
        break
