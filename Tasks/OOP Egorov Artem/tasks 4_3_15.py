# Пицца
# Теперь пиццерия хочет сделать красивое строковое представление для классов Pizza и Ingredient.
#
# Представление класса Ingredient должно состоять из имени и количества грамм ингредиента.
#
# Представление класса Pizza должно начинаться с фразы
#
# Пицца <имя_пиццы> состоит из:
# и далее в отдельных строках должны быть перечислены все ингредиенты пиццы в порядке уменьшения количества грамм.
#
#
#
# Начальная реализация классов Pizza и Ingredient уже имеется, необходимо дописать строковое представление.
#
# Sample Input 1:
#
# barbecue = Pizza('BBQ', [
#     Ingredient('chicken', 200),
#     Ingredient('mozzarella', 300),
#     Ingredient('sauce bbq', 150),
#     Ingredient('red onion', 150)
# ])
#
# print(barbecue)
# Sample Output 1:
#
# Пицца BBQ состоит из:
# mozzarella: 300г.
# chicken: 200г.
# sauce bbq: 150г.
# red onion: 150г.
# Sample Input 2:
#
# tomatoes = Ingredient('tomatoes', 200)
# cheese = Ingredient('mozzarella', 400)
# print(tomatoes)
# print(cheese)
#
# peperoni = Pizza('Пеперони')
# peperoni.ingredients.append(tomatoes)
# peperoni.ingredients.append(cheese)
# print(peperoni)
# Sample Output 2:
#
# tomatoes: 200г.
# mozzarella: 400г.
# Пицца Пеперони состоит из:
# mozzarella: 400г.
# tomatoes: 200г.


class Ingredient:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f'{self.name}: {self.weight}г.'


class Pizza:
    def __init__(self, name, ingredients=None):
        self.name = name
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients

    def __str__(self):
        a = '\n'
        return f'Пицца {self.name} состоит из:{a}{a.join(map(str, sorted(self.ingredients, key=lambda x: -x.weight)))}'


barbecue = Pizza('BBQ', [
    Ingredient('chicken', 200),
    Ingredient('mozzarella', 300),
    Ingredient('sauce bbq', 150),
    Ingredient('red onion', 150)
])
# print(type(barbecue.ingredients), barbecue.ingredients)
# print(barbecue.ingredients[0])
print(barbecue)
