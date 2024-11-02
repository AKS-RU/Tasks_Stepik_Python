# Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.
#
# В классе Counter нужно определить:
#
# Метод start_from, который принимает один необязательный аргумент — значение, с которого начинается подсчет
# (по умолчанию равно 0);
#
# Метод increment, который увеличивает счетчик на 1;
#
# Метод display, который печатает фразу «Текущее значение счетчика = <value>»;
#
# Метод reset,  который обнуляет накопившееся значение счетчика.
# Необходимо написать только определение класса Counter


class Counter:

    def start_from(self, start: int = 0):
        self.cnt = start

    def increment(self):
        self.cnt += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.cnt}')

    def reset(self):
        self.cnt = 0


c2 = Counter()
c2.start_from()
c2.display()  # печатает 0
c2.increment()
c2.display()  # печатает 1
c2.increment()
c2.display()  # печатает 2
