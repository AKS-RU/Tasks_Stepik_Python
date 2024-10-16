# Создайте класс Zebra, внутри которого есть метод which_stripe , который поочередно печатает фразы «Полоска белая»,
# «Полоска черная» без кавычек, начиная именно с фразы «Полоска белая».
#
# Также реализуйте метод run_away, который печатает фразу «Oh, Sugar Honey Ice Tea».


class Zebra():

    def __init__(self):
        self.count = 1

    def which_stripe(self):
        print('Полоска белая' if self.count % 2 else 'Полоска черная')
        self.count += 1

    def run_away(self):
        print('Oh, Sugar Honey Ice Tea')


zebra_1 = Zebra()
zebra_2 = Zebra()
zebra_1.which_stripe()
zebra_2.which_stripe()
zebra_1.which_stripe()
zebra_1.which_stripe()
zebra_1.which_stripe()
zebra_2.which_stripe()
zebra_2.which_stripe()
