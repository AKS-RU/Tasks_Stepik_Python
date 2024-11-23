# Бронирование номеров в отеле
# Перед вами уже практически готовая программа по оформлению бронирования номеров для отельного
# бизнеса. В ней присутствуют несколько классов, а именно:
#
# класс Customer - покупатель, хранит в себе имя и телефон потенциального посетителя отеля
#
# класс ReservationPeriod - период бронирования, хранит в себе только даты начала и конца
# желаемой поездки
#
# класс Room - номер в отеле, хранит в себе номер и список периодов забронированных дат
# (экземпляров класса ReservationPeriod)
#
# класс Hotel - отель, хранит в себе название и комнаты
#
# класс Reservation - резервация или бронирование комнаты в отеле. Для выполнения бронирования
# нам нужно знать данные покупателя, данные отеля и даты поездки. Если в отеле найдется свободная
# комната, то бронирование должно успешно состояться, иначе предупреждаем покупателя о том, что в
# заданный период невозможно заселиться в номер отеля
# Вам необходимо дописать реализацию нескольких методов, чтобы программа заработала.
# Проанализируйте код классов и код, который выполняет действия над классами, и тогда вы поймете,
# что нужно доделать, чтобы все заработало


from datetime import date


class Customer:
    def __init__(self, name: int, phone: str):
        self.name = name
        self.phone = phone


class ReservationPeriod:
    def __init__(self, start_date: date, end_date: date):
        self.start_date = start_date
        self.end_date = end_date


class Room:
    def __init__(self, room_number: int):
        self.room_number = room_number
        self.reservation_periods = []  # Список периодов бронирования для этой комнаты

    def is_available(self, start_date: date, end_date: date) -> bool:
        """Проверить доступность комнаты на указанный период."""
        return start_date >= self.reservation_periods[1] or end_date <= self.reservation_periods[0]

    def reserve(self, start_date: date, end_date: date) -> bool:
        """Забронировать комнату на указанный период, если она доступна"""
        if len(self.reservation_periods) == 0 or self.is_available(start_date, end_date):
            self.reservation_periods.append(start_date)
            self.reservation_periods.append(end_date)
            return start_date, end_date

    def cancel_reservation(self, start_date: date, end_date: date) -> bool:
        """Отменить бронирование на указанный период."""
        self.reservation_periods.remove(start_date)
        self.reservation_periods.remove(end_date)
        return self.reservation_periods


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = {}  # Словарь для хранения комнат в отеле

    def add_room(self, room_number):
        """Добавить комнату в отель."""
        self.rooms[room_number] = Room(room_number)

    def reserve_room(self, room_number, start_date: date, end_date: date):
        """Забронировать комнату на указанный период."""
        if room_number in self.rooms:
            return self.rooms[room_number].reserve(start_date, end_date)
        else:
            return False

    def cancel_reservation(self, room_number, start_date: date, end_date: date):
        """Отменить бронирование комнаты на указанный период."""
        if room_number in self.rooms:
            return self.rooms[room_number].cancel_reservation(start_date, end_date)
        else:
            return False


class Reservation:
    def __init__(self, hotel, customer, room_number, start_date: date, end_date: date):
        self.hotel = hotel
        self.customer = customer
        self.room_number = room_number
        self.start_date = start_date
        self.end_date = end_date

    def make_reservation(self):
        """Попытаться забронировать комнату на указанный период."""
        if self.hotel.reserve_room(self.room_number, self.start_date, self.end_date):
            return f"Бронирование успешно: {self.customer.name} забронировал комнату {self.room_number} в отеле {self.hotel.name} на период с {self.start_date.strftime('%Y-%m-%d')} по {self.end_date.strftime('%Y-%m-%d')}."
        else:
            return f"Извините {self.customer.name}, но комната {self.room_number} в отеле {self.hotel.name} на указанный период недоступна."

    def cancel_reservation(self):
        """Отменить бронирование комнаты на указанный период."""
        if self.hotel.cancel_reservation(self.room_number, self.start_date, self.end_date):
            return f"Бронирование отменено: {self.customer.name} отменил бронирование комнаты {self.room_number} в отеле {self.hotel.name} на период с {self.start_date.strftime('%Y-%m-%d')} по {self.end_date.strftime('%Y-%m-%d')}."
        else:
            return f"Ошибка отмены бронирования: комната {self.room_number} в отеле {self.hotel.name} на указанный период не найдена."


# Создаем объекты покупателя и отеля
customer1 = Customer("Иван", "123-456-789")
customer2 = Customer("Петя", "789-456-123")
hotel1 = Hotel("Отель 'Летний бриз'")

# Добавляем комнаты в отель
hotel1.add_room(101)
hotel1.add_room(102)
hotel1.add_room(103)

# Создаем заказ и пытаемся забронировать комнату на период
reservation1 = Reservation(hotel1, customer1, 101, date(2023, 9, 25), date(2023, 9, 28))
result1 = reservation1.make_reservation()
print(result1)

# Пытаемся забронировать ту же комнату на тот же период
result2 = reservation1.make_reservation()
print(result2)
#
# Пытаемся забронировать ту же комнату другим покупателем с пересекающимся интервалом
reservation2 = Reservation(hotel1, customer2, 101, date(2023, 9, 27), date(2023, 9, 30))
print(reservation2.make_reservation())
#
# Меняем дату заезда, прежний посетитель в этот день должен выехать из номера
reservation2.start_date = date(2023, 9, 28)
print(reservation2.make_reservation())
#
# Отменяем бронирование
cancel_result = reservation1.cancel_reservation()
print(cancel_result)

# Пытаемся забронировать комнату после отмены
result3 = reservation1.make_reservation()
print(result3)
