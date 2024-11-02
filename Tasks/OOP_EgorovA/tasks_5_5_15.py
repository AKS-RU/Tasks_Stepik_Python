class Initialization:

    def __init__(self, capacity, food):
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = food
        else:
            print('Количество людей должно быть целым числом')


class Vegetarian(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'


class MeatEater(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'


class SweetTooth(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'

    def __eq__(self, value):
        if isinstance(value, int):
            return self.capacity == value
        elif isinstance(value, (Vegetarian, MeatEater)):
            return self.capacity == value.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {value}'

    def __lt__(self, value):
        if isinstance(value, int):
            return self.capacity < value
        elif isinstance(value, (Vegetarian, MeatEater)):
            return self.capacity < value.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {value}'

    def __gt__(self, value):
        if isinstance(value, int):
            return self.capacity > value
        elif isinstance(value, (Vegetarian, MeatEater)):
            return self.capacity > value.capacity
        else:
            return f'Невозможно сравнить количество сладкоежек с {value}'


p1 = Initialization('Chuck', [])
assert isinstance(p1, Initialization)
assert not hasattr(
    p1, 'capacity'), 'Не нужно создавать атрибут "capacity", если передается не целое число'
assert not hasattr(
    p1, 'food'), 'Не нужно создавать атрибут "food", если передается не целое число'

c1 = Vegetarian(100, [1, 2, 3])
print(c1)
assert isinstance(c1, Vegetarian)
assert c1.capacity == 100
assert c1.food == [1, 2, 3]

b1 = MeatEater(1000, ['Arkasha'])
print(b1)
assert isinstance(b1, MeatEater)
assert b1.capacity == 1000
assert b1.food == ['Arkasha']

pla = SweetTooth(444, [2150, 777])
print(pla)
assert isinstance(pla, SweetTooth)
assert pla.capacity == 444
assert pla.food == [2150, 777]
assert pla > 100
assert not pla < 80
assert not pla == 90
assert pla > c1
assert not pla < c1
assert not pla == c1
assert not pla > b1
assert pla < b1
assert not pla == b1

v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
# 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
print(v_first)
# Количество людей должно быть целым числом
v_second = Vegetarian([23], ['nothing'])

m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
# 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
print(m_first)
s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
# Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
print(s_first)
# Сладкоежек больше, чем людей с другим вкусовым предпочтением
print(s_first > v_first)
# Количество сладкоежек из опрошенных людей совпадает с 30000
print(30000 == s_first)
print(s_first == 25000)  # Количество людей не совпадает
print(100000 < s_first)  # Количество сладкоежек в Москве не больше, чем 100000
print(100 < s_first)  # Количество сладкоежек больше, чем 100
print('ok  ')
