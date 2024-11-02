#                           Пицца
# Программист Терентий создал для ближайшей пиццерии класс Pizza
#
# class Pizza:
#     def __init__(self, ingredients=None):
#         if ingredients is None:
#             ingredients = []
#         self.ingredients = ingredients
# который позволяет создавать пиццу с различными ингредиентами
#
# mozzarella = Pizza(['mozzarella', 'tomatoes'])
# pizza_ham = Pizza(['mozzarella', 'ham'])
# hawaii = Pizza(['mozzarella', 'tomatoes', 'pineapple', 'chicken'])
# print(mozzarella.ingredients)
# print(pizza)
# Но вскоре пиццерия поняла, что все гости заказывают только одни и те же виды пицц:
#
# маргарита (состав: mozzarella, tomatoes);
#
# пеперони (состав: mozzarella, peperoni, tomatoes);
#
# барбекю (состав: mozzarella, red onion, sauce bbq, chicken);
# Им стало неудобно каждый раз при создании пиццы перечислять одни и те же ингредиенты, поэтому они попросили
# Терентия написать методы для создания каждого вида пиццы.
#
# Терентий убежал на пары, поэтому вы за него. Нужно создать следующие методы:
#
# margherita
# peperoni
# barbecue
# Каждый метод должен возвращать новую созданную пиццу соответствующего типа. Состав каждого вида пиццы указан выше.
#
# Написать нужно только определение класса Pizza, сама реализация  методов на ваше усмотрение.


class Pizza:

    def __init__(self, ingredients=None):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def peperoni(cls):
        return cls(['mozzarella', 'peperoni', 'tomatoes'])

    @classmethod
    def barbecue(cls):
        return cls(['chicken', 'mozzarella', 'red onion', 'sauce bbq'])


pizza = Pizza()

bbq = pizza.barbecue()
peperoni = pizza.peperoni()
print(sorted(bbq.ingredients))
print(sorted(peperoni.ingredients))
