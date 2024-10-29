# Нам необходимо создать класс Building. Мы должны научиться создавать здание определенной этажности и уметь
# бронировать за компанией определенный этаж в здании. Важно, что в нашем классе за одним этажом может быть
# закреплена только одна компания
#
# Для этого в классе Building должны быть реализованы:
#
# метод __init__, который принимает количество этажей в здании;
#
# метод __setitem__, который закрепляет за определенным этажом компанию. Если этаж был занят другой компанией,
# нужно заменить название другой компанией;
#
# метод __getitem__, который возвращает название компании с этого этажа. В случае, если этаж пустует, следует вернуть None;
#
# метод __delitem__, который высвобождает этаж.
# В этом задании вы сами решаете какие атрибуты создавать внутри класса, главное реализовать магические
# методы из списка выше


class Building:

    def __init__(self, floors):
        self.floors = [None for _ in range(floors)]

    def __setitem__(self, key, value):
        if 0 <= key < len(self.floors):
            self.floors[key] = value

    def __getitem__(self, item):
        if 0 <= item < len(self.floors):
            return self.floors[item]

    def __delitem__(self, key):
        if 0 <= key < len(self.floors):
            self.floors[key] = None


iron_building = Building(22)  # Создаем здание с 22 этажами
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building[2])
del iron_building[2]
print(iron_building[2])
